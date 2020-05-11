#Create a Generator Function that implements and yields the Fibonacci sequence
def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b


#Iterate over the fibonacci generator function
numbers = 50
for num in fibonacci(numbers):
    print(num)

#Use Generator Expressions to discover sum, min, and max of the square roots of a random list of numbers
import random
numbers = random.sample(range(1, 100), 20)
sumNumbers = sum(n**0.5 for n in numbers)
minNumbers = min(n**0.5 for n in numbers)
maxNumbers = max(n**0.5 for n in numbers)

#Use f-string to format sum, min, and max
print(f"sum={sumNumbers} min={minNumbers} max={maxNumbers}")
