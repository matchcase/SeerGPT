import os
from importlib.resources import files
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from SeerGPT.cards import meaning_of_card

def test_meanings():
    dirpath = files("src.SeerGPT.assets")
    for filepath in dirpath.iterdir():
        filename = os.path.basename(filepath)
        if filename.endswith(".png") and "backcover.png" not in filename:
            assert meaning_of_card(filepath), f"Card {filename} does not have a meaning value."
    print("All cards have meaning values!")

if __name__ == '__main__':
    test_meanings()
    print("All tests succeeded!")
