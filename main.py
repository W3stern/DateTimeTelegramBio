from telethon import TelegramClient, functions, errors
import asyncio
from datetime import datetime
import os
from zoneinfo import ZoneInfo  # اگر پایتون شما زیر 3.9 است، از pytz استفاده کنید
import random

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
session_name = 'mysession'

def bold_digits(s):
    # تبدیل همه ارقام به math bold
    trans = str.maketrans('0123456789', '𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟯𝟴𝟵')
    return s.translate(trans)

async def main():
    print('Connecting...')
    async with TelegramClient(session_name, api_id, api_hash) as client:
        print('Connected!')
        last_time_str = None
        while True:
            try:
                now_tehran = datetime.now(ZoneInfo('Asia/Tehran'))
                time_str = bold_digits(now_tehran.strftime('| %H:%M'))
                if last_time_str != time_str:
                    await client(functions.account.UpdateProfileRequest(last_name=time_str))
                    print(f"Updated last name to: {time_str}")
                    last_time_str = time_str
                # امن‌تر: 61.2 ثانیه + مقداری تصادفی جزئی
                await asyncio.sleep(61 + random.uniform(0, 2))
            except errors.FloodWaitError as e:
                print(f"Flood wait for {e.seconds} seconds.")
                await asyncio.sleep(e.seconds + 5)  # +5 برای اطمینان
            except Exception as err:
                print("Unknown error:", err)
                await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())
