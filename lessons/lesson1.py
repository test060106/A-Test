import pytest

class TestDemo():

    def test_one(self):
        print("开始执行test——one方法")
        x = 'this'
        assert 'h' in x

    def test_two(self):
        print("开始执行test——two方法")
        x = 'hello'
        assert 'e' in x

    def test_three(self):
        print("开始执行test——three方法")
        a = 'hello'
        b = 'hello word'
        assert a in b