import asyncio

async def worker(name, delay):
    print(name, "started")
    await asyncio.sleep(delay)
    print(name, "finished")

async def main():
    await asyncio.gather(worker("A", 0.2), worker("B", 0.1))

if __name__ == "__main__":
    asyncio.run(main())
