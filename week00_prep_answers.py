def greet(name):
    print("Hello, "+name)

greet("Vaso")

def Goldilocks(height):
    min=140
    max=150
    if height>max:
        print("Too large!")
    elif height<min:
        print("Too small!")
    else:
        print("Just right. :)")

Goldilocks(135)
Goldilocks(145)
Goldilocks(165)

def square_list(numbers):
    for i in range(len(numbers)):
        numbers[i]=numbers[i]**2
    return numbers
print(square_list([1,2,3]))

def fibonacci_stop(number):
    fib_seq=[1]
    f1=0
    f2=1
    result=f1+f2
    
    while (result<=number):
        fib_seq.append(result)
        f1=f2
        f2=result
        result=f1+f2
    
    return fib_seq
print(fibonacci_stop(30))
