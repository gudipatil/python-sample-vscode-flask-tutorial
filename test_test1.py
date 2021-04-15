import os
DB_NAME = os.getenv('DB_NAME')

def test_mock():
  assert True

  
def test_not_mock():
  assert True
  
def test_var():
  assert DB_NAME == 'MYSQLDB'
