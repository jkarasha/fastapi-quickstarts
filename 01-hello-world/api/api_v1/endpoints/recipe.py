from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import Any, Optional

import crud
from api import deps
from schemas.recipe import Recipe, RecipeCreate, RecipeSearchResults

router = APIRouter()

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
def create_recipe(*, recipe_in: RecipeCreate, db: Session = Depends(deps.get_db),) -> dict:
    """
    Create a new recipe
    """
    recipe = crud.recipe.create(db=db, obj_in=recipe_in)
    return recipe
