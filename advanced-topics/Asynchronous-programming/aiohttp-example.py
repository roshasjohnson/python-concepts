import aiohttp
import asyncio

# Function to fetch user data from the API
async def fetch_user(session, user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    async with session.get(url) as response:
        return await response.json()  # Get the response as JSON

# Main function to run the program
async def main():
    user_ids = [1, 2, 3, 4, 5]  # IDs of users to fetch
    async with aiohttp.ClientSession() as session:
        # Create a list of tasks to fetch all users
        tasks = [fetch_user(session, user_id) for user_id in user_ids]
        # Run all tasks concurrently
        users = await asyncio.gather(*tasks)
        # Print the results
        for user in users:
            print(f"User {user['id']}: {user['name']}")

# Run the program
asyncio.run(main())