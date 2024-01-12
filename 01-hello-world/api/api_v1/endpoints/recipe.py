import asyncio
import httpx
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import Any, Optional

import crud
from api import deps
from clients.reddit import RedditClient
from schemas.recipe import (
    Recipe,
    RecipeCreate,
    RecipeSearchResults,
    RecipeUpdateRestricted
)
from models.user import User

router = APIRouter()
RECIPE_SUBREDDITS = ["recipes", "easyrecipes", "topsecretrecipes"]

@router.get("/{recipe_id}", status_code=status.HTTP_200_OK, response_model=Recipe)
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

@router.get("/", status_code=status.HTTP_200_OK, response_model=RecipeSearchResults)
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

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Recipe)
def create_recipe(
            *, 
            recipe_in: RecipeCreate,
            db: Session = Depends(deps.get_db),
            current_user: User = Depends(deps.get_current_user)
    ) -> dict:
    """
    Create a new recipe
    """
    recipe = crud.recipe.create(db=db, obj_in=recipe_in)
    return recipe

async def get_reddit_top_async(subreddit: str) -> list:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5",
            headers={"User-Agent": "recipe bot 0.1"},
        )
    #
    subreddit_recipes = response.json()
    subreddit_data = []
    #
    for entry in subreddit_recipes["data"]["children"]:
        score = entry["data"]["score"]
        title = entry["data"]["title"]
        link = entry["data"]["url"]
        #
        subreddit_data.append(f"{str(score)}: {title} ({link})")
    return subreddit_data

def get_reddit_top(subreddit: str) -> list:
    response = httpx.get(
        f"https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5",
        headers={"User-agent": "recipe bot 0.1"},
    )
    subreddit_recipes = response.json()
    subreddit_data = []
    for entry in subreddit_recipes["data"]["children"]:
        score = entry["data"]["score"]
        title = entry["data"]["title"]
        link = entry["data"]["url"]
        subreddit_data.append(f"{str(score)}: {title} ({link})")
    return subreddit_data

@router.get("/ideas/async")
async def fetch_ideas_async(
    user: User = Depends(deps.get_current_active_superuser)
    ) -> dict:
    results = await asyncio.gather(
        *[get_reddit_top_async(subreddit=subreddit) for subreddit in RECIPE_SUBREDDITS]
    )
    #
    return dict(zip(RECIPE_SUBREDDITS, results))

@router.get("/ideas/")
def fetch_ideas(reddit_client: RedditClient = Depends(deps.get_reddit_client)) -> dict:
    return {key: reddit_client.get_reddit_top(subreddit=key) for key in RECIPE_SUBREDDITS}
