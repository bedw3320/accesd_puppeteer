# This is a scraping bot for gathering personnal finance data from the various platforms I use online to manage my finances.
# The data is fetched, then pushed to a GSHEET.

import asyncio
import pyppeteer

async def main():
    browser = await pyppeteer.launch()
    page = await browser.newPage()
    await page.goto('https://www.metro.ca/en?ds_rl=1275254&ds_rl=1282314&ds_rl=1282803&gclid=CjwKCAjw8JKbBhBYEiwAs3sxN-BA0S3Qs83_WiwYXkh2vheVx-dmtabDrneiauVq8y0FCHA-rQeg6BoCZTUQAvD_BwE&gclsrc=aw.ds')
    await page.screenshot({'path': 'metro_python.png'})
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())