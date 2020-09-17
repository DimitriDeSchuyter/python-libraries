# Content of test_sample.py

from src.depuydt import echo

def test_echo():
    echo.notice("Testing notice message")
    echo.warning("Testing warning message")
    echo.error("Testing error message")
    