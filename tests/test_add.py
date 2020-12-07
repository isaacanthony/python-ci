"""Tests for src/add.py"""
import unittest
from src.add import add


def test_add():
    """Test add()"""
    case = unittest.TestCase()
    case.assertEqual(add(2, 2), 4)
