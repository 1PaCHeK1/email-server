import dotenv
dotenv.load_dotenv(".env")

from core.di import create_container
from core.domain.email.services import SmtpService
from asyncio import run


async def main():
    container = create_container()
    context = container.context()
    service = await context.resolve(SmtpService)
    service.send(["maksyutov.vlad@gmail.com", "hello"])

run(main())
