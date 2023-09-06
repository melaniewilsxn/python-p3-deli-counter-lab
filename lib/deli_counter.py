def line(deli):
    deli_line = "The line is currently:"
    if deli == []:
        print("The line is currently empty.")
    else:
        i=1
        for name in deli:
            deli_line += f' {i}. {name}'
            i += 1
        print(deli_line)

    
def take_a_number(deli, name):
    number = len(deli) + 1
    deli.append(name)
    print(f'Welcome, {name}. You are number {number} in line.')

def now_serving(deli):
    if deli == []:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {deli[0]}.")
        deli.pop(0)