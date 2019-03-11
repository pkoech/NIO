Programming Quiz
----------------

We’re assuming familiarity with GitHub/BitBucket and Markdown, so we’ll use backticks (`...`) to describe inline code.

We expect this quiz to take about one to two hours.


1. How is `**` used as a unary operator in Python? In other words, when you see someone make a call to a function, `some_func(**kwargs)`, what is generally happening?


2. What does the line `#!/bin/sh` do at the beginning of a file?


3. Assume you have a list `x = ["table", "chair", "cup", "fork"]`. Write a function to write the contents of this list to a file, one item per line.


4. Write another function to read the file from the previous question, and return the same list of items. (Hint: What about non-printing characters?)


5. Write a function to calculate the factorial of number.


6. Write a function to generate the n-th element of the sequence 2, 1, 3, 4, 7, 11, 18,...


7. Write a function to determine if a number is a prime.


8. Write a class with a method that determines if a word is a palindrome.


9. Write a function to sum the bits of a number. For example `sum_bits(2) == 1`, `sum_bits(3) == 2`.


10. What is the difference between a logical/boolean OR operation, and a bitwise OR operation? In other words, what is happening in this snippet from a Python interactive session:

>>> a = 0b10
>>> b = 0b11
>>>
>>> a or b
2
>>> a | b
3


11. What is a bit mask? If you had `data = 0b01000010`, how would you toggle the seventh bit from 1 to 0?


12. What are the differences between TCP and UDP? (List one or two sentences.)


13. Pick the invalid IP address(es): a) 127.0.0.1,  b) 0.0.0.0,  c) 127.256.365.0


14. How many tests would you need in order to test an arbitrary state machine? (Is there an upper bound?)


15. Examine the following Python code, add comments, and offer suggestions to make this more readable and robust. Context: an Armstrong number is one that can be written as a sum of cubes of its digits. For example, 153 is an Armstrong number is equal to 1^3 + 5^3 + 3^3 = 1 + 125 + 27. 

def armstrong(n):
    res = 0
    orig = n
    while n != 0:
        remainder = n % 10
        res += remainder**3
        n //= 10
    if orig == res:
        return True
    return False


