from lab5_3 import line_base
from lab5_4 import top_leaf

def middle_leaf():
    line_base(5, 3)
    line_base(4, 5)
    line_base(2, 9)

def bottom_leaf():
    line_base(4, 5)
    line_base(2, 9)
    line_base(0, 13)

def base():
    line_base(5, 3)
    line_base(5, 3)
    line_base(5, 3)
def tree():
    print("_ _ _ _ _ _ _ _ _ _ _")
    top_leaf()
    middle_leaf()
    bottom_leaf()
    base()
    print("_ _ _ _ _ _ _ _ _ _ _")
if __name__ == "__main__":
    tree()