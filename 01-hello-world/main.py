from typing import Optional, Any
from fastapi import FastAPI, APIRouter, status, Query, HTTPException, Request, Depends
from fastapi.templating import Jinja2Templates
from pathlib import Path

from sqlalchemy.orm import Session
from schemas.recipe import Recipe, RecipeSearchResults, RecipeCreate

from recipe_data import RECIPES
import deps
import crud

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

app = FastAPI(title="Recipe API", openapi_url="/openapi.json")

api_router = APIRouter()

@api_router.get("/", status_code=status.HTTP_200_OK)
def root(request: Request, db: Session = Depends(deps.get_db)) -> dict:
    """
    Root GET
    """
    return TEMPLATES.TemplateResponse(
        "index.html",
         {"request": request, "recipes": RECIPES}
    )

@api_router.get("/recipe/{recipe_id}", status_code=status.HTTP_200_OK, response_model=Recipe)
def fetch_recipe(*, recipe_id: int, db: Session = Depends(deps.get_db)) -> Any:
    """
    Fetch a recipe by ID
    """
    result = crud.recipe.get(db=db, id=recipe_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Recipe with ID {recipe_id} not found"
        )
    return result

@api_router.get("/search/", status_code=status.HTTP_200_OK, response_model=RecipeSearchResults)
def search_recipes(
    keyword: Optional[str]=Query("Tofu",min_length=3, example="chicken"),
    max_results: Optional[int]=10,
    db: Session = Depends(deps.get_db)) -> dict:
    """
    Search for recipes by label keyword
    """
    recipes = crud.recipe.get_multi(db=db, limit=max_results)
    if not keyword:
        return {"results": recipes}
    #
    # lambda function to match recipes by keyword, use lambda function to filter recipes by keyword
    results = filter(lambda recipe: keyword.lower() in recipe.label.lower(), recipes)
    # filter returns an iterator, so we need to convert it to a list
    return {"results": list(results)[:max_results]}

@api_router.post("/recipe/", status_code=status.HTTP_201_CREATED, response_model=Recipe)
def create_recipe(*, recipe_in: RecipeCreate, db: Session = Depends(deps.get_db),) -> dict:
    """
    Create a new recipe
    """
    recipe = crud.recipe.create(db=db, obj_in=recipe_in)
    return recipe

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, log_level="debug")
