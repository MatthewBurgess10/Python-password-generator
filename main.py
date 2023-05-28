import random

lowercharacters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
                   "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]
uppercharacter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                  "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z"]
    
    




lowercharacternum = random.randint(1, 15)

uppercharacternum = random.randint(1, 15)

specialcharacternum = random.randint(1, 15)


for i in range(0,lowercharacternum):
  lowercharacterchoice = random.choice(str(lowercharacters))

for i in range(0,uppercharacternum):
  uppercharacterchoice = random.choice(str(uppercharacter))
  
#for i in range(0,specialcharacternum):
  #specialcharacterchoice = random.choice(str(specialcharacter))
 
            
             

orderedpassword = lowercharacterchoice + uppercharacterchoice #+ specialcharacterchoice

shuffledstring = ''.join(random.sample(orderedpassword, len(orderedpassword)))
print(shuffledstring)


    

