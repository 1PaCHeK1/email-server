import uvicorn
import dotenv


if __name__ == "__main__":
    dotenv.load_dotenv()
    uvicorn.run(
        "interfaces.api.app:create_app",
        reload=True,
        factory=True,
    )
