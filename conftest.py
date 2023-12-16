import pytest

def pytest_addoption(parser):
    parser.addoption("--email", action="store", default="jdoe@example.com", help="Specify the email for testing.")