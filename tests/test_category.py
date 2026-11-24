import pytest

from src.category import Category, Product


def test_category_initialization_with_products(sample_category_with_products):
    cat = sample_category_with_products
    assert cat.name == "Бытовая техника"
    assert cat.description == "Техника для дома"

    assert cat.products.count("\n") == 2

    assert "Чайник" in cat.products
    assert "Утюг" in cat.products


def test_category_empty_initialization(empty_category):
    cat = empty_category
    assert cat.name == "Электроника"
    assert cat.products == ""


def test_total_products_count():
    p1 = Product("Чайник", "Электрический", 2999.99, 10)
    p2 = Product("Утюг", "Паровой", 3499.50, 5)
    p3 = Product("Тостер", "Компактный", 1999.00, 8)

    cat1 = Category("Бытовая техника", "Для дома", [p1, p2])
    cat2 = Category("Мелкая бытовая", "Компактные приборы", [p3])

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_total_categories_count_increments():
    Category("Категория 1", "Первая категория", [])
    Category("Категория 2", "Вторая категория", [])
    Category("Категория 3", "Третья категория", [])

    assert Category.category_count == 3
    assert Category.product_count == 0


def test_private_products_not_accessible():
    cat = Category("Фрукты", "Свежие фрукты")
    with pytest.raises(AttributeError):
        _ = cat.__products


def test_add_product():
    cat = Category("Фрукты", "Свежие фрукты")
    p = Product("Яблоко", "Зелёное", 10.0, 5)
    cat.add_product(p)
    assert "Яблоко, 10.0 руб. Остаток: 5 шт.\n" in cat.products


def test_add_product_returns_none():
    cat = Category("Фрукты", "Свежие фрукты")
    p = Product("Яблоко", "Зелёное", 10.0, 5)
    assert cat.add_product(p) is None


def test_add_product_increments_product_count():
    cat = Category("Фрукты", "Свежие фрукты")
    assert Category.product_count == 0
    cat.add_product(Product("Яблоко", "Зелёное", 10.0, 5))
    assert Category.product_count == 1
    cat.add_product(Product("Груша", "Жёлтая", 20.0, 3))
    assert Category.product_count == 2


def test_product_count_shared_between_categories():
    cat1 = Category("Фрукты", "Свежие фрукты")
    cat2 = Category("Овощи", "Свежие овощи")
    cat1.add_product(Product("Яблоко", "Зелёное", 10.0, 5))
    cat2.add_product(Product("Морковь", "Оранжевая", 15.0, 10))
    assert Category.product_count == 2


def test_add_product_with_list_in_init():
    products = [
        Product("Яблоко", "Зелёное", 10.0, 5),
        Product("Груша", "Жёлтая", 20.0, 3),
    ]
    cat = Category("Фрукты", "Свежие фрукты", products)
    assert Category.product_count == 2
    assert "Яблоко" in cat.products
    assert "Груша" in cat.products


def test_products_getter_single_product():
    cat = Category("Фрукты", "Свежие фрукты")
    cat.add_product(Product("Яблоко", "Зелёное", 10.0, 5))
    assert cat.products == "Яблоко, 10.0 руб. Остаток: 5 шт.\n"


def test_products_getter_multiple_products():
    cat = Category("Фрукты", "Свежие фрукты")
    cat.add_product(Product("Яблоко", "Зелёное", 10.0, 5))
    cat.add_product(Product("Груша", "Жёлтая", 20.0, 3))
    expected = "Яблоко, 10.0 руб. Остаток: 5 шт.\n" "Груша, 20.0 руб. Остаток: 3 шт.\n"
    assert cat.products == expected


def test_products_getter_empty_category():
    cat = Category("Фрукты", "Свежие фрукты")
    assert cat.products == ""


def test_products_getter_reflects_price_change():
    cat = Category("Фрукты", "Свежие фрукты")
    p = Product("Яблоко", "Зелёное", 10.0, 5)
    cat.add_product(p)
    p.price = 15.0
    assert "Яблоко, 15.0 руб. Остаток: 5 шт.\n" in cat.products


def test_products_getter_reflects_quantity_change():
    cat = Category("Фрукты", "Свежие фрукты")
    p = Product("Яблоко", "Зелёное", 10.0, 5)
    cat.add_product(p)
    Product.new_product({"name": "Яблоко", "description": "Зелёное", "price": 12.0, "quantity": 3}, cat.products_list)
    assert "Яблоко, 12.0 руб. Остаток: 8 шт.\n" in cat.products
