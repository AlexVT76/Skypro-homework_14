import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_product():
    """Базовый товар для тестов."""
    return Product(name="Чайник", description="Электрический чайник", price=2999.99, quantity=10)


@pytest.fixture
def sample_category_with_products():
    cat = Category("Бытовая техника", "Техника для дома")
    cat.add_product(Product("Чайник", "Электрический", 2999.99, 10))
    cat.add_product(Product("Утюг", "Паровой", 3499.5, 5))
    return cat


@pytest.fixture
def empty_category():
    """Пустая категория (без товаров)."""
    return Category("Электроника", "Гаджеты и аксессуары")


@pytest.fixture(autouse=True)
def reset_category_counters():

    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture(autouse=True)
def reset_counters():

    Category.category_count = 0
    Category.product_count = 0
    yield
