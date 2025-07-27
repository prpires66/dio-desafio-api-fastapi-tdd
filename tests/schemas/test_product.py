from uuid import UUID

import pytest
from store.schemas.product import ProductIn
from tests.schemas.factories import product_data_factory


def test_schema_return_sucess():
    data = product_data_factory()
    product = ProductIn.model_validate(data)

    assert product.name == "Iphone 14 pro Max"
    assert product.quantity == 10
    assert product.price == 9999.99
    assert product.status is True
    assert isinstance(product.id, UUID)


def test_schema_return_raise():
    data = {
        "name": "Iphone 14 pro Max",
        "quantity": -10,  # Invalid quantity
        "price": 9999.99,
    }
    with pytest.raises(ValueError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0]["msg"] == "Field required"
