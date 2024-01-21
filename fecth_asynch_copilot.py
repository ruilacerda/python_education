import requests
import asyncio
import time

# A function to fetch the html of a given url
async def fetch_html(url):
    response = requests.get(url)
    return response.text

# A list of 5 websites to crawl
urls = [
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.python.org",
    "https://www.reddit.com",
    "https://www.youtube.com"
]

# A function to create and run the tasks
async def main():
    # Record the start time
    start = time.time()
    # Create a list of tasks
    tasks = [asyncio.create_task(fetch_html(url)) for url in urls]
    # Wait for all the tasks to finish and gather the results
    results = await asyncio.gather(*tasks)
    # Record the end time
    end = time.time()
    # Print the results and the time elapsed
    for url, html in zip(urls, results):
        print(f"The html of {url} is {len(html)} characters long.")
    print(f"It took {end - start} seconds to finish all the tasks.")

# Run the main function
asyncio.run(main())
