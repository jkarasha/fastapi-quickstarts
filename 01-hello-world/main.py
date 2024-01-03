import time
from fastapi import FastAPI, APIRouter, status, Request, Depends
from fastapi.templating import Jinja2Templates
from pathlib import Path

from sqlalchemy.orm import Session

import api.deps as deps

from api.api_v1.api import api_router
from core.config import settings

import crud

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

app = FastAPI(title="Recipe API", openapi_url="/openapi.json")
root_router = APIRouter()

@root_router.get("/", status_code=status.HTTP_200_OK)
def root(request: Request, db: Session = Depends(deps.get_db)) -> dict:
    """
    Root GET
    """
    recipes = crud.recipe.get_multi(db=db, limit=10)
    return TEMPLATES.TemplateResponse(
        "index.html",
         {"request": request, "recipes": recipes}
    )

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, log_level="debug")
