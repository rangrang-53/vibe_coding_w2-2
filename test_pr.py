# PR 테스트용 파일
# 이 파일은 GitHub Actions 자동화 기능을 테스트하기 위해 생성되었습니다.

def hello_world():
    """
    간단한 인사 함수
    GitHub Actions의 자동 라벨링, 리뷰어 할당, 댓글 생성 등을 테스트합니다.
    """
    return "Hello, World! This is a PR test."

def add_numbers(a: int, b: int) -> int:
    """
    두 숫자를 더하는 함수
    
    Args:
        a (int): 첫 번째 숫자
        b (int): 두 번째 숫자
        
    Returns:
        int: 두 숫자의 합
    """
    return a + b

def multiply_numbers(a: int, b: int) -> int:
    """
    두 숫자를 곱하는 함수
    
    Args:
        a (int): 첫 번째 숫자
        b (int): 두 번째 숫자
        
    Returns:
        int: 두 숫자의 곱
    """
    return a * b

if __name__ == "__main__":
    print(hello_world())
    print(f"2 + 3 = {add_numbers(2, 3)}")
    print(f"4 * 5 = {multiply_numbers(4, 5)}") 