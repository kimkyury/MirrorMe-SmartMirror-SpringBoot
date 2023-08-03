import asyncio

async def foo(time):
    #while(True):
    await asyncio.sleep(time)
    print(f"{time}")


async def main():
    time_1 = asyncio.create_task(foo(1))
    time_2 = asyncio.create_task(foo(3))

    await time_2
    print(0)
    await time_1


# asyncio.run(main())



