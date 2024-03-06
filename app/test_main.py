import datetime
from unittest.mock import patch
from app.main import outdated_products


def test_outdated_products() -> None:
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.today.return_value = datetime.datetime(2022, 2, 2)
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)

    assert outdated_products([
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]) == ["duck"]
