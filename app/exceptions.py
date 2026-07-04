########################
# Creation of an exception file for error handling  #
########################

class CalculatorError(Exception):
    """
    This is the base class for all calculator-related exceptions.

    It serves as a template for more specific exceptions that may arise during calculator operations.
    """
    pass

class OperationError(CalculatorError):
    """
    This exception is raised when an error occurs during a mathematical operation.

    """
    pass


class ConfigurationError(CalculatorError):
    """
    This exception is raised when there is an error related to the calculator's configuration.

    """
    pass