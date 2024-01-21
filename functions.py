from random import randint

n = 30

def solid(current_colour):
    return {i: (current_colour['R'],current_colour['G'],current_colour['B'])
            for i in range(n)}

def aura(current_colour):
    perc = 90

    print(randint(-perc,perc)//100)

    d= {i: (current_colour['R'] + randint(-perc,0) * current_colour['R'] // 100,
            current_colour['G'] + randint(-perc,0) * current_colour['G'] // 100,
            current_colour['B'] + randint(-perc,0) * current_colour['B'] // 100 )
            for i in range(n)}
    print(d)
    return d