from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from loader import _


async def base_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="click", callback_data="callback"),
            ],
        ],
    )
    return ikb
