# Exercise 1
name=input("Type your name: ")
def greet(name):
    print(f"Hello,{name}!")
greet(name)
# Exercise 2
bed_length=int(input("Bed's length: "))
def goldilocks(bed_length):
    if bed_length<140:
        print("Too small!")
    elif bed_length>150:
        print("Too large!")
    else:
        print("Just right!")
goldilocks(bed_length)
# Exercise 3
numbers=list(map(int, input('Type number (separeted by spaces): ').split()))
def square_list(numbers):
    return[num**2 for num in numbers]
print(square_list(numbers))
# Exercise 4
max_value=int(input('Type max value: '))
def fibonacci_stop(max_value):
    fibonacci_sequence = [1, 1]
    while True:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_value > max_value:
            break
        fibonacci_sequence.append(next_value)
    return fibonacci_sequence
print(fibonacci_stop(max_value))
# Exercise 5
pitch_angles=list(map(int, input('Type pitch angles: ')))
status_signals=list(map(int, input('Type status signals: ')))
def clean_pitch(pitch_angles, status_signals):
    cleaned_angles = []
    
    for angle, status in zip(pitch_angles, status_signals):
        if (angle < 0 or angle > 90) and status > 0:
            cleaned_angles.append(-999)
        else:
            cleaned_angles.append(angle)
    
    return cleaned_angles
print(clean_pitch(pitch_angles, status_signals))
