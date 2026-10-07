"""
Simple Python Application for DevOps CI/CD Demo
"""

def greet(name: str = "World") -> str:
    return f"Hello, {name}! Welcome to Jenkins CI/CD Integration."

def add_numbers(a: int, b: int) -> int:
    return a + b

def is_service_healthy() -> bool:
    return True

if __name__ == "__main__":
    print("=" * 50)
    print(greet("DevOps Engineer"))
    print(f"Sample Calculation (5 + 7): {add_numbers(5, 7)}")
    print(f"Health Status: {'OK' if is_service_healthy() else 'FAIL'}")
    print("=" * 50)
    print("Application executed successfully during Jenkins build!")
