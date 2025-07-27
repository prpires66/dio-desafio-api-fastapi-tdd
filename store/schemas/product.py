from typing import Annotated
from pydantic import Field
from store.schemas.base import BaseSchemaMixin


class ProductIn(BaseSchemaMixin):
    name: Annotated[str, Field(description="Name of the product")]
    quantity: Annotated[int, Field(description="Quantity of the product")]
    price: Annotated[float, Field(description="Price of the product")]
    status: Annotated[bool, Field(description="Status of the product")]
