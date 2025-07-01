import pytest
from llm_course.main import main

def test_main_callable():
    assert callable(main)
