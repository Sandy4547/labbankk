import sys
import io

# Set stdout to utf-8 encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from Dog import Dog
from Cat import Cat

def print_pet_info(pet):
    print(pet.display_info())
    print(pet.makeSound())

# Creating instances of dogs
dog1 = Dog("บุญรอด", "บางแก้ว", 3)
dog2 = Dog("ดัชมิล", "ลาบาดอล", 4)
dog3 = Dog("ศรีบูด", "ไซบิเลียน", 2)

# Creating instances of cats
cat1 = Cat("มันนี่", "เปอร์เซีย", 2)
cat2 = Cat("ชาบู", "สก็อตติช", 3)
cat3 = Cat("คัพเค้ก", "วิเชียรมาศ", 4)

# Creating a list of pets
pets = [dog1, dog2, dog3, cat1, cat2, cat3]

# Using polymorphism to display information and sounds
for pet in pets:
    print_pet_info(pet)
    print()
