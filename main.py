import random

lowercharacters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
                   "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]
uppercharacter = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    #The ord function gets Unicode starting character of a and ending character of z, then it loops through from a to z 
    #thereby getting all the letters of the alphabet
    


specialcharacter = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                      '-', '_', '+', '=', ',', '.', '/', '?']



lowercharacternum = random.randint(0, 7)

uppercharacternum = random.randint(0, 6)

specialcharacternum = random.randint(0, 5)


for i in range(lowercharacternum):
  lowercharacterchoice = str(random.choice(lowercharacters))

for i in range(uppercharacternum):
  uppercharacterchoice = random.choice(uppercharacternum)
  
for i in range(specialcharacternum):
  specialcharacterchoice = str(random.choice(specialcharacter))
 
            
             

orderedpassword = lowercharacterchoice + uppercharacterchoice + specialcharacterchoice
shuffledpassword = random.shuffle(orderedpassword)
print(shuffledpassword)
    

    


    

