from grader_contracts.python_basics import *
from python_basics import *

if __name__ == '__main__':
    print("Задача 1.")
    print("Hello World:", count_vowels(TextInput('Hello World')))  
    print("Programming:", count_vowels(TextInput('Programming')))  
    print("Rhythm:", count_vowels(TextInput('Rhythm')))            

    print("\nЗадача 2.")
    print("'a':", has_unique_characters(TextInput('a')))
    print("'':", has_unique_characters(TextInput('')))
    print("'abcde':", has_unique_characters(TextInput('abcde')))
    print("'hello':", has_unique_characters(TextInput('hello')))
    print("'a b c':", has_unique_characters(TextInput('a b c')))

    print("\nЗадача 3.")
    print("213123:", count_one_bits(PositiveIntegerInput(213123)))
    print("7:", count_one_bits(PositiveIntegerInput(7)))            
    print("8:", count_one_bits(PositiveIntegerInput(8)))            

    print("\nЗадача 4.")
    print("39:", multiplicative_persistence(PositiveIntegerInput(39)))
    print("999:", multiplicative_persistence(PositiveIntegerInput(999)))
    print("4:", multiplicative_persistence(PositiveIntegerInput(4)))
    print("123:", multiplicative_persistence(PositiveIntegerInput(123)))

    print("\nЗадача 5.")
    print("Идеальное совпадение:", mse(VectorPairInput(predicted=[1, 2, 3], expected=[1, 2, 3])))
    print("Разные векторы:", mse(VectorPairInput(predicted=[1, 2], expected=[3, 2])))  

    print("\nЗадача 6.")
    print("86240:", prime_factorization(PositiveIntegerInput(86240)))
    print("12:", prime_factorization(PositiveIntegerInput(12)))     
    print("37:", prime_factorization(PositiveIntegerInput(37)))     

    print("\nЗадача 7.")
    print("5:", pyramid(PositiveIntegerInput(5)))                   
    print("14:", pyramid(PositiveIntegerInput(14)))                 
    print("10:", pyramid(PositiveIntegerInput(10)))                 

    print("\nЗадача 8.")
    print("1234006:", is_balanced_number(PositiveIntegerInput(1234006)))  
    print("123456:", is_balanced_number(PositiveIntegerInput(123456)))    
    print("7:", is_balanced_number(PositiveIntegerInput(7)))              
    print("11:", is_balanced_number(PositiveIntegerInput(11)))            