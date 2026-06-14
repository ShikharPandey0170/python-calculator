# Python Calculator

A simple calculator project showcasing both a command-line interface (CLI) and a graphical user interface (GUI) written in Python.

## Features

### CLI (`calculator_cli.py`)

* Addition, subtraction, multiplication, and division
* Power (`a ** b`) and square-root operations
* Input validation and error handling (division by zero, non-numeric input)
* Interactive text-based menu loop

### GUI (`pycalculator_gui.py`)

* Full-screen Tkinter interface with clickable buttons
* Supports the same arithmetic operations as the CLI, plus:

  * Square (`x²`) and square-root (`√`) shortcuts
  * Expression entry with support for `+`, `-`, `*`, `/`, and `^` (converted to `**`)
  * Safe evaluation (only digits, basic operators, parentheses, and spaces)
  * Clear (`C`) and Backspace (`⌫`) functionality
* Basic error handling (invalid characters, math errors)

## Technologies Used

* Python 3.x
* Tkinter (standard GUI toolkit for Python)

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/ShikharPandey0170/python-calculator.git
cd python-calculator
```

### 2. Ensure Python Is Installed

```bash
python --version
```

The output should show Python 3.x.

### 3. Run the Version You Want

#### CLI Version

```bash
python calculator_cli.py
```

#### GUI Version

```bash
python pycalculator_gui.py
```

> **Note:** The GUI requires Tkinter, which is included with most Python installations. On some Linux distributions, you may need to install it manually:

```bash
sudo apt-get install python3-tk
```

## Usage Example (CLI)

```text
         Calculator
1) Addition
2) Subtraction
3) Multiplication
4) Division
5) Power
6) Square Root
7) Exit

Enter your choice:- 1
Enter first number:- 4
Enter second number:- 6
Result:- 10.0

         Calculator
1) Addition
2) Subtraction
3) Multiplication
4) Division
5) Power
6) Square Root
7) Exit

Enter your choice:- 7
Thank you for using the Calculator!
```

## Usage Example (GUI)

Running:

```bash
python pycalculator_gui.py
```

opens a dark-themed window titled **PyCalculator** with:

* An entry field at the top for the current expression/result
* Buttons for digits `0–9`, decimal point, basic operators, parentheses, clear, backspace, square (`x²`), square-root (`√`), and exponent (`xʸ → ^`)
* Clicking `=` evaluates the expression (e.g., `2+3*4 → 14`) and displays the result
* Errors (e.g., invalid characters or division by zero) display `"Error"` in the output field

## Project Structure

```text
python-calculator/
│
├── calculator_cli.py      # Text-based interactive calculator
├── pycalculator_gui.py    # Tkinter GUI version
├── README.md              # Project documentation
└── .git/                  # Git repository metadata
```

## Future Improvements

* [ ] Add scientific functions (trigonometry, logarithms, etc.)
* [ ] Implement a calculation history (saved to a file)
* [ ] Add unit tests for core arithmetic functions
* [ ] Enhance the GUI with themes and keyboard shortcuts
* [ ] Package the project for installation via pip

## Author

**Shikhar**

GitHub: https://github.com/ShikharPandey0170
