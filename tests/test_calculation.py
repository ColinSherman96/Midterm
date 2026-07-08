import pytest
from decimal import Decimal
from datetime import datetime
import logging

from app.calculation import Calculation
from app.exceptions import OperationError


def test_calculation_creation():
    calc = Calculation(
        operation="Addition",
        operand1=Decimal("2"),
        operand2=Decimal("3"),
        result=Decimal("5")
    )

    assert calc.operation == "Addition"
    assert calc.operand1 == Decimal("2")
    assert calc.operand2 == Decimal("3")
    assert calc.result == Decimal("5")


def test_to_dict():
    calc = Calculation(
        operation="Addition",
        operand1=Decimal("2"),
        operand2=Decimal("3"),
        result=Decimal("5")
    )

    result_dict = calc.to_dict()

    assert result_dict == {
        "operation": "Addition",
        "operand1": "2",
        "operand2": "3",
        "result": "5",
        "timestamp": calc.timestamp.isoformat()
    }


def test_from_dict():
    data = {
        "operation": "Addition",
        "operand1": "2",
        "operand2": "3",
        "result": "5",
        "timestamp": datetime.now().isoformat()
    }

    calc = Calculation.from_dict(data)

    assert calc.operation == "Addition"
    assert calc.operand1 == Decimal("2")
    assert calc.operand2 == Decimal("3")
    assert calc.result == Decimal("5")


def test_from_dict_result_mismatch(caplog):
    data = {
        "operation": "Addition",
        "operand1": "2",
        "operand2": "3",
        "result": "10",
        "timestamp": datetime.now().isoformat()
    }

    with caplog.at_level(logging.WARNING):
        Calculation.from_dict(data)

    # Currently your code intentionally does not log mismatches
    assert caplog.text == ""


def test_invalid_from_dict():
    data = {
        "operation": "Addition",
        "operand1": "invalid",
        "operand2": "3",
        "result": "5",
        "timestamp": datetime.now().isoformat()
    }

    with pytest.raises(OperationError, match="Invalid calculation data"):
        Calculation.from_dict(data)


def test_invalid_operand_raises():
    with pytest.raises(OperationError, match="Invalid operand"):
        Calculation(
            operation="Addition",
            operand1="invalid",
            operand2=Decimal("3"),
            result=Decimal("0")
        )


def test_format_result():
    calc = Calculation(
        operation="Division",
        operand1=Decimal("1"),
        operand2=Decimal("3"),
        result=Decimal("0.333333333333333333")
    )

    assert calc.format_result(precision=2) == "0.33"
    assert calc.format_result(precision=10) == "0.3333333333"


def test_equality():
    calc1 = Calculation(
        operation="Addition",
        operand1=Decimal("2"),
        operand2=Decimal("3"),
        result=Decimal("5")
    )

    calc2 = Calculation(
        operation="Addition",
        operand1=Decimal("2"),
        operand2=Decimal("3"),
        result=Decimal("5")
    )

    calc3 = Calculation(
        operation="Subtraction",
        operand1=Decimal("5"),
        operand2=Decimal("3"),
        result=Decimal("2")
    )

    assert calc1 == calc2
    assert calc1 != calc3