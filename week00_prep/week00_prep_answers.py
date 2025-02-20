#Excercise 1

def greet(names):
    for name in names:
        print("Hello, " + name + "!")
          
greet(["Nicklas"])


#Excercise 2

def goldilocks(length):
    if length < 140:
        print("Too short!")
    elif length > 150:
        print("Too long!")
    else:
        print("Just right!")

goldilocks(130)
goldilocks(140)
goldilocks(160)

#Excercise 3

def square_list(numbers):
    return [number**2 for number in numbers]

print(square_list([1, 2, 3, 4, 5]))

#Excercise 4
def fibonacci_stop(value):
    fibonacci = [1, 1]
    while True:
        next_value = fibonacci[-1] + fibonacci[-2]
        if next_value >= value:
            break
        fibonacci.append(next_value)
    return fibonacci

print(fibonacci_stop(30))

#Excercise 5
def clean_pitch(pitch_angles, status_signals):
    cleaned_angles = []
    for angle, status in zip(pitch_angles, status_signals):
        if (angle < 0 or angle > 90) and status > 0:
            cleaned_angles.append(-999)
        else:
            cleaned_angles.append(angle)
    return cleaned_angles

pitch_angles = [10, 95, 45, -5, 85]
status_signals = [0, 1, 0, 1, 0]
print(clean_pitch(pitch_angles, status_signals))
