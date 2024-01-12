import logging
from sqlalchemy.orm import Session

from db import base
from crud.crud_recipe import recipe
from crud.crud_user import user
from schemas.user import UserCreate
from schemas.recipe import RecipeCreate
from recipe_data import RECIPES

logger = logging.getLogger(__name__)

FIRST_SUPERUSER = "admin@easyrecipes.com"

def init_db(db: Session) -> None:
    if FIRST_SUPERUSER:
        user_tmp = user.get_by_email(db, email=FIRST_SUPERUSER)
        if not user_tmp:
            user_in = UserCreate(
                first_name="Initial",
                surname="Superuser",
                full_name="Initial Superuser",
                email=FIRST_SUPERUSER,
                is_superuser=True,
            )
            user_tmp = user.create(db, obj_in=user_in)
        else:
            logger.warning(
                "Skipping creating superuser. User with email "
                f"{FIRST_SUPERUSER} already exists. "
            )
        #
        if not user_tmp.recipes:
            for recipe_itr in RECIPES:
                recipe_in = RecipeCreate(
                    label=recipe_itr["label"],
                    source=recipe_itr["source"],
                    url=recipe_itr["url"],
                    submitter_id=user_tmp.id
                )
                recipe.create(db, obj_in=recipe_in)
    else:
        logger.warning(
            "Skipping creating superuser.  FIRST_SUPERUSER needs to be "
            "provided as an env variable. "
            "e.g.  FIRST_SUPERUSER=admin@api.coursemaker.io"
        )
    