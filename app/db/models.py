from typing import Generator
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from .session import Base, engine, SessionLocal

recipe_ingredient = Table(
    "recipe_ingredient",
    Base.metadata,
    Column(
        "recipe_id",
        Integer,
        ForeignKey("recipe.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "ingredient_id",
        Integer,
        ForeignKey("ingredient.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


class Ingredient(Base):
    __tablename__ = "ingredient"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=True)

    recipes = relationship(
        "Recipe",
        secondary=recipe_ingredient,
        back_populates="ingredients",
        passive_deletes=True,
    )


class Recipe(Base):
    __tablename__ = "recipe"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=True)
    steps = Column(Text, nullable=True)

    ingredients = relationship(
        "Ingredient",
        secondary=recipe_ingredient,
        back_populates="recipes",
        passive_deletes=True,
    )


class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(
        Integer,
        ForeignKey("recipe.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    rating = Column(Integer, nullable=True)

    recipe = relationship("Recipe", back_populates="reviews")


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")
