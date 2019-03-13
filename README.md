# NIO


Programming Quiz
----------------

We’re assuming familiarity with GitHub/BitBucket and Markdown, so we’ll use backticks (`...`) to describe inline code.

We expect this quiz to take about one to two hours.


1. How is `**` used as a unary operator in Python? In other words, when you see someone make a call to a function, `some_func(**kwargs)`, what is generally happening?

```** unpacks the contents of a dictionary into the function call.

```

2. What does the line `#!/bin/sh` do at the beginning of a file?
```
This line directs the system to always run scripts with sh, rather than another shell. ‘/bin/sh’ is an executable representing the system shell
```
3. Assume you have a list `x = ["table", "chair", "cup", "fork"]`. Write a function to write the contents of this list to a file, one item per line.

```python

	def write_to_file():
	## create a file call f
		with open(‘nio.txt) as f:
            		for item in x:
		        	f.write(“s\n”% item)
```


4. Write another function to read the file from the previous question, and return the same list of items. (Hint: What about non-printing characters?)


5. Write a function to calculate the factorial of number.
``` python
	def factorial(n):
		if n < 1:
			return 1
		else:
			return n*factorial(n-1)
```


6. Write a function to generate the n-th element of the sequence 2, 1, 3, 4, 7, 11, 18,...

``` python
The above sequence can be expressed with this equation:

	1/2 (5 fibonacci(n) - LucasL(n))
	where 
	F_n  is the Fibonacci of n and L_n is the Lucas number of n 
	

		
	1/2 (5 fibonacci(n) - Lucas(n)) 
			
def generate_nth_sequence_number(n):
	#this is the function that generates the nth element of the sequence using fibonacci sequence and lucas sequence

	return 0.5 (5*fibonacci(n) -lucas(n)



def fibonacci(n):
	#base case
    if n == 0: 
    	return 0
    elif n == 1: 
    	return 1
    else: 
    	return fibonacci(n-1)+fibonacci(n-2)	

def lucas(n) : 
      
    # Base cases  
    if (n == 0) : 
        return 2
    if (n == 1) : 
        return 1
  
    # recurrence relation  
    return lucas(n - 1) + lucas(n - 2) 
    
```


7. Write a function to determine if a number is a prime.
	``` python
	def is_prime(n):
	    # 0 and 1 are not primes
	    if n < 2:
	        return False

	    # 2 is the only even prime number
	    if n == 2:
	        return True

	    # all other even numbers are not primes
	    if not n & 1:
	        return False

	    # range starts with 3 and only needs to go up
	    # the square root of n for all odd numbers
	    for x in range(3, int(n**0.5) + 1, 2):
	        if n % x == 0:
	            return False

	    return True
	```


8. Write a class with a method that determines if a word is a palindrome.
``` python
class Person:
  def __init__(self):
   

  def is_palindrome(self, string):
  	if string == self.reverse(string):
		return True
	return False
	
  def reverse(self,s):
  	return s[::-1]
  	
  ```



9. Write a function to sum the bits of a number. For example `sum_bits(2) == 1`, `sum_bits(3) == 2`.
	``` python 
	
	def  countSetBits(n): 
    		count = 0
   	 	while (n): 
        		count += n & 1
       			n >>= 1
    		return count 
  
	
	
	
	```

10. What is the difference between a logical/boolean OR operation, and a bitwise OR operation? In other words, what is happening in this snippet from a Python interactive session:
```
>>> a = 0b10
>>> b = 0b11
>>>
>>> a or b
2
>>> a | b
3


 First logical  OR operator will return 2 because logical operator will perform **short circuit** logic, meaning that if the outcome is known after only checking the first condition, the second condition is ignored. In this case the outcome is know after checking if a is True. If the first of the two evaluates to true, then the result will be true regardless of the second condition, and therefore the second condition will not be evaluated.
 
Bitwise OR operator evaluates each bit of two expressions i.e is performs 0b10 OR 0b11 and the results is 0b11 because it checks 1 OR 0 which gives 1 and the checks 1 OR 1 which gives 1 thus the result 0b11


````


11. What is a bit mask? If you had `data = 0b01000010`, how would you toggle the seventh bit from 1 to 0?

```  python
A mask defines which bits you want to keep, and which bits you want to clear. This is done by applying a mask value with bitwise operations - AND, OR and XOR. 

For this case to toggle the seventh bit from one to 0 we need to AND data with a value with a 0 on the sevent 0.

 def mask_data(data):
 	value  = 0b01000000
 data = data XOR value
 

```

12. What are the differences between TCP and UDP? (List one or two sentences.)

```
                                          
TCP is connection oriented  while UDP is the Datagram oriented protocol.  
TCP is reliable as it guarantees delivery of data to the destination router. The delivery of data to the destination cannot be guaranteed in UDP. 
Retransmission of lost packets is possible in TCP, but not in UDP while there is no retransmission of lost packets in User Datagram Protocol (UDP).

```


13. Pick the invalid IP address(es): a) 127.0.0.1,  b) 0.0.0.0,  c) 127.256.365.0
``	
b is invalid

```


14. How many tests would you need in order to test an arbitrary state machine? (Is there an upper bound?)


15. Examine the following Python code, add comments, and offer suggestions to make this more readable and robust. Context: an Armstrong number is one that can be written as a sum of cubes of its digits. For example, 153 is an Armstrong number is equal to 1^3 + 5^3 + 3^3 = 1 + 125 + 27.

``` python


# rename the function to is_armstrong(n)
# more descriptive of what it's doing
def armstrong(n):
	"""
	I would rename the variables as below so that
	they are more descriptive.
	I would also use the longer version of variable
	assignment since it is more readable that way.
	"""
    res = 0 # rename to sum_so_far 
    orig = n # rename to original
    while n != 0:
        remainder = n % 10 # last_digit = n % 10
        res += remainder**3 # sum_so_far = sum_so_far + last_digit**3
        n //= 10	# n = n // 10
    if orig == res: # original == sum_so_far
        return True
    return False
    
    ```
