import asyncio
import requests
import time

# Asynchronous function to get HTML content of a website
async def get_html(url):
    loop = asyncio.get_event_loop()
    # Using run_in_executor to run synchronous requests.get in an asynchronous manner
    response = await loop.run_in_executor(None, requests.get, url)
    return response.text

# Main asynchronous function to gather all tasks
async def main(urls):
    # Using asyncio.gather to run all the tasks concurrently
    tasks = [asyncio.create_task(get_html(url)) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

# URLs to crawl
urls = [
    "https://www.wikipedia.org",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.python.org",
    "https://www.linux.org"
]

# Measure time and execute
start_time = time.time()
html_contents = asyncio.run(main(urls))
end_time = time.time()

# Print time taken
print(f"Time taken: {end_time - start_time} seconds")

# Optionally print HTML contents
for content in html_contents:
    print(len(content))  # Print first 200 characters for brevity
