# 🧮 Python Calculator Application

## 📖 Project Overview

This project is a command-line calculator application developed for my Midterm Project, which involves developing an enhanced calculator command-line application.

The calculator supports multiple arithmetic operations, maintains calculation history, provides undo/redo functionality, automatically saves history, and includes logging and automated testing.

The application was designed using object-oriented programming principles and common software design patterns to create a modular and extensible structure.

---

# ✨ Features

## Arithmetic Operations

The calculator currently supports the following operations:

* Addition
* Subtraction
* Multiplication
* Division
* Power
* Root
* Modulus
* Integer Division
* Percentage
* Absolute Difference

Operations are implemented using a common abstract `Operation` class and created through `OperationFactory`, which allows new operations to be added easily.

---

## Calculation History

The application includes persistent calculation history:

* View previous calculations
* Save history to CSV
* Load previous history
* Clear history
* Automatic history saving

History entries store:

* Operation performed
* First operand
* Second operand
* Result
* Timestamp

---

## Undo / Redo Support

The calculator supports:

* Undoing previous calculations
* Redoing undone calculations

This functionality is implemented using the Memento Pattern.

---

## Logging

The application includes centralized logging:

* Calculation events are logged
* History auto-save events are recorded
* Errors can be tracked through application logs

Logs are managed through a dedicated logger class.

---

## Automated Testing

The project includes a comprehensive test suite using `pytest`.

Testing covers:

* Calculator functionality
* Individual operations
* Error handling
* History management
* REPL commands
* Serialization/deserialization
* Configuration validation

Current test coverage target:

```
90%+
```

Current test coverage is approximately 92%.
Coverage is enforced through GitHub Actions.

---

# 🏗️ Project Structure

```
project_root/
│
├── app/
│   ├── calculator.py              # Core calculator logic
│   ├── calculator_repl.py         # Command-line interface
│   ├── calculation.py             # Calculation data model
│   ├── operations.py              # Arithmetic operation classes
│   ├── calculator_config.py       # Application configuration
│   ├── calculator_memento.py      # Undo/redo state management
│   ├── history.py                 # History observers and persistence
│   ├── input_validators.py        # Input validation helpers
│   ├── logger.py                  # Logging configuration
│   └── exceptions.py              # Custom exceptions
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_calculator.py
│   ├── test_calculation.py
│   ├── test_operations.py
│   ├── test_exceptions.py
│   ├── test_validators.py
|
├── main.py                         # Application entry point
├── requirements.txt                # Python dependencies
├── pytest.ini                      # Pytest configuration
├── .env                            # Environment configuration
└── .github/
    └── workflows/
        └── python-app.yml          # Continuous integration testing
```

---

# ⚙️ Installation

## Requirements

* Python 3.10+
* pip

---

## Clone Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

---

## Create Virtual Environment (Recommended)

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Running the Application

Start the calculator:

```bash
python main.py
```

The calculator will start in interactive mode:

```
Calculator started. Type 'help' for commands.
```

---

# 📋 Available Commands

| Command      | Description                 |
| ------------ | --------------------------- |
| `add`        | Addition                    |
| `subtract`   | Subtraction                 |
| `multiply`   | Multiplication              |
| `divide`     | Division                    |
| `power`      | Exponentiation              |
| `root`       | Root calculation            |
| `modulus`    | Remainder calculation       |
| `int_divide` | Integer division            |
| `percent`    | Percentage calculation      |
| `abs_diff`   | Absolute difference         |
| `history`    | Display calculation history |
| `clear`      | Clear history               |
| `undo`       | Undo previous calculation   |
| `redo`       | Redo previous calculation   |
| `save`       | Save history                |
| `load`       | Load history                |
| `exit`       | Exit application            |

---

# 🧪 Running Tests

Run the complete test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=app --cov-report=term-missing
```

Generate an HTML coverage report:

```bash
pytest --cov=app --cov-report=html
```

---

# 🔄 Continuous Integration

The project uses GitHub Actions to automatically:

* Install dependencies
* Run the test suite
* Verify minimum code coverage requirements

The workflow is located at:

```
.github/workflows/python-app.yml
```

---

# 🧩 Design Patterns Used

## Factory Pattern

`OperationFactory` dynamically creates operation objects.

Benefits:

* Reduces coupling
* Makes adding operations easier
* Centralizes object creation

---

## Strategy Pattern

Arithmetic operations are implemented as interchangeable strategies.

The calculator can switch between operations without modifying calculator logic.

---

## Observer Pattern

History observers monitor calculator events.

Implemented observers:

* LoggingObserver
* AutoSaveObserver

---

## Memento Pattern

Undo/redo functionality uses saved calculator states.

---

# 🛠️ Configuration

Application behavior can be configured through environment variables in `.env`.

Examples:

```env
CALCULATOR_AUTO_SAVE=true
CALCULATOR_PRECISION=10
CALCULATOR_MAX_HISTORY_SIZE=1000
```

---

# 👤 Author

Colin Sherman

Midterm Project Submission  
IS601 - NJIT  
Last Updated: July 8, 2026

---

# Demo Example

(venv) csherman@CSlaptop:~/Midterm$ python3 main.py
Calculator started. Type 'help' for commands.

Enter command: add

Enter numbers (or 'cancel' to abort):
First number: 5
Second number: 2

Result: 7

Enter command: help

Available commands:
  add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff - Perform calculations
  history - Show calculation history
  clear - Clear calculation history
  undo - Undo the last calculation
  redo - Redo the last undone calculation
  save - Save calculation history to file
  load - Load calculation history from file
  exit - Exit the calculator

Enter command: history

Calculation History:
1. Addition(5, 2) = 7.0000000000

Enter command: save
History saved successfully

Enter command: exit
History saved successfully.
Goodbye!

# 📌 Future Improvements

Potential enhancements:

* Additional mathematical operations
* Improved terminal formatting/colors
* GUI interface
* More extensive user input validation
* Additional export formats
