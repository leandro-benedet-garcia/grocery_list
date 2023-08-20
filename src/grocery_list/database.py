from typing import Annotated

import sqlalchemy as sql
from sqlalchemy import orm

engine = sql.create_engine("sqlite:///products.db")

Mapped = orm.Mapped

int_pk = Annotated[
    int,
    orm.mapped_column(
        unique=True, init=False, autoincrement=True, primary_key=True
    ),
]
reg = orm.registry()


@reg.mapped_as_dataclass(unsafe_hash=True)
class Product:
    __tablename__ = "product"

    pk_id: Mapped[int_pk]
    name: Mapped[str]
    brand: Mapped[str]
    cost: Mapped[float]
    bulk_amount: Mapped[int]
    bulk_cost: Mapped[float]


with orm.Session(engine) as session:
    Product.__table__.create(engine)
    session.add(Product(None, "Coke", "Coca-Cola", 10.5, 3, 8))
    session.commit()
