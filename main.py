from flask import Flask
from threading import Thread
import telebot

bot = telebot.TeleBot("8243097610:AAEFbrq5pSnsvyKKGjVy_Zkdu8exfhAio6M")
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! Bot is running fine.")

keep_alive()
bot.polling()

import asyncio
from aiogram.types import FSInputFile, BufferedInputFile
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import os # File path aur operations ke liye zaroori
from dotenv import load_dotenv
load_dotenv()

# ======================================================================
# 1. Configuration & Constants ⚙️
# ======================================================================

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    print("Error: BOT_TOKEN environment variable nahi mila. .env file check karein.")
    exit()

# ⚠️ APNE IDs AUR LINKS YAHAN DAAlein

SUPPORT_USERNAME = "traderdivu" 
RAZORPAY_LINK = os.environ.get("RAZORPAY_LINK")
if not RAZORPAY_LINK:
    print("Error: RAZORPAY_LINK environment variable nahi mila.")
    exit()

bot = Bot(token=TOKEN)
dp = Dispatcher()

# File IDs (Aapke diye gaye valid IDs)
SIMPLE_PDF_ID = "BQACAgUAAxkDAAIBeWj55GDfzbVMEpMPaKthR19JvJEUAAL9GAAC_n_RVzb0hEZTjh5WNgQ"
FOREX_PDF_ID = "BQACAgUAAxkDAAIBgGj55cKqvTmo7LHXfntn6wdqZwxJAAICGQAC_n_RV5kzSTpx0VFuNgQ"

# ======================================================================
# 2. Keyboards Setup (Reply & Inline) ⌨️
# ======================================================================

# Reply Keyboard
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🚀 Start")],
        [KeyboardButton(text="❓ Help"), KeyboardButton(text="🤝 Support")],
    ],
    resize_keyboard=True
)

# Inline Keyboard
inline_keyboard_options = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📈 Simple Trading", callback_data="charts"),
            InlineKeyboardButton(text="💵 Forex Trading", callback_data="forex_trade")
        ],
        [InlineKeyboardButton(text="✨ Pro Insights (Options)", callback_data="vip_notes")],
        [InlineKeyboardButton(text="📊 Market Strategis", callback_data="market")],
    ]
)

# ======================================================================
# 3. Message Handlers (Non-Inline Buttons) 💬
# ======================================================================

@dp.message(Command("start")) 
async def start_command_handler(message: Message):
    await message.answer(
        "👋 Welcome to ChartVault Pro! Please select '🚀 Start' from the keyboard below to begin your trading journey.",
        reply_markup=main_keyboard,
        parse_mode="Markdown"
    )

@dp.message(lambda message: message.text == "🚀 Start")
async def trading_start_handler(message: Message):
    await message.answer(
        "🚀 *Trading Journey Start!* Select an option below:",
        reply_markup=inline_keyboard_options,
        parse_mode="Markdown"
    )

@dp.message(lambda message: message.text == "❓ Help")
async def help_handler(message: Message):
    help_text = (
        "Welcome to the ChartVault Pro Help Center! 🤖\n\n"
        "This bot is designed to guide your trading journey through the following main features:\n\n"
        "<b>1. Trading Options:</b>\n\n"
        "• <b>Simple Trading:</b> Access fundamental resources and basic market documents.\n"
        "• <b> Pro Insights (Options):</b> Unlock premium strategies and Masterclass content.\n"
        "• <b>Market Strategis:</b> View upcoming features like Live Market Analysis.\n\n"
        "<b>2. Navigation & Assistance:</b>\n\n"
        "• <b>🚀 Start:</b> Use this button to view all available trading options.\n"
        "• <b>🤝 Support:</b> Use this to directly contact the admin for personalized assistance."
    )
    await message.answer(help_text, parse_mode="HTML")

@dp.message(lambda message: message.text == "🤝 Support")
async def support_handler(message: Message):
    support_link = f"[@{SUPPORT_USERNAME}](https://t.me/{SUPPORT_USERNAME})"
    
    support_text = (
        "Thank you for reaching out to the ChartVault Pro Support team.\n\n"
        "For immediate assistance, please contact the admin directly by clicking the username below:\n\n"
        f"**Support Admin:** {support_link}\n\n"
        "**Please include the following in your message:**\n"
        "1. Your Telegram Username/ID.\n"
        "2. A clear description of the issue or question.\n\n"
        "We typically respond within 24 hours. We appreciate your patience!"
    )
    await message.answer(support_text, parse_mode="Markdown")

