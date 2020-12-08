import random
from random import seed
import string
RANDOM_BOUNDARIES = 9

seed(random.random())
n_chars = 10
n_passwords = 10

f = open("password.txt", "w")
f = open("password.txt","a")
print("Getting started, generating 10 passwords with 30 chars on file password.txt on current directory")
while n_passwords != 0:
    f.write("\t" + "--..-- RANDOM PASSWORD " + str(11 - n_passwords) + " --..--" + "\n \n")
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
