#-- shout out to gemini for helping with this 


# Type checking decorator(90% ai code)
import functools

def ensure_numbers(func):
    """
    Decorator to ensure both arguments 'a' and 'b' are numeric (int or float).
    """
    @functools.wraps(func)
    def wrapper(a, b):
        # Check if 'a' is a valid numeric type
        if not isinstance(a, (int, float)):
            raise TypeError(
                f"Invalid type for first argument 'a' in {func.__name__}: "
                f"Expected int or float, but got {type(a).__name__}"
            )
        
        # Check if 'b' is a valid numeric type
        if not isinstance(b, (int, float)):
            raise TypeError(
                f"Invalid type for second argument 'b' in {func.__name__}: "
                f"Expected int or float, but got {type(b).__name__}"
            )
            
        # If checks pass, execute the original function
        return func(a, b)
    
    return wrapper
#---- end of ai code
def multiplication(a, b):
    return a * b

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b
def distribution(a, b):
    if b == 0:
        return "error, cannot divide by 0"
    else:
        return a / b
    
def pangkat(a, b):
    return a^b
def sisa(a, b):
    return a % b
def akar(a, b):
    return a ** b



def something(operator, a, b):
    if operator == "+":
        return addition(a, b)
    elif operator == "-":
        return subtraction(a, b)
    elif operator == "*":
        return multiplication(a, b)
    elif operator == "/":
        return distribution(a, b)
    elif operator == "^":
        return pangkat(a, b)
    elif operator == "%":
        return sisa(a, b)
    elif operator == "**":
        return akar(a, b)
    
    
FUNCTIONS_TO_DECORATE = [
    "multiplication", 
    "addition", 
    "subtraction", 
    "distribution", 
    "pangkat", 
    "sisa", 
    "akar"
]

for func_name in FUNCTIONS_TO_DECORATE:
    original_func = globals()[func_name]
    decorated_func = ensure_numbers(original_func)
    globals()[func_name] = decorated_func # Use dict assignment for conciseness