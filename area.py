'''def area(type_,x):
    if type_=="circle":
        area=3.14*x**2
        print(area)
    elif type_=="square":
        area=x**2
        print(area)
    else:
        print("I don't know")
area("square",5)'''
"""
def fahrenheit_to_celcius():
    temp_str=input("Enter Farheneit temp:")
    if temp_str:
        if temp_str.isdigit():
            temp=int(temp_str)
            newTemp=5*(temp-32)/9
            print("The fahrenheit temperature",temp,"is equivalent to ",end="")
            print(newTemp,"degree celcius")
        else:
            print("You must enter a number...")
fahrenheit_to_celcius()
"""
def problem1_2(x,y):

    sum=x+y
    mul=x*y
    print("The Sum is: ",sum)
    print("The mul is: ", mul)
problem1_2(2,3)

