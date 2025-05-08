def greet(name):
    print(f"Hello, {name}!")

greet("world")

def goldilocks(length):
    if length > 150:
        print("Too large!")
    elif length < 140:
        print("Too small!")
    else:
        print("Just right. :)")

goldilocks(139)
goldilocks(140)
goldilocks(151)
goldilocks(150)

def square_list(x):
    y = x.copy()
    for i in range(len(y)):
        y[i] = y[i]**2
    return y

print(square_list([1, 2, 3]))

def fibonacci_stop(n):
    l = [1, 1]
    while l[-1] + l[-2] <= n:
        l.append(l[-1] + l[-2])
    return l

print(fibonacci_stop(30))

def clean_pitch(l1, l2):
    l3 = l1.copy()
    for i, num in enumerate(l2):
        if num == 1:
            l3[i] = -999
    return l3

x = [-1, 2, 6, 95]  # "raw" pitch angle at four time steps
status = [1, 0, 0, 0]  # status signal
print(clean_pitch(x, status))