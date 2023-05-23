#!/usr/bin/python3
# author ekubo
# 2023年05月23日
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

asyncio.run(main())