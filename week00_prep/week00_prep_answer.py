#%%
#1. write a simple function
def greet(name):
     print(f"Hello, {name}!")
greet('Arianna')


# %%
#2. If/else statement

def goldilocks(length):
    if 140 < length < 150:
        print("Just right")
    elif length < 140:
        print("Too small")
    else:
        print("Too large")

goldilocks(145)


# %%
#3. For loops
def square_list(numbers):
    return[x**2 for x in numbers]
numbers=[2,4,6]
squared_numbers=(square_list(numbers))
print(squared_numbers)

# %%
#4. While loops
def fibonacci_stop(max_value):
    fib_sequence = [1, 1]
    
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > max_value:
            break
        fib_sequence.append(next_fib)
    
    return fib_sequence
result = fibonacci_stop(20)
print(result)
    
# %%
#5. Logical operators
def clean_pitch(measurements, status):
    cleaned_angles = []
    
    for i in range(len(measurements)):
        if 0 <= measurements[i] <= 90:
            # Good pitch angle, no malfunction
            cleaned_angles.append(measurements[i])
        elif status[i] > 0:
            # Bad pitch angle with malfunction
            cleaned_angles.append(-999)
        else:
            # Non-malfunctioning angle outside the range (not expected by problem)
            cleaned_angles.append(-999)
    
    return cleaned_angles

measurements = [-1,2,6,95]
status= [1,0, 0, 0]
cleaned_angles = clean_pitch(measurements, status)
print(cleaned_angles)  


# %%
