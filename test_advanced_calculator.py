"""
고급 계산기 모듈 테스트

이 모듈은 advanced_calculator.py의 모든 함수에 대한 포괄적인 테스트를 제공합니다.
"""

import pytest
import math
from advanced_calculator import (
    divide_numbers,
    power_numbers,
    square_root,
    factorial,
    calculate_average,
    find_maximum,
    find_minimum,
    is_prime
)


class TestDivideNumbers:
    """divide_numbers 함수 테스트"""
    
    def test_divide_positive_numbers(self):
        """양수 나누기 테스트"""
        assert divide_numbers(10, 2) == 5.0
        assert divide_numbers(15, 3) == 5.0
        assert divide_numbers(7, 2) == 3.5
    
    def test_divide_negative_numbers(self):
        """음수 나누기 테스트"""
        assert divide_numbers(-10, 2) == -5.0
        assert divide_numbers(10, -2) == -5.0
        assert divide_numbers(-10, -2) == 5.0
    
    def test_divide_by_zero(self):
        """0으로 나누기 예외 테스트"""
        with pytest.raises(ValueError, match="0으로 나눌 수 없습니다"):
            divide_numbers(10, 0)
    
    def test_divide_zero_by_number(self):
        """0을 숫자로 나누기 테스트"""
        assert divide_numbers(0, 5) == 0.0


class TestPowerNumbers:
    """power_numbers 함수 테스트"""
    
    def test_power_positive_numbers(self):
        """양수 거듭제곱 테스트"""
        assert power_numbers(2, 3) == 8
        assert power_numbers(5, 2) == 25
        assert power_numbers(3, 4) == 81
    
    def test_power_zero_exponent(self):
        """지수가 0인 경우 테스트"""
        assert power_numbers(5, 0) == 1
        assert power_numbers(100, 0) == 1
    
    def test_power_negative_exponent(self):
        """음수 지수 테스트"""
        assert power_numbers(2, -2) == 0.25
        assert power_numbers(4, -1) == 0.25
    
    def test_power_fractional_exponent(self):
        """소수 지수 테스트"""
        assert power_numbers(9, 0.5) == 3.0
        assert power_numbers(8, 1/3) == pytest.approx(2.0, rel=1e-10)


class TestSquareRoot:
    """square_root 함수 테스트"""
    
    def test_square_root_positive_numbers(self):
        """양수 제곱근 테스트"""
        assert square_root(4) == 2.0
        assert square_root(9) == 3.0
        assert square_root(16) == 4.0
        assert square_root(2) == pytest.approx(1.414213562373095)
    
    def test_square_root_zero(self):
        """0의 제곱근 테스트"""
        assert square_root(0) == 0.0
    
    def test_square_root_negative_number(self):
        """음수 제곱근 예외 테스트"""
        with pytest.raises(ValueError, match="음수의 제곱근은 계산할 수 없습니다"):
            square_root(-1)


class TestFactorial:
    """factorial 함수 테스트"""
    
    def test_factorial_positive_numbers(self):
        """양수 팩토리얼 테스트"""
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(5) == 120
        assert factorial(7) == 5040
    
    def test_factorial_negative_number(self):
        """음수 팩토리얼 예외 테스트"""
        with pytest.raises(ValueError, match="음이 아닌 정수만 입력 가능합니다"):
            factorial(-1)
    
    def test_factorial_non_integer(self):
        """정수가 아닌 값 팩토리얼 예외 테스트"""
        with pytest.raises(ValueError, match="음이 아닌 정수만 입력 가능합니다"):
            factorial(3.5)  # type: ignore


class TestCalculateAverage:
    """calculate_average 함수 테스트"""
    
    def test_average_positive_numbers(self):
        """양수 평균 테스트"""
        assert calculate_average([1, 2, 3, 4, 5]) == 3.0
        assert calculate_average([10, 20, 30]) == 20.0
    
    def test_average_mixed_numbers(self):
        """양수와 음수 혼합 평균 테스트"""
        assert calculate_average([-1, 0, 1]) == 0.0
        assert calculate_average([-5, 5, -10, 10]) == 0.0
    
    def test_average_single_number(self):
        """단일 숫자 평균 테스트"""
        assert calculate_average([42]) == 42.0
    
    def test_average_empty_list(self):
        """빈 리스트 평균 예외 테스트"""
        with pytest.raises(ValueError, match="빈 리스트는 평균을 계산할 수 없습니다"):
            calculate_average([])


