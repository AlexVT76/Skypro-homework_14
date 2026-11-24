class Product:
    """Класс продукта магазина."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self._price = new_price

    @classmethod
    def new_product(cls, data: dict, products: list | None = None) -> "Product":

        if products is not None:
            for product in products:
                if product.name == data["name"]:
                    product.quantity += data["quantity"]
                    if data["price"] > product.price:
                        product.price = data["price"]
                    return product
        return cls(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=data["quantity"],
        )

    def __add__(self, other: "Product") -> float:
        if not isinstance(other, Product):
            raise TypeError("Складывать можно только объекты класса Product")
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self) -> str:
        return (
            f"Product(name={self.name!r}, description={self.description!r}, "
            f"price={self._price}, quantity={self.quantity})"
        )
