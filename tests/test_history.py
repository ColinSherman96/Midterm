import pytest
from unittest.mock import Mock, MagicMock, patch
from app.calculation import Calculation
from app.history import LoggingObserver, AutoSaveObserver
from app.calculator import Calculator
from app.calculator_config import CalculatorConfig

# Sample setup for mock calculation
calculation_mock = Mock(spec=Calculation)
calculation_mock.operation = "addition"
calculation_mock.operand1 = 5
calculation_mock.operand2 = 3
calculation_mock.result = 8

# Test cases for LoggingObserver

@patch('app.logger.Logger.get_logger')
def test_logging_observer_logs_calculation(mock_get_logger):
    mock_logger = Mock()
    mock_get_logger.return_value = mock_logger

    observer = LoggingObserver()
    observer.update(calculation_mock)

    mock_logger.info.assert_called_once_with(
        "Calculation performed: %s (%s, %s) = %s",
        "addition",
        5,
        3,
        8
    )

def test_logging_observer_no_calculation():
    observer = LoggingObserver()
    with pytest.raises(AttributeError):
        observer.update(None)  # Passing None should raise an exception as there's no calculation

# Test cases for AutoSaveObserver
