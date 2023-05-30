import random
import string


def generation(length):
  characters = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters)for i in range(length))
  return password

length = int(input('Enter the length of the password: '))
password = generation(length)
print('Your password is: {0}'.format(password))


    

