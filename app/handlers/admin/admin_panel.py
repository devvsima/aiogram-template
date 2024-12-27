from aiogram import types
from aiogram.filters import Command

from loader import _
from loader import router as dp

from app.filters.admin import Admin


@dp.message(Admin(), Command("admin"))
async def _admin_command(message: types.Message) -> None:
    await message.answer(
        text=_("You admin!")
    )
