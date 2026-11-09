# Function:Double the input number.

def double(number):
    """returns the number doubled"""
    return number * 2

def is_pass(score):
    """return true if the number is a passing score"""
    return score >= 50

def greet(name, greeting="hello"):
    """returns a greeting for a name, defaulting to Hello"""
    return greeting + ", " + name + "!"


print(double(7))
print(double(10))
print(is_pass(80))
print(is_pass(20))
print(greet("Amina"))
print(greet("Brian", "Habari"))