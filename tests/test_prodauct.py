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
