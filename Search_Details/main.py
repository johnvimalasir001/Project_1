from fastapi import FastAPI
from .router import user,admin
from .loggings import logger




app = FastAPI()


logger.debug("Debugging Authentication")
#app.include_router(authentication.router)

logger.debug("Debugging User")
app.include_router(user.router)

logger.debug("Debugging Admin")
app.include_router(admin.router)

