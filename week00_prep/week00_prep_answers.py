#ex1 
def great(name):
    return "Hello " + name + "!"
#ex 2
def goldilocks(lenght):
    if lenght < 140:
        return "unhappy!"
    elif lenght > 150:
        return "unhappy!"
    else:
        return "perfect!"
#ex3 
def square_list(number_list):
    for i in range(len(number_list)):
        number_list[i]=number_list[i]**2
    return number_list
#ex4

def fibonacci_stop(max):
    for i in range(max):
        if i == 0:
            fib = [0]
        elif i == 1:
            fib.append(1)
        else:
            fib.append(fib[-1] + fib[-2])
        if fib[-1] >= max:
            return fib[:-1]
        return fib
#ex5 
def clean_pitch(pitch_angles, status_signals):
    cleaned_pitch = []
    for i in range(len(pitch_angles)):
        angle = pitch_angles[i]
        status = status_signals[i]
        if (angle < 0 or angle > 90) and status > 0:
            cleaned_pitch.append(-999)
        else:
            cleaned_pitch.append(angle)
    return cleaned_pitch


