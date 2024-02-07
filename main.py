import asyncio
import time
from imagesizeclient import ImageSizeClient


size_client = ImageSizeClient()
start_time = time.perf_counter()
asyncio.run(size_client.main(sheet_url="https://docs.google.com/spreadsheets/d/1YLapSHmGJHjAAk9jrzIFLUAf8c--LoZU1utiMYdcCxA/edit#gid=1902149593"))
end_time = time.perf_counter()
print(f"Elapsed: {end_time - start_time} seconds")