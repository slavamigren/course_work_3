from src.main import show_last_five
from datetime import datetime
import pytest

def test_show_last_five():
    assert show_last_five('..\data\operations.zip') == None