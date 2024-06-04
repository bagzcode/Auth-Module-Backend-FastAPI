from fastapi import HTTPException, Depends, Header
from fastapi.security import OAuth2PasswordBearer
from services.UserService import UserService
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
import jwt
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path=dotenv_path)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")
profile_controller_router = InferringRouter()


@cbv(profile_controller_router)
class ProfileController:
    def __init__(self):
        self.userService = UserService()

    @profile_controller_router.get("/detail")
    def detailUser(self, token: str = Depends(oauth2_scheme)):
        self.userService.authenticate(token)
        decoded_data = jwt.decode(jwt=token,
                                  key=os.environ.get(
                                      "SECRET_KEY"),
                                  algorithms=[os.environ.get("ALGORITHM")])
        return decoded_data
