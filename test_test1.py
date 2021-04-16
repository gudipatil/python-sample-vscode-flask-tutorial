import os
import pytest

DB_NAME = os.getenv('DB_NAME')

@pytest.mark.parameterize('num', [2,3,4,5])
def test_mock(num):
  assert num % 2 == 0

  
def test_not_mock():
  assert True
  
def test_var():
  assert DB_NAME == 'MYSQLDB'
