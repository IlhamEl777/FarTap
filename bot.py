import aiohttp
import asyncio
import json
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# Skor awal disamain sesuai akunnya
skor_awal = 44158.43
increment = 33

# URL endpoint
url = "https://build.far.quest/wtf/v1/fartap/game"

# Headers
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Api-Key": "far.quest-default-5477272",
    "Origin": "https://far.quest",
    "Priority": "u=1, i",
    "Referer": "https://far.quest/",
    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\", \"Microsoft Edge WebView2\";v=\"126\"",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
    "Authorization": "Bearer xxxxx.xxxx.xxxxx"
}

# Template payload
payload_template = {
    "taps": None,  # This will be updated in each iteration
    "boosts": {},
    "invite": None,
    "quests": {
        "followWieldLabs": True,
        "likeWieldLabsLatest": True,
        "followTgAnnouncement": True,
        "followJcdenton": True
    }
}

async def send_request(skor_awal):
    async with aiohttp.ClientSession() as session:
        payload = payload_template.copy()
        payload["taps"] = skor_awal
        try:
            async with session.post(url, json=payload, headers=headers) as response:
                response_data = await response.json()
                if response_data.get("success"):
                    score = response_data["data"]["score"]
                    print(f"{Fore.GREEN}Sukses | Skor: {score}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Gagal | Respons: {response_data}{Style.RESET_ALL}")
        except json.JSONDecodeError:
            print(f"{Fore.RED}Gagal | Respons JSON tidak valid: {await response.text()}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Gagal | Error: {str(e)}{Style.RESET_ALL}")

async def main():
    skor = skor_awal
    while True:  # Loop tak berujung
        await send_request(skor)
        skor += increment
        await asyncio.sleep(2)  # Tunggu selama 2 detik

# Run the asynchronous main function
asyncio.run(main())
