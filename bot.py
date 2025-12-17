from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("ثبت نام رایگان", callback_data="free")],
        [InlineKeyboardButton("عضویت پولی", callback_data="paid")],
        [InlineKeyboardButton("کمک یک‌باره", callback_data="one")]
    ]
    await update.message.reply_text(
        "به ربات Kevin Trudeau Fan Club خوش آمدید 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()

    if q.data == "free":
        await q.message.reply_text("ثبت‌نام رایگان:\nhttps://kevintrudeaufanclub.com")
    elif q.data == "paid":
        await q.message.reply_text("سطوح عضویت: Bronze تا Patron")
    elif q.data == "one":
        await q.message.reply_text("One-Time Contribution فعال است")

def run():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))
    app.run_polling()
