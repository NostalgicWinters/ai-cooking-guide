import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "..", "cooking_helper"))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
    os.chdir(PROJECT_ROOT)

from app.db.session import SessionLocal
from app.db.models import Recipe, Ingredient, Review, recipe_ingredient


def reset_database():
    confirm = input(
        "⚠️ This will delete ALL recipes, ingredients, and reviews. Are you sure? (y/N): "
    )
    if confirm.lower() != "y":
        print("Aborted.")
        return

    print("🔄 Deleting data...")

    session = SessionLocal()
    try:
        # Delete association table entries first
        session.execute(recipe_ingredient.delete())

        # Then delete dependent tables
        session.query(Review).delete()
        session.query(Recipe).delete()
        session.query(Ingredient).delete()

        session.commit()
        print("✅ Database reset complete!")
    except Exception as e:
        session.rollback()
        print(f"❌ Error: {e}")
    finally:
        session.close()


# TODO: Add the entry-point guard that calls reset_database() when this script is run directly
if __name__ == "__main__":
    reset_database(confirm=True)
