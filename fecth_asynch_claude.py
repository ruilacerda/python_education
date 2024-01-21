import asyncio
import time
import requests

async def get_html(url):
    resp = requests.get(url)
    return resp.text

async def main():
    start = time.time()
    urls = [
        'https://www.python.org',
        'https://www.google.com',
        'https://www.example.com',
        'https://www.wikipedia.org',
        'https://www.yahoo.com'
    ]
    
    tasks = []
    for url in urls:
        task = asyncio.create_task(get_html(url))
        tasks.append(task)
    
    await asyncio.gather(*tasks)
    
    end = time.time()
    print("Total time taken:", end - start)

if __name__ == '__main__':
    asyncio.run(main())