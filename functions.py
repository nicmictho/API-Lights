n = 30

def solid(current_colour):
    return {i: (current_colour['R'],current_colour['G'],current_colour['B'])
            for i in range(n)}