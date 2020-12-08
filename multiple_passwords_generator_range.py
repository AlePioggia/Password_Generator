import random
from random import seed
import string
RANDOM_BOUNDARIES = 9

seed(random.random())

n_passwords = int(input("Insert the number of passwords to generate "))
password_length = int(input("Insert the n. of chars of the passwords(should be a square value, otherwise the chars number will be wrong "))
if password_length % 2 != 0:
    print("--WARNING-- the number of chars will be imperfect")
n_chars = int(password_length // 3)

f = open("password.txt", "w")
f = open("password.txt","a")
print("Getting started, generating passwords")
original_n_passwords = n_passwords
while n_passwords != 0:
    f.write("\t" + "--..-- RANDOM PASSWORD " + str(original_n_passwords + 1 - n_passwords) + " --..--" + "\n \n")
    for _ in range(0, n_chars):
        letter = random.choice(string.ascii_letters)
        f.write(letter)
        ascii_value = chr(random.randint(33,127))
        f.write(str(ascii_value))
        r = random.randint(0,RANDOM_BOUNDARIES)
        f.write(str(r))
    f.write("\n \n")
    n_passwords = n_passwords - 1
print("Job finished : check the file password.txt file for the passwords")
f.close()
