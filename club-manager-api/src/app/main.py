from fastapi import FastAPI
from app.api import orgs, users
from app.config import settings

app = FastAPI(
    title=settings.project_name,
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

@app.get("/")
def index():
    return {"message": "Hello World!"} 

app.include_router(orgs.org_router, prefix="/orgs", tags=["org"])
app.include_router(users.user_router, prefix="/users", tags=["users"])