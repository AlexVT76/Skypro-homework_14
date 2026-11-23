from src.category import Category, Product


def test_category_initialization_with_products(sample_category_with_products):
    cat = sample_category_with_products
    assert cat.name == "Бытовая техника"
    assert cat.description == "Техника для дома"
    assert len(cat.products) == 2
    assert isinstance(cat.products[0], Product)
    assert isinstance(cat.products[1], Product)


def test_category_empty_initialization(empty_category):
    cat = empty_category
    assert cat.name == "Электроника"
    assert cat.products == []


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
