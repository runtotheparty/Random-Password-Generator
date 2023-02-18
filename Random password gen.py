import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
#Generate more characters here
lowercaseLetter1=chr(random.randint(97, 122))
lowercaseLetter2=chr(random.randint(97, 122))
digit1=chr(random.randint(48, 57))
digit2=chr(random.randint(48, 57))
punch1=chr(random.randint(32, 47))
punch2=chr(random.randint(32, 47))
#....

#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punch1 + punch2
password = shuffle(password)

#Ouput
print(password)