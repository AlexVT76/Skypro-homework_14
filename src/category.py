from typing import List, Optional

from src.product import Product


class Category:
    """Класс категории товаров."""

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:

        self.name: str = name
        self.description: str = description
        self.products: List[Product] = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.products)
