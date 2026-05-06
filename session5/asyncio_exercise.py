"""Session 5 exercise: asyncio.gather to fetch from two simulated sources."""
import asyncio

async def fetch_from_source(name: str, delay: float):
    await asyncio.sleep(delay)
    return f"{name} result"

async def get_both():
    a = fetch_from_source("source_a", 1)
    b = fetch_from_source("source_b", 1.5)
    results = await asyncio.gather(a, b)
    return results

if __name__ == "__main__":
    print(asyncio.run(get_both()))
