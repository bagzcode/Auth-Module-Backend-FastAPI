from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from controllers.UserController import user_controller_router
from controllers.ProfileController import profile_controller_router
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

tags_metadata = [
    {"name": "Users", "description": "Operations related to user management"}
]

# Include the routers from controller modules
app.include_router(user_controller_router, prefix="/users", tags=["Users"])
app.include_router(profile_controller_router,
                   prefix="/profile", tags=["Profile"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    uvicorn.run("app:app", host=os.environ.get("HOST"),
                port=int(os.environ.get("PORT")), reload=True)

# @tour_manager_controller_router.get("/get_top_10_dests")
# def get_top_10_destinations(self, token: str = Depends(oauth2_scheme)):
#    self.userService.authenticate(token)
#    return self.tourManagementService.get_top_10_destinations()
