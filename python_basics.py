"""Заготовки задач на базовый Python."""

from grader_contracts.python_basics import PositiveIntegerInput, TextInput, VectorPairInput


def count_vowels(data: TextInput) -> int:
    text = data.value.lower()
    count = 0
    str_vowels = 'aeiou'
    for char in text:
        if char in str_vowels:
            count+=1
    return count


def has_unique_characters(data: TextInput) -> bool:
    text = data.value.lower()
    text_char = set(text.replace(' ', ''))
    for char in text_char:
        if text.count(char) > 1:
            return False
    return True


def count_one_bits(data: PositiveIntegerInput) -> int:
    number = data.value
    return bin(number).count('1')


def multiplicative_persistence(data: PositiveIntegerInput) -> int:
    number = data.value
    cnt = 0
    while number >= 10:
        result = 1
        for digit in str(number):
            result *= int(digit)
        number = result
        cnt += 1
    return cnt


def mse(data: VectorPairInput) -> float:
    predicted, expected = data.predicted, data.expected
    n = len(predicted)
    if n == 0:
        return 0.0
    squared_diff_sum = sum((x - y) ** 2 for x, y in zip(predicted, expected))
    
    return squared_diff_sum / n


def prime_factorization(data: PositiveIntegerInput) -> str:
    number = data.value
    number = data.value
    factors = []
    d = 2
    while d * d <= number:
        count = 0
        while number % d == 0:
            count += 1
            number //= d
            
        if count > 0:
            if count == 1:
                factors.append(f"({d})")
            else:
                factors.append(f"({d}**{count})")
        
        if d == 2:
            d = 3
        else:
            d += 2
            
    if number > 1:
        factors.append(f"({number})")
        
    return "".join(factors)

def pyramid(data: PositiveIntegerInput) -> int | str:
    cube_count = data.value
    current_sum = 0
    k = 1
    while current_sum < cube_count:
        current_sum += k ** 2
        if current_sum == cube_count:
            return k
        k += 1
    return "It is impossible"


def is_balanced_number(data: PositiveIntegerInput) -> bool:
    number = data.value
    s = str(number)
    n = len(s)
    
    left_part = s[:(n - 1) // 2]
    right_part = s[n // 2 + 1:]
    
    sum_left = sum(int(digit) for digit in left_part)
    sum_right = sum(int(digit) for digit in right_part)
    
    return sum_left == sum_right
