# Exercise 1
def greet(name):
    return print("Hello, " + name + "!")
print("\n\nThe answer to exercise 1 is:")
greet("World")

# Exercise 2
def goldilock(x):
    if x < 140:
        return print("Too small!")
    elif x > 150:
        return print("Too large!")
    else:
        return print("Just right. :)")
    
print("\n\nThe answer to exercise 2 is:")

Bed1 = 130
print('If the bed is %d cm long' %Bed1)
goldilock(Bed1)

Bed2 = 140
print('If the bed is %d cm long' %Bed2)
goldilock(Bed2)

Bed3 = 151
print('If the bed is %d cm long' %Bed3)
goldilock(Bed3)

Bed4 = 150
print('If the bed is %d cm long' %Bed4)
goldilock(Bed4)

# Exercise 3
def square_list(list):
    for i in range(len(list)):
        list[i] = list[i] ** 2
    return list

list = [1,2,3]
print("\n\nThe answer to exercise 3 is:")
print("The list is %s" %list)
print("The squared list is %s" %square_list(list))

# Exercise 4
def fibonacci_stop(stop):
    fib = [0,1]
    fib_new = 0
    while fib_new < stop:
        fib_new = fib[-1] + fib[-2]
        fib.extend([fib_new])
    return fib[:-1]

print("\n\nThe answer to exercise 4 is:")
fib_stop = 30
results = fibonacci_stop(fib_stop)
print("The fibonacci sequence up to %d is\n %s" %(fib_stop, fibonacci_stop(fib_stop)))

# Exercise 5
def clean_pitch(x, status):
    x_clean = [None] * len(x)
    for i in range(len(x)):
        if (x[i] < 0) and status[i] == 1:
            x_clean[i] = -999
        elif (x[i] < 0) and status[i] == 0:
            x_clean[i] = x[i]
        elif (x[i] > 90) and status[i] == 1:
            x_clean[i] = -999
        elif (x[i] > 90) and status[i] == 0:
            x_clean[i] = x[i]
        else:
            x_clean[i] = x[i]
    return x_clean

    

x = [-1, 2, 6, 95, 55]
status = [1, 0, 0, 0, 1]
x_clean = clean_pitch(x, status)
print("\n\nThe answer to exercise 5 is:")
print("If the measured pitch is %s and the status is %s the following would be the output:" %(x, status))
print(x_clean)
