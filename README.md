                    BIG O COMPLEXITY CALCULATOR
================================================================================

A Python tool that calculates the largest input size n an algorithm can handle,
given a maximum operation budget x.

Supports a command-line interface and a Tkinter GUI.


--------------------------------------------------------------------------------
SUPPORTED COMPLEXITY CLASSES
--------------------------------------------------------------------------------

  Logarithmic       O(log n)
  Square Root       O(√n)
  Linear            O(n)
  Log Linear        O(n log n)
  Quadratic         O(n²)
  Cubic             O(n³)
  Exponential       O(2ⁿ)
  Factorial         O(n!)


--------------------------------------------------------------------------------
REQUIREMENTS
--------------------------------------------------------------------------------

  - Python 3.x
  - simpleeval (https://pypi.org/project/simpleeval/)

Install dependencies:
  pip install -r requirements.txt


--------------------------------------------------------------------------------
USAGE
--------------------------------------------------------------------------------

GUI:
  python Largest_O_n__calculator_GUI.py
  Enter a value for x, then tap a complexity button to see the largest n.

CLI:
  python main.py
  - Option i : runs all complexities at once.
  - Option j : lets you batch multiple inputs.


--------------------------------------------------------------------------------
EXAMPLE (x = 1,000,000)
--------------------------------------------------------------------------------

  Complexity       Largest n
  ------------------------------------
  O(log n)        ~2^1000000
  O(√n)           ~1.000e+12
  O(n)            1,000,000
  O(n log n)      ~62,746
  O(n²)           ~1,000
  O(n³)           ~100
  O(2ⁿ)           19
  O(n!)           12


--------------------------------------------------------------------------------
FILES
--------------------------------------------------------------------------------

  main.py                          - Core logic + CLI
  Largest_O_n__calculator_GUI.py   - Tkinter GUI
  requirements.txt                 - Dependencies
