import asyncio

# Async function with a delay
async def task(num):
    print(f"Task {num} started.")
    await asyncio.sleep(num)  # Simulate a delay
    print(f"Task {num} finished.")

# Process multiple tasks with a for loop
async def main():
    tasks = [task(i) for i in range(1, 4)]  # Create tasks 1, 2, 3
    await asyncio.gather(*tasks)  # Run them concurrently

asyncio.run(main())
