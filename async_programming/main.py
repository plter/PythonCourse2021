# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import asyncio


async def print_hi(name):
    await asyncio.sleep(1)
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


async def main():
    await print_hi("Python")


if __name__ == '__main__':
    asyncio.run(main())
