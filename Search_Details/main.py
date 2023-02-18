from fastapi import FastAPI
from .router import user,admin,authentication




app = FastAPI()

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(admin.router)

