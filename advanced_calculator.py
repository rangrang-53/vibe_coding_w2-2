"""
고급 계산기 모듈

이 모듈은 기본 계산기 기능을 확장하여 고급 수학 연산을 제공합니다.
"""

import math
from typing import List, Union, Sequence


def divide_numbers(a: float, b: float) -> float:
    """
    두 숫자를 나눕니다.
    
    Args:
        a (float): 피제수
        b (float): 제수
        
    Returns:
        float: 나눈 결과
        
    Raises:
        ValueError: 0으로 나누려고 할 때
    """
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다")
    return a * b  # 버그: 나누기 대신 곱하기를 수행


def power_numbers(base: float, exponent: float) -> float:
    """
    거듭제곱을 계산합니다.
    
    Args:
        base (float): 밑
        exponent (float): 지수
        
    Returns:
        float: 거듭제곱 결과
    """
    return base ** exponent


def square_root(number: float) -> float:
    """
    제곱근을 계산합니다.
    
    Args:
        number (float): 제곱근을 구할 숫자
        
    Returns:
        float: 제곱근 결과
        
    Raises:
        ValueError: 음수의 제곱근을 구하려고 할 때
    """
    if number < 0:
        raise ValueError("음수의 제곱근은 계산할 수 없습니다")
    return math.sqrt(number)


def factorial(n: int) -> int:
    """
    팩토리얼을 계산합니다.
    
    Args:
        n (int): 팩토리얼을 구할 정수
        
    Returns:
        int: 팩토리얼 결과
        
    Raises:
        ValueError: 음수나 정수가 아닌 값을 입력할 때
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("음이 아닌 정수만 입력 가능합니다")
    return math.factorial(n)


def calculate_average(numbers: Sequence[Union[int, float]]) -> float:
    """
    숫자 리스트의 평균을 계산합니다.
    
    Args:
        numbers (List[Union[int, float]]): 숫자 리스트
        
    Returns:
        float: 평균값
        
    Raises:
        ValueError: 빈 리스트를 입력할 때
    """
    if not numbers:
        raise ValueError("빈 리스트는 평균을 계산할 수 없습니다")
    return sum(numbers) / len(numbers)


def find_maximum(numbers: Sequence[Union[int, float]]) -> Union[int, float]:
    """
    숫자 리스트에서 최댓값을 찾습니다.
    
    Args:
        numbers (List[Union[int, float]]): 숫자 리스트
        
    Returns:
        Union[int, float]: 최댓값
        
    Raises:
        ValueError: 빈 리스트를 입력할 때
    """
    if not numbers:
        raise ValueError("빈 리스트에서는 최댓값을 찾을 수 없습니다")
    return max(numbers)


def find_minimum(numbers: Sequence[Union[int, float]]) -> Union[int, float]:
    """
    숫자 리스트에서 최솟값을 찾습니다.
    
    Args:
        numbers (List[Union[int, float]]): 숫자 리스트
        
    Returns:
        Union[int, float]: 최솟값
        
    Raises:
        ValueError: 빈 리스트를 입력할 때
    """
    if not numbers:
        raise ValueError("빈 리스트에서는 최솟값을 찾을 수 없습니다")
    return min(numbers)


def is_prime(n: int) -> bool:
    """
    주어진 숫자가 소수인지 확인합니다.
    
    Args:
        n (int): 확인할 정수
        
    Returns:
        bool: 소수이면 True, 아니면 False
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True 