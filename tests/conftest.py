import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def sample_product():
    """Базовый товар для тестов."""
    return Product(name="Чайник", description="Электрический чайник", price=2999.99, quantity=10)


@pytest.fixture
def sample_category_with_products():
    """Категория с двумя товарами."""
    p1 = Product("Чайник", "Электрический", 2999.99, 10)
    p2 = Product("Утюг", "Паровой", 3499.50, 5)
    return Category("Бытовая техника", "Техника для дома", [p1, p2])


@pytest.fixture
def empty_category():
    """Пустая категория (без товаров)."""
    return Category("Электроника", "Гаджеты и аксессуары")


@pytest.fixture(autouse=True)
def reset_category_counters():

    Category.total_categories = 0
    Category.total_products = 0
