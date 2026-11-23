from typing import List, Optional
from src.product import Product


class Category:
    """Класс категории товаров."""

    total_categories: int = 0
    total_products: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:

        self.name: str = name
        self.description: str = description
        self.products: List[Product] = products if products is not None else []

        Category.total_categories += 1
        Category.total_products += len(self.products)
