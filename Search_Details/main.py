from fastapi import FastAPI
from ..router import user,admin,news_scrape,intern_scrape
from .loggings import logger




app = FastAPI()




logger.debug("Debugging Authentication")
#app.include_router(authentication.router)

logger.debug("Debugging User")
app.include_router(user.router)


logger.debug("Debugging News scrape")
app.include_router(news_scrape.router)


logger.debug("Debugging Intern scrape")
app.include_router(intern_scrape.router)


logger.debug("Debugging Admin")
app.include_router(admin.router)




