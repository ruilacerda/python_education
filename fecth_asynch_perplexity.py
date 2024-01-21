import asyncio
import requests
import time

async def fetch_html(url):
    response = requests.get(url)
    return response.text

async def main():
    urls = [
            'https://www.google.com',
            'https://www.yahoo.com',
            'https://www.bbc.com',
            'https://www.wikipedia.org',
            'https://www.amazon.com'
    ]
    tasks = [fetch_html(url) for url in urls]
    start_time = time.time()
    htmls = await asyncio.gather(*tasks)
    end_time = time.time()
    for html in htmls:
        print(len(html))
    print(f'Time taken: {end_time - start_time} seconds')

if __name__ == "__main__":
    asyncio.run(main())
