from crud.base import BaseCrud
from models.recipe import Recipe
from schemas.recipe import RecipeCreate, RecipeUpdate 

class CrudRecipe(BaseCrud[Recipe, RecipeCreate, RecipeUpdate]):
    ...

recipe = CrudRecipe(Recipe)