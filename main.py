from aiogram import Bot, types
from app import middlewares ,filters, handlers
from loader import dp, bot
from utils.logging import logger
import asyncio

async def main():
    # from app.middlewares import setup_middlewares
    # setup_middlewares(dp)
    from app.handlers import setup_handlers
    setup_handlers(dp)
    logger.info("~ Bot_startup")
    await dp.start_polling(     
        bot,
        skip_updates=True,
    )



if __name__ == "__main__":
    asyncio.run(main())
