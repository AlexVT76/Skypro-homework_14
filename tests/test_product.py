import pytest

from src.product import Product


def test_product_initialization(sample_product):
    assert sample_product.name == "Чайник"
    assert sample_product.description == "Электрический чайник"
    assert sample_product.price == 2999.99
    assert sample_product.quantity == 10


def test_product_different_values():
    product = Product(name="Тостер", description="Компактный тостер", price=1999.00, quantity=8)
    assert product.name == "Тостер"
    assert product.price == 1999.00
    assert product.quantity == 8


def test_price_getter():
    p = Product("Телефон", "Смартфон", 50000.0, 5)
    assert p.price == 50000.0


def test_price_setter_positive():
    p = Product("Телефон", "Смартфон", 50000.0, 5)
    p.price = 60000.0
    assert p.price == 60000.0


def test_price_setter_zero():
    p = Product("Телефон", "Смартфон", 50000.0, 5)
    p.price = 0
    assert p.price == 50000.0  # цена не изменилась


def test_price_setter_negative():
    p = Product("Телефон", "Смартфон", 50000.0, 5)
    p.price = -100.0
    assert p.price == 50000.0  # цена не изменилась


def test_price_setter_message(capsys):
    p = Product("Телефон", "Смартфон", 50000.0, 5)
    p.price = -100.0
    captured = capsys.readouterr()
    assert captured.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_new_product_from_dict():
    data = {"name": "Телефон", "description": "Смартфон", "price": 50000.0, "quantity": 5}
    p = Product.new_product(data)
    assert isinstance(p, Product)
    assert p.name == "Телефон"
    assert p.description == "Смартфон"
    assert p.price == 50000.0
    assert p.quantity == 5


def test_new_product_no_duplicate():
    existing = [Product("Телефон", "Смартфон", 50000.0, 5)]
    data = {"name": "Ноутбук", "description": "Игровой", "price": 80000.0, "quantity": 2}
    p = Product.new_product(data, existing)
    assert isinstance(p, Product)
    assert p.name == "Ноутбук"
    assert len(existing) == 1


def test_new_product_duplicate_merges_quantity():
    existing = [Product("Телефон", "Смартфон", 50000.0, 5)]
    data = {"name": "Телефон", "description": "Смартфон", "price": 55000.0, "quantity": 3}
    p = Product.new_product(data, existing)
    assert p is existing[0]
    assert p.quantity == 8
    assert p.price == 55000.0


def test_new_product_duplicate_keeps_higher_price():
    existing = [Product("Телефон", "Смартфон", 60000.0, 5)]
    data = {"name": "Телефon", "description": "Смартфон", "price": 55000.0, "quantity": 3}
    data["name"] = "Телефон"
    p = Product.new_product(data, existing)
    assert p.quantity == 8
    assert p.price == 60000.0
