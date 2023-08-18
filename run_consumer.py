import dotenv

dotenv.load_dotenv()

from interfaces.rabbit.consumer import consume


if __name__ == "__main__":
    import anyio

    anyio.run(consume)
