########################
# History Management    #
########################

from abc import ABC, abstractmethod
from app.logger import Logger
import logging
from typing import Any
from app.calculation import Calculation


class HistoryObserver(ABC):
    """
    Abstract base class for calculator observers.

    This class defines the interface for observers that monitor and react to
    new calculation events. Implementing classes must provide an update method
    to handle the received Calculation instance.
    """

    @abstractmethod
    def update(self, calculation: Calculation) -> None:
        """
        Handle new calculation event.

        Args:
            calculation (Calculation): The calculation that was performed.
        """
        pass  # pragma: no cover


class LoggingObserver(HistoryObserver):
    """
    Observer that logs calculations to a file.

    Implements the Observer pattern by listening for new calculations and logging
    their details to a log file.
    """
    def __init__(self):
        """
        Initialize the LoggingObserver.

        Sets up the logger for logging calculation details.
        """
        self.logger = Logger.get_logger()

    def update(self, calculation: Calculation) -> None:
        """
        Log calculation details.

        This method is called whenever a new calculation is performed. It records
        the operation, operands, and result in the log file.

        Args:
            calculation (Calculation): The calculation that was performed.
        """
        if calculation is None:
            raise AttributeError("Calculation cannot be None")
        self.logger.info(
            "Calculation performed: %s (%s, %s) = %s",
            calculation.operation,
            calculation.operand1,
            calculation.operand2,
            calculation.result
        )

class AutoSaveObserver(HistoryObserver):

    def __init__(self, calculator: Any):
        if not hasattr(calculator, 'config') or not hasattr(calculator, 'save_history'):
            raise TypeError("Calculator must have 'config' and 'save_history' attributes")
        self.calculator = calculator

    def update(self, calculation: Calculation) -> None:
        if calculation is None:
            raise AttributeError("Calculation cannot be None")

        if self.calculator.config.auto_save:
            self.calculator.save_history()
            Logger.get_logger().info("History auto-saved")