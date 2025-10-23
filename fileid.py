import asyncio
from aiogram import Bot
from aiogram.types import FSInputFile
import os

# 🚨 APNE BOT KA TOKEN YAHAN DAAlein 
# (Same token jo aapne main.py mein use kiya hai)
TOKEN = "8243097610:AAEFbrq5pSnsvyKKGjVy_Zkdu8exfhAio6M" 

# 🚨 APNI PDF FILE KA PATH YAHAN DAAlein
# (Wahi path jise aapne main.py mein theek kiya tha)
print(f"Current Working Directory: {os.getcwd()}")
FILE_PATH = r"Forex-Trading Ultimate.pdf"
FILE_NAME = os.path.basename(FILE_PATH)

# Jis chat_id par aap file bhejna chahte hain
# (Apni khud ki Telegram ID/username/kisi private group ki ID daalein)
# Agar aap ID nahi jante to apni chat ID nikalne ke liye @userinfobot use karein.
CHAT_ID = 7271678268 # <--- APNI CHAT ID YA BOT SE JURI HUI CHAT ID DAALEIN

async def get_file_id():
    bot = Bot(token=TOKEN)
    
    # File check
    if not os.path.exists(FILE_PATH):
        print(f"ERROR: File not found at path: {FILE_PATH}")
        await bot.close()
        return

    print(f"Attempting to upload file: {FILE_NAME}")
    
    # FSInputFile se file ko load karein
    document_to_send = FSInputFile(FILE_PATH)
    
    try:
        # File ko send karein
        sent_message = await bot.send_document(
            chat_id=CHAT_ID,
            document=document_to_send,
            caption=f"File uploaded successfully! ID for {FILE_NAME} is below."
        )
        
        # Sent message object mein se File ID nikalna
        file_id = sent_message.document.file_id
        
        print("\n" + "="*50)
        print("✅ SUCCESS: FILE ID FOUND!")
        print(f"File Name: {FILE_NAME}")
        print(f"FILE ID: {file_id}")
        print("="*50 + "\n")
        print("COPY THE FILE ID ABOVE AND PASTE IT INTO main.py")
        
    except Exception as e:
        print("\n" + "="*50)
        print(f"❌ ERROR DURING UPLOAD: {e}")
        print("Please check your TOKEN, CHAT_ID, and network connection.")
        print("="*50 + "\n")

    finally:
        await bot.close()

if __name__ == "__main__":
    asyncio.run(get_file_id())