
from aiogram import Dispatcher
from aiogram.types import ErrorEvent

from utils import logger

from .admin import dp as router
from .user import dp as router


def setup_handlers(dp: Dispatcher) -> None:
    @dp.error()
    async def _error(event: ErrorEvent):
        logger.exception(event.exception)

    dp.include_routers(router)