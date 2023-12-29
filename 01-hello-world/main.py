from typing import Optional
from fastapi import FastAPI, APIRouter, status
app = FastAPI(title="Recipe API", openapi_url="/openapi.json")

api_router = APIRouter()

RECIPES = [
    {
        "id": 1,
        "label": "Chicken Vesuvio",
        "source": "Serious Eats",
        "url": "http://www.seriouseats.com/recipes/2011/12/chicken-vesuvio-recipe.html",
    },
    {
        "id": 2,
        "label": "Chicken Paprikash",
        "source": "No Recipes",
        "url": "http://norecipes.com/recipe/chicken-paprikash/",
    },
    {
        "id": 3,
        "label": "Cauliflower and Tofu Curry Recipe",
        "source": "Serious Eats",
        "url": "http://www.seriouseats.com/recipes/2011/02/cauliflower-and-tofu-curry-recipe.html",
    },
]

@api_router.get("/", status_code=status.HTTP_200_OK)
def root() -> dict:
    """
    Root GET
    """
    return {"message": "Hello World"}

@api_router.get("/recipe/{recipe_id}", status_code=status.HTTP_200_OK)
def fetch_recipe(*, recipe_id: int) -> dict:
    """
    Fetch a recipe by ID
    """
    result = [recipe for recipe in RECIPES if recipe["id"] == recipe_id]
    if result:
        return result[0]

@api_router.get("/search/", status_code=status.HTTP_200_OK)
def search_recipes(keyword: Optional[str]=None, max_results: Optional[int]=10) -> dict:
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

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, log_level="debug")
