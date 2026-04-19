""" Day 1: Basic python practice."""

def is_prime(n: int)-> bool:
    """return True if n is prime num else False """
    
    # handle the number less than 2
    if n < 2:
        return False
    #check from 2 
    i = 2
    #loop untill square root of n
    while i*i <= n:
        #starts checking if i divides by n
        if n % i == 0:
            return False
        #move to the next number
        i += 1
    #if no diviser found 
    return True
print (is_prime(4))


def reverse_string(s: str) -> str:
    """Reverse a string without using slicing [::-1]."""
    # initialize an empty string to store the reversed string
    reversed_str = ""
    # loop trough the original string in reverse order    
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
print (reverse_string("hello world"))

def count_vowels(s: str) -> int:
    """Count the number of vowels (a, e, i, o, u) in s."""
    # define a set of vowels for quick lookup
    vowels = set("aeiouAEIOU")
    # initialize a counter for the number of vowels
    count = 0
    # loop through each character in the string
    for char in s:
        # if the character is a vowel, increment the count
        if char in vowels:
            count += 1
    return count           
print (count_vowels("hello world"))

def find_largest(numbers: list[int]) -> int:
    """Return the largest number in the list without using max()."""
    # check if the list is empty
    if not numbers:
        raise ValueError ("The list cannot be empty.")
    # initialize the largest number to the first element of the list
    largest = numbers[0]
    # loop through the list to find the largest number
    for num in numbers:
        if num > largest:
            largest = num
    return largest
print (find_largest([3, 1, 4, 1, 5, 9]))

def fibonacci(n: int) -> list[int]:
    """Return the first n terms of the Fibonacci sequence."""
    # handle the case when n is less than or equal to 0
    if n <= 0:
        return []
    # initialize the first two terms of the Fibonacci sequence
    fib_sequence = [0, 1]
    # generate the Fibonacci sequence until we have n terms
    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    return fib_sequence
print (fibonacci(10))

if __name__ == "__main__":
    print("is_prime(7):", is_prime(7))
    print("is_prime(10):", is_prime(10))
    print("reverse_string('hello'):", reverse_string("hello"))
    print("count_vowels('programming'):", count_vowels("programming"))
    print("find_largest([3, 7, 2, 9, 5]):", find_largest([3, 7, 2, 9, 5]))
    print("fibonacci(10):", fibonacci(10))