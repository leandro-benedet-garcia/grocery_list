import dataclasses

from typing import Callable


@dataclasses.dataclass
class Product:
    name: str
    brand: str
    cost: float
    bulk_amount: int
    bulk_cost: float

    def __hash__(self):
        return hash(f"{self.name}_{self.brand}")


def try_parse(label: str, data_type: Callable[[str], int | float]):
    while True:
        try:
            return data_type(input(label))
        except ValueError:
            print(f"The value needs to be {data_type}")


database: set[Product] = set()
product_list: list[list[int, Product]] = []


def add_product():
    name = input("Product name: ")
    brand = input("Brand: ")
    cost = try_parse("Product cost: ", float)
    amount = try_parse("Amount: ", int)
    bulk_amount = try_parse("Bulk amount: ", int)
    bulk_cost = try_parse("Bulk cost: ", float)

    product = Product(
        name,
        brand,
        cost,
        bulk_amount,
        bulk_cost,
    )

    database.add(product)
    product_list.append([amount, product])


def list_products():
    for amount, curr_prod in product_list:
        print(f"{curr_prod.brand} {curr_prod.name}", end=", ")
        if curr_prod.bulk_amount >= amount:
            print(f"Total cost: {curr_prod.bulk_cost * amount}")
        else:
            print(f"Total cost: {curr_prod.cost * amount}")


def remove_product():
    name = input("Product to Remove: ").lower()
    for amount, curr_product in product_list:
        if curr_product.name.lower() == name:
            product_list.remove([amount, curr_product])


while True:
    match input("Type Command: ").lower():
        case "a" | "add":
            add_product()
        case "l" | "list":
            list_products()
        case "r" | "remove":
            remove_product()
        case "q" | "quit":
            break