# ======================================================================
# 4. Inline Callback Handlers (Actions) 🧠
# ======================================================================

# 📈 SIMPLE TRADING (PDF Sharing)
@dp.callback_query(lambda c: c.data == "charts")
async def charts_handler(callback: types.CallbackQuery):
    await callback.answer() 
    
    # 🚨 FIX: Purane message ko edit kiya aur buttons hataye
    await callback.message.edit_text(
        text="📈 Simple Trading",
        reply_markup=None 
    )
    
    # PDF File ID use karke document send karein
    await callback.message.answer_document(
        document=SIMPLE_PDF_ID, 
        caption="✅ Here is your FREE Simple Trading Guide (PDF). \n\n🤔This document was sourced via a different channel and additional research. Consequently, I am not confident in its reliability."
    )

# 💵 FOREX TRADING (PDF Sharing)
@dp.callback_query(lambda c: c.data == "forex_trade")
async def forex_handler(callback: types.CallbackQuery):
    await callback.answer()
    chr
    # 🚨 FIX: Purane message ko edit kiya aur buttons hataye
    await callback.message.edit_text(
        text="💵 Forex Trading",
        reply_markup=None 
    )
    
    # Document bhejna File ID ka use karke
    forex_caption = (
        "🚀 **Master the Currency Market!**\n\n"
        "Here is your complimentary **Forex Trading Starter Guide** (PDF). 📘\n\n"
        "This essential guide provides a solid foundation, covering:\n"
        "✅ Core currency pair analysis\n"
        "✅ Key market terminologies\n"
        "✅ Risk management basics\n\n"
        "Start your journey to understanding global finance. Happy Trading! 📈"
    )
    await callback.message.answer_document(
        document=FOREX_PDF_ID, 
        caption=forex_caption,
        parse_mode="Markdown"
    )

# 🧠 ELITE OPTIONS (Payment Link)
@dp.callback_query(lambda c: c.data == "vip_notes")
async def vip_notes_handler(callback: types.CallbackQuery):
    await callback.answer()
    
    support_link = f"[@{SUPPORT_USERNAME}](https://t.me/{SUPPORT_USERNAME})"
    
    # Buy Button (Inline Keyboard) Create Karein
    buy_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💳 Buy Now (₹1199)", 
                    url=RAZORPAY_LINK,
                )
            ]
        ]
    )
    
    # Information text with clear instructions
    info_text = (
        f"💎 **ChartVault Pro: Elite Options Masterclass**\n\n"
        f"Stop guessing. Start trading with an edge. This guide unlocks the advanced strategies pros use.\n\n"
        f"**What You Will Master:**\n"
        f"✅ **Advanced Chart Patterns:**🎯 Access premium patterns you won't find elsewhere.\n"
        f"✅ **In-Depth VIP Insights:** 🔎Enhance your analysis and understand the *why* behind market moves.\n"
        f"✅ **Informed Decisions:** 👉Move from reacting to the market to anticipating it.\n\n"
        f"**Price:** ₹1199 (approx. $13.60 USD)\n\n"
    )
    
    # 🚨 FIX: Message ko edit kiya aur buttons hataye
    await callback.message.edit_text(
        text="✨ Pro Insights (Options)",
        reply_markup=None 
    )
    
    # Final message send karein (yeh message mein Buy button hoga)
    await callback.message.answer(
        info_text,
        reply_markup=buy_keyboard,
        parse_mode="Markdown"
    )

# 📊 MARKET STRATEGIS (Simple Placeholder)
@dp.callback_query(lambda c: c.data == "market")
async def market_handler(callback: types.CallbackQuery):
    await callback.answer()
    
    # 🚨 FIX: Message ko edit kiya aur buttons hataye
    await callback.message.edit_text(
        text="📊 Market Strategis",
        reply_markup=None 
    )
    
    await callback.message.answer(
        "Market Strategis: Live analysis feature is coming soon!..."
    )

# ======================================================================
# 5. Main Execution Loop 🚀
# ======================================================================

async def main():
    print("🤖 ChartVault Pro Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped by user.")

