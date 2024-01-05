from fastapi import APIRouter

from api.api_v1.endpoints import recipe, auth

api_router = APIRouter()
api_router.include_router(recipe.router, prefix="/recipe", tags=["recipe"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])