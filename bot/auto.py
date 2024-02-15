
from telegram import *
from telegram.ext import *
import random

from variables import text
import media
from constants import url
from hooks import api


async def messages(context: ContextTypes.DEFAULT_TYPE) -> None:
    job = context.job
    messages = [text.ABOUT, text.AIRDROP, text.ECOSYSTEM,
                text.VOLUME, random.choice(text.QUOTES)]
    random_message = random.choice(messages)
    if random_message in text.QUOTES:
        message = f"*X7 Finance Whitepaper Quote*\n\n{random_message}"
    else:
        message = random_message

    await context.bot.send_photo(
        chat_id=job.chat_id,
        photo=api.get_random_pioneer(),
    )

    await context.bot.send_message(
        chat_id=job.chat_id,
        text=f"{message}",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="Xchange App", url=f"{url.XCHANGE}")],
                [InlineKeyboardButton(text="Website", url=f"{url.WEBSITE}")],
            ]
        ),
    )


async def replies(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = f"{update.effective_message.text}"
    lower_message = message.lower()
    keyword_to_response = {
        "https://twitter": {
            "text": random.choice(text.X_REPLIES),
            "mode": None,
        },
        "https://x.com": {
            "text": random.choice(text.X_REPLIES),
            "mode": None,
        },
        "gm": {"sticker": media.GM},
        "gm!": {"sticker": media.GM},
        "new on chain message": {"sticker": media.ONCHAIN},
        "lfg": {"sticker": media.LFG},
        "goat": {"sticker": media.GOAT},
        "smashed": {"sticker": media.SMASHED},
        "wagmi": {"sticker": media.WAGMI},
        "slapped": {"sticker": media.SLAPPED},
    }

    words = lower_message.split()

    for keyword, response in keyword_to_response.items():
        if keyword.startswith("https://"):
            if any(word.startswith(keyword) for word in words):
                if "text" in response:
                    await update.message.reply_text(
                        text=response["text"], parse_mode=response["mode"]
                    )
                elif "sticker" in response:
                    await update.message.reply_sticker(sticker=response["sticker"])
        else:
            if (
                f" {keyword} " in f" {lower_message} "
                or lower_message.startswith(keyword + " ")
                or lower_message.endswith(" " + keyword)
            ):
                if "text" in response:
                    await update.message.reply_text(
                        text=response["text"], parse_mode=response["mode"]
                    )
                elif "sticker" in response:
                    await update.message.reply_sticker(sticker=response["sticker"])
