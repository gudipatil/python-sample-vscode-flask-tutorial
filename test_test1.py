import pytest

even = [(4, 5), (4, 4)]
odd = [99, 89]
skip_test = True


@pytest.fixture(scope='class')
def connection(request):
    print('set up')
    request.cls.num1 = 10
    print(request.cls.num1)
    yield
    print('tear down')
    request.cls.num1 = 0
    print(request.cls.num1)
    pytest.exit('test', 0)
    
 def div(a,b):
    return a/0


@pytest.mark.usefixtures('connection')
class TestRecon:
    @pytest.mark.parametrize('num', even, ids=['E35', 'E45'])
    @pytest.mark.skipif(not skip_test, reason='skipping test')
    def test_row_count(self, num):
        assert num[0] == num[1]
        assert self.num1 > 9

    @pytest.mark.parametrize('num', odd)
    @pytest.mark.skipif(skip_test, reason='skip')
    def test_is_odd(self, num):
        assert num % 2 == 1
        assert self.num1 == 8
    
    def test_mul(3,4):
        assert div(3, 4) > 0


