from crud.base import CRUDBase
from models.recipe import Recipe
from schemas.recipe import RecipeCreate, RecipeUpdate 

class CrudRecipe(CRUDBase[Recipe, RecipeCreate, RecipeUpdate]):
    ...

recipe = CrudRecipe(Recipe)