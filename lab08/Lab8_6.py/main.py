import sys
import io

# Set stdout to utf-8 encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from Dog import Dog
from Cat import Cat

# Creating instances
dog1 = Dog("หมา1", "พันธุ์บางแก้ว", 3)
cat1 = Cat("แมว1", "พันธุ์เปอร์เชีย", 2)

# Using the instances
print(dog1.display_info())  # Expected Output: Name: หมา1, Age: 3, Breed: พันธุ์ไทยบ้าน
print(dog1.makeSound())     # Expected Output: Woof!

print(cat1.display_info())  # Expected Output: Name: แมว1, Age: 2, Breed: พันธุ์เปอร์เชีย
print(cat1.makeSound())     # Expected Output: Meow!
