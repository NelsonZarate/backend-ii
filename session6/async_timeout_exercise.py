"""Session 6 exercise: launching tasks with timeout and handling cancellations."""
import asyncio

async def long_task(name: str, delay: float):
    try:
        await asyncio.sleep(delay)
        return f"{name} done"
    except asyncio.CancelledError:
        return f"{name} cancelled"

async def main():
    task1 = asyncio.create_task(long_task("t1", 2))
    task2 = asyncio.create_task(long_task("t2", 4))
    try:
        res = await asyncio.wait_for(task1, timeout=3)
    except asyncio.TimeoutError:
        res = "t1 timed out"
    # cancel task2 early
    task2.cancel()
    res2 = await task2
    return res, res2

if __name__ == "__main__":
    print(asyncio.run(main()))
