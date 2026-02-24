import asyncio
import aiohttp
import time

URL = "https://orlia26.vercel.app"  # Replace with your site
TOTAL_REQUESTS = 2_000_000  # 2 Million requests
BATCH_SIZE = 500  # Concurrent requests per batch
TIMEOUT = 10  # seconds per request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

async def fetch(session):
    try:
        async with session.get(URL, headers=HEADERS) as response:
            await response.text()
            return response.status
    except Exception as e:
        return str(e)

async def run_load_test():
    connector = aiohttp.TCPConnector(limit=1000, force_close=True)
    timeout = aiohttp.ClientTimeout(total=TIMEOUT)
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        start_time = time.time()
        total_sent = 0
        total_success = 0
        total_failed = 0
        batch_num = 0

        print(f"Starting load test on {URL}")
        print(f"Total Requests: {TOTAL_REQUESTS:,} | Batch Size: {BATCH_SIZE}\n")

        while total_sent < TOTAL_REQUESTS:
            batch_num += 1
            remaining = TOTAL_REQUESTS - total_sent
            current_batch = min(BATCH_SIZE, remaining)

            tasks = [fetch(session) for _ in range(current_batch)]
            batch_start = time.time()

            results = await asyncio.gather(*tasks)

            total_sent += len(results)

            success = sum(1 for r in results if isinstance(r, int))
            failed = len(results) - success
            total_success += success
            total_failed += failed

            elapsed = time.time() - batch_start
            progress = (total_sent / TOTAL_REQUESTS) * 100
            print(f"Batch {batch_num} | Sent: {total_sent:,}/{TOTAL_REQUESTS:,} ({progress:.1f}%) | Reached: {success} | Errors: {failed} | Time: {elapsed:.2f}s")
            if failed > 0:
                errors = [r for r in results if not isinstance(r, int)]
                print(f"  Error sample: {errors[0]}")

        total_time = time.time() - start_time
        print(f"\n--- Results ---")
        print(f"Total Requests Sent: {total_sent:,}")
        print(f"Reached Server: {total_success:,} | Connection Errors: {total_failed:,}")
        print(f"Total Time: {total_time:.2f}s")
        print(f"Requests/sec: {total_sent / total_time:.0f}")

if __name__ == "__main__":
    asyncio.run(run_load_test())