class TestFindMaximum:
    """find_maximum 함수 테스트"""
    
    def test_maximum_positive_numbers(self):
        """양수 최댓값 테스트"""
        assert find_maximum([1, 5, 3, 9, 2]) == 9
        assert find_maximum([10, 20, 15]) == 20
    
    def test_maximum_negative_numbers(self):
        """음수 최댓값 테스트"""
        assert find_maximum([-1, -5, -3]) == -1
    
    def test_maximum_mixed_numbers(self):
        """양수와 음수 혼합 최댓값 테스트"""
        assert find_maximum([-5, 0, 3, -2]) == 3
    
    def test_maximum_single_number(self):
        """단일 숫자 최댓값 테스트"""
        assert find_maximum([42]) == 42
    
    def test_maximum_empty_list(self):
        """빈 리스트 최댓값 예외 테스트"""
        with pytest.raises(ValueError, match="빈 리스트에서는 최댓값을 찾을 수 없습니다"):
            find_maximum([])


class TestFindMinimum:
    """find_minimum 함수 테스트"""
    
    def test_minimum_positive_numbers(self):
        """양수 최솟값 테스트"""
        assert find_minimum([1, 5, 3, 9, 2]) == 1
        assert find_minimum([10, 20, 15]) == 10
    
    def test_minimum_negative_numbers(self):
        """음수 최솟값 테스트"""
        assert find_minimum([-1, -5, -3]) == -5
    
    def test_minimum_mixed_numbers(self):
        """양수와 음수 혼합 최솟값 테스트"""
        assert find_minimum([-5, 0, 3, -2]) == -5
    
    def test_minimum_single_number(self):
        """단일 숫자 최솟값 테스트"""
        assert find_minimum([42]) == 42
    
    def test_minimum_empty_list(self):
        """빈 리스트 최솟값 예외 테스트"""
        with pytest.raises(ValueError, match="빈 리스트에서는 최솟값을 찾을 수 없습니다"):
            find_minimum([])


class TestIsPrime:
    """is_prime 함수 테스트"""
    
    def test_prime_numbers(self):
        """소수 테스트"""
        assert is_prime(2) is True
        assert is_prime(3) is True
        assert is_prime(5) is True
        assert is_prime(7) is True
        assert is_prime(11) is True
        assert is_prime(13) is True
        assert is_prime(17) is True
        assert is_prime(19) is True
        assert is_prime(23) is True
    
    def test_non_prime_numbers(self):
        """합성수 테스트"""
        assert is_prime(4) is False
        assert is_prime(6) is False
        assert is_prime(8) is False
        assert is_prime(9) is False
        assert is_prime(10) is False
        assert is_prime(12) is False
        assert is_prime(15) is False
        assert is_prime(16) is False
    
    def test_edge_cases(self):
        """경계값 테스트"""
        assert is_prime(0) is False
        assert is_prime(1) is False
        assert is_prime(-1) is False
        assert is_prime(-5) is False
    
    def test_large_prime(self):
        """큰 소수 테스트"""
        assert is_prime(97) is True
        assert is_prime(101) is True
    
    def test_large_non_prime(self):
        """큰 합성수 테스트"""
        assert is_prime(100) is False
        assert is_prime(99) is False


# 통합 테스트
class TestIntegration:
    """통합 테스트"""
    
    def test_calculator_workflow(self):
        """계산기 워크플로우 테스트"""
        # 기본 연산들을 조합한 복잡한 계산
        numbers = [2, 4, 6, 8, 10]
        
        # 평균 계산
        avg = calculate_average(numbers)
        assert avg == 6.0
        
        # 최댓값과 최솟값
        max_val = find_maximum(numbers)
        min_val = find_minimum(numbers)
        assert max_val == 10
        assert min_val == 2
        
        # 거듭제곱과 제곱근
        power_result = power_numbers(max_val, 2)  # 10^2 = 100
        sqrt_result = square_root(power_result)   # √100 = 10
        assert sqrt_result == 10.0
        
        # 나누기
        division_result = divide_numbers(power_result, min_val)  # 100 / 2 = 50
        assert division_result == 50.0 