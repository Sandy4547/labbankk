from lab5_3 import line_base
from lab5_4 import top_leaf

def middle_leaf():
    print("2. Draw middle leaf.")


def bottom_leaf():
    print("3. Draw bottom leaf.")

def base():
    line_base(0, 3)
    line_base(0, 3)
    line_base(0, 3)
    
def tree():
    print("_ _ _ _ _ _ _ _ _ _ _")
    top_leaf()
    middle_leaf()
    bottom_leaf()
    base()
    print("_ _ _ _ _ _ _ _ _ _ _")
if __name__ == "__main__":
    tree()