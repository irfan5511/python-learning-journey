def is_prime(n: int) -> bool:
    """Return True if n is a prime number, else False.
    
    A prime number is a number greater than 1 that has no divisors
    other than 1 and itself. Examples: 2, 3, 5, 7, 11 are prime. 
    4, 6, 8, 9 are not.
    """
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def reverse_string(s: str) -> str:
    """Reverse a string without using slicing [::-1] or the reversed() function.
    
    Example: reverse_string("hello") should return "olleh"
    """
    reverse_s  = ""
    for char in s:
        reverse_s = char + reverse_s
    return reverse_s

        


def count_vowels(s: str) -> int:
    """Count the number of vowels (a, e, i, o, u) in the string s.
    
    Should count both lowercase and uppercase vowels.
    Example: count_vowels("Hello") should return 2.
    """
    # your code here
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
    


def find_largest(numbers: list[int]) -> int:
    """Return the largest number in the list without using the built-in max() function.
    
    Example: find_largest([3, 7, 2, 9, 5]) should return 9.
    Decide yourself what should happen if the list is empty.
    """
    max_num = numbers [0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def fibonacci(n: int) -> list[int]:
    """Return the first n terms of the Fibonacci sequence as a list.
    
    The Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
    Each number is the sum of the two before it.
    
    Example: fibonacci(5) should return [0, 1, 1, 2, 3]
    Example: fibonacci(1) should return [0]
    Example: fibonacci(0) should return []
    """
    if n == 0:
        return []
    if n == 1:
        return [0]
    fib= [0,1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib


    


if __name__ == "__main__":
    # Test your functions here
    print("is_prime(7):", is_prime(7))         # Should print: True
    print("is_prime(10):", is_prime(10))       # Should print: False
    print("is_prime(1):", is_prime(1))         # Should print: False
    print("reverse_string('hello'):", reverse_string("hello"))  # Should print: olleh
    print("count_vowels('Hello World'):", count_vowels("Hello World"))  # Should print: 3
    print("find_largest([3, 7, 2, 9, 5]):", find_largest([3, 7, 2, 9, 5]))  # Should print: 9
    print("fibonacci(0):", fibonacci(0))       # Should print: []
    print("fibonacci(1):", fibonacci(1))       # Should print: [0]
    print("fibonacci(5):", fibonacci(5))       # Should print: [0, 1, 1, 2, 3]
    print("fibonacci(10):", fibonacci(10))     # Should print: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]