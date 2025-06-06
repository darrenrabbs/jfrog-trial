import allure
import pytest
from main import main


@allure.feature("Greeting")
def test_main_returns_hello_world():
    assert main() == "Hello World!"