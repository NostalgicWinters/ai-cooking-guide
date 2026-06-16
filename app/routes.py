from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():
    return {"message": "Welcome to the Cooking API"}


@router.get("/recipes")
def get_recipes():
    return [
        {"id": 1, "name": "Pizza"},
        {"id": 2, "name": "Pasta"},
    ]


@router.get("/recipes/{recipe_id}")
def get_recipe(recipe_id: int):
    return {
        "id": recipe_id,
        "name": f"Recipe {recipe_id}"
    }


@router.post("/recipes")
def create_recipe(recipe: dict):
    return {
        "message": "Recipe created",
        "recipe": recipe
    }
