import sys

sys.path.append('./script')

import pytest
from stock_data import StockData

@pytest.mark.parametrize(
    'input, correct', [
        ('aapl', 'AAPL'),
        ('AAPL', 'AAPL'),
        ('Appl', 'AAPL'),
        ('mEta', 'META'),
        ('vOO', 'VOO'),
        ('spYd', 'SPY'),
        ('vY M', 'VYM')
    ]
)

def test_ticker(input, correct):
    test_instance = StockData(input)
    assert test_instance.get_ticker() == correct
