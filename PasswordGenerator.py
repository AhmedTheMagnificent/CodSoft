import random
import string

length = int(input("Enter the excepted length of the password: "))
characterSet = string.ascii_letters + string.digits
password = "".join(random.choices(characterSet, k = length))
print(password)
