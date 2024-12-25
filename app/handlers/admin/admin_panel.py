from aiogram import types, Dispatcher
from aiogram.filters import Command

from loader import _
from app.filters.admin import Admin
from loader import router as dp


@dp.message(Admin(), Command("admin"))
async def _admin_command(message: types.Message):
    await message.answer(
        text=_("You admin!")
    )
