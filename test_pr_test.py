# test_pr_test.py
# PR 테스트 파일에 대한 테스트 코드

import pytest
from test_pr import hello_world, add_numbers, multiply_numbers

def test_hello_world():
    """hello_world 함수 테스트"""
    result = hello_world()
    assert result == "Hello, World! This is a PR test."
    assert isinstance(result, str)

def test_add_numbers():
    """add_numbers 함수 테스트"""
    # 기본 테스트
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0
    assert add_numbers(10, -5) == 5
    
    # 큰 숫자 테스트
    assert add_numbers(1000, 2000) == 3000

def test_multiply_numbers():
    """multiply_numbers 함수 테스트"""
    # 기본 테스트
    assert multiply_numbers(4, 5) == 20
    assert multiply_numbers(0, 10) == 0
    assert multiply_numbers(1, 1) == 1
    assert multiply_numbers(-2, 3) == -6
    assert multiply_numbers(-2, -3) == 6
    
    # 큰 숫자 테스트
    assert multiply_numbers(100, 200) == 20000

def test_add_numbers_type_hints():
    """타입 힌트 확인을 위한 테스트"""
    result = add_numbers(1, 2)
    assert isinstance(result, int)

def test_multiply_numbers_type_hints():
    """타입 힌트 확인을 위한 테스트"""
    result = multiply_numbers(2, 3)
    assert isinstance(result, int)

if __name__ == "__main__":
    pytest.main([__file__]) 