## Usage of Decorators

# Decorator Code Segment Begin
def new_decorator_code(original_func):
    # Wrap Segment Begin
    def wrap_func():
        # Some new code before the original code segment
        print("Some new code before the original code segment")
        
        # Original code
        original_func()

        # Some new code after the original code segment
        print("Some new code after the original code segment")
        
        # Wrap Segment End
    return wrap_func
# Decorator Code Segment End

# Using the Decorator Code segment
@new_decorator_code
# Original Code Segment Begin
def func_to_decorate():
    print("\tThis is original code segment begin")
    print("\tThis is original code segment end")
# Original Code Segment End

func_to_decorate()
