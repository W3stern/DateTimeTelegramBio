from telethon import TelegramClient, functions
import asyncio
from datetime import datetime
import os

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
session_name = 'mysession'

async def main():
    try:
        print('Connecting...')
        async with TelegramClient(session_name, api_id, api_hash) as client:
            print('Connected!')
            while True:
                now = datetime.now().strftime("⏰ %H:%M")
                await client(functions.account.UpdateProfileRequest(about=now))
                print(f"Updated bio to: {now}")
                await asyncio.sleep(60)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    asyncio.run(main())
