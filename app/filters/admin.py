from aiogram.filters import Filter
from aiogram.types import Message
from data.config import ADMINS

class Admin(Filter):
    async def __call__(self, message: Message) -> bool:
        return bool(int(message.from_user.id) in ADMINS)

        