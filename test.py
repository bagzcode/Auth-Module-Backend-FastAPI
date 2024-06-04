from DTOs.CustomResponseMessage import CustomResponseMessage
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path=dotenv_path)

database = os.environ.get("SECRET_KEY")
CustomResponseMessage = CustomResponseMessage()


def response():
    return CustomResponseMessage(status_code=200, message=f"User registered successfully.")


print(response())
