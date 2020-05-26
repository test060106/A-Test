import pytest

@pytest.fixture()
def login():
    print("This is login method")

def test_case1(login):
    print('test case1 need login')
    pass

def test_case2():
    print("test case2 doesn't login")
    pass

def test_case3(login):
    print('test case3 need login')
    pass

if __name__ == '__main__':
    pytest.main()
