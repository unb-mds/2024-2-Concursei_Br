# test_requests.py
import sys
import requests_mock

print("sys.path:", sys.path)
print("requests_mock.__file__:", requests_mock.__file__)

def test_import():
    assert True