# Image Size Client

The Image Size Client is a Python script designed to fetch image sizes from URLs and update a Google Sheet with the obtained information. It uses the `aiohttp` library for asynchronous HTTP requests, `gspread` for Google Sheets integration, and the `PIL` (Pillow) library for handling images.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/image-size-client.git
    cd image-size-client
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Obtain Google Sheets API credentials:

    - Follow the instructions [here](https://gspread.readthedocs.io/en/latest/oauth2.html) to create a service account and download the JSON key file.

7. Place the downloaded JSON key file in the project directory.

8. Create `.env` file following `.env.example`

## Dependencies

- aiohttp
- gspread
- gspread_asyncio
- tqdm_asyncio
- Pillow (PIL)

### [Sheet with results](https://docs.google.com/spreadsheets/d/1YLapSHmGJHjAAk9jrzIFLUAf8c--LoZU1utiMYdcCxA/edit#gid=1902149593)