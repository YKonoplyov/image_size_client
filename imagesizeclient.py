import time
import asyncio
from io import BytesIO

from tqdm.asyncio import tqdm_asyncio
import gspread_asyncio
from gspread_asyncio import AsyncioGspreadWorksheet
from gspread.cell import Cell
import aiohttp
from aiohttp.client import ClientResponseError, InvalidURL
from PIL import Image

from utils.utils import get_creds


class ImageSizeClient:
    def __init__(self):
        """Initialize the ImageSizeClient."""
        self.agcm = gspread_asyncio.AsyncioGspreadClientManager(get_creds)
    
    async def get_image_size(
        self,
        session: aiohttp.ClientSession,
        url: str
    ) -> str:
        """Fetch and return the size of an image from a given URL.

        Args:
            session: aiohttp ClientSession instance.
            url (str): URL of the image.

        Returns:
            str: Image size in the format "width x height" or an error message.
        """

        try:
            async with session.get(url) as response:
                response.raise_for_status()
                image_data = await response.read()
                img = Image.open(BytesIO(image_data))
                return f"{img.size[0]}x{img.size[1]}"
        except ClientResponseError:
            return "Image isn't accessible"
        except InvalidURL:
            return("Invalid url")

    async def process_url(
            self,
            session,
            row,
            url,
            size_column
        ):
        """Process an image URL, get its size, and create a Cell object.

        Args:
            session: aiohttp ClientSession instance.
            row (int): Row number in the worksheet.
            url (str): URL of the image.
            size_column (int): Column number where the size should be updated.

        Returns:
            Cell: Cell object containing image size information.
        """
        size = await self.get_image_size(session, url)
        cell = Cell(row=row, col=size_column, value=size)
        return cell

    async def main(self, sheet_url: str) -> None:
        """Main asynchronous function to fetch image sizes and update a Google Sheet.

        Args:
            sheet_url (str): URL of the Google Sheet.

        Returns:
            None
        """
        self.agclient = await self.agcm.authorize()
        spreadsheet = await self.agclient.open_by_url(sheet_url)
        worksheet = (await spreadsheet.worksheets())[0]
        image_column = (await worksheet.find("image_url")).col
        size_column = (await worksheet.find("SIZE")).col
        images_urls = await worksheet.col_values(image_column)

        async with aiohttp.ClientSession() as session:
            tasks = [self.process_url(session, row_num + 2, url, size_column) for row_num, url in enumerate(images_urls[1:])]
            cell_list = await tqdm_asyncio.gather(*tasks)
            
            await worksheet.update_cells(cell_list=cell_list)

