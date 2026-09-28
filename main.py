import asyncio

from runner import Runner

PATH = "https://dummyjson.com"


runner = Runner(PATH)


async def test_runner():
    runner = Runner(PATH)
    print(runner.get_path())
    response = await runner.get()
    print(response.status_code)


async def main():
    await test_runner()


if __name__ == "__main__":
    asyncio.run(main())
