# filepath: /x:/buildStuff/calculator-app/create_shortcut.py
import os
from pyshortcuts import make_shortcut

# Path to your Python script
script_path = os.path.join(os.path.dirname(__file__), 'src', 'gui.py')

# Create a shortcut on the desktop
make_shortcut(script_path, name='CalculatorApp', description='My first Calculator', icon=None)