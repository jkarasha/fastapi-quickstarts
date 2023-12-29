from typing import Optional, Any
from fastapi import FastAPI, APIRouter, status, Query, HTTPException, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path

from schemas import Recipe, RecipeSearchResults, RecipeCreate

from recipe_data import RECIPES

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

app = FastAPI(title="Recipe API", openapi_url="/openapi.json")

api_router = APIRouter()

@api_router.get("/", status_code=status.HTTP_200_OK)
def root(request: Request) -> dict:
    """
    Root GET
    """
    return TEMPLATES.TemplateResponse(
        "index.html",
         {"request": request, "recipes": RECIPES}
    )

@api_router.get("/recipe/{recipe_id}", status_code=status.HTTP_200_OK, response_model=Recipe)
def fetch_recipe(*, recipe_id: int) -> Any:
    """
    Fetch a recipe by ID
    """
    result = [recipe for recipe in RECIPES if recipe["id"] == recipe_id]
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Recipe with ID {recipe_id} not found"
        )
    return result[0]

@api_router.get("/search/", status_code=status.HTTP_200_OK, response_model=RecipeSearchResults)
def search_recipes(keyword: Optional[str]=Query("Tofu", min_length=3, example="chicken"), max_results: Optional[int]=10) -> dict:
    """
    Search for recipes by label keyword
    """
    if not keyword:
        return {"results": RECIPES[:max_results]}
    #
    # lambda function to match recipes by keyword, use lambda function to filter recipes by keyword
    results = filter(lambda recipe: keyword.lower() in recipe["label"].lower(), RECIPES)
    # filter returns an iterator, so we need to convert it to a list
    return {"results": list(results)[:max_results]}

@api_router.post("/recipe/", status_code=status.HTTP_201_CREATED, response_model=Recipe)
def create_recipe(*, recipe: RecipeCreate) -> dict:
    """
    Create a new recipe
    """
    new_entry_id = len(RECIPES) + 1
    recipe_entry = Recipe(
        id=new_entry_id,
        label=recipe.label,
        source=recipe.source,
        url=recipe.url,
    )
    RECIPES.append(recipe_entry.model_dump())
    return recipe_entry

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, log_level="debug")
