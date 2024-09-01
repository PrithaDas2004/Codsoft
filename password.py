import random
import string

def generate_password(length):
 
  lowercase = string.ascii_lowercase
  uppercase = string.ascii_uppercase
  digits = string.digits
  punctuation = string.punctuation

  all_characters = lowercase + uppercase + digits + punctuation

  password = ''.join(random.choices(all_characters, k=length))

  return password

password_length = int(input("Enter desired password length (minimum recommended: 8): "))

while password_length < 8:
  password_length = int(input("Password length should be at least 8. Please enter a new length: "))

generated_password = generate_password(password_length)
print("Your randomly generated password:", generated_password)

