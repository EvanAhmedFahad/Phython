numOfLetter=0
numOfDigit=0
numOfWord=0

text=input("Enter any text : ")
for x in text :
    x.lower()
    if x>='a' and x<='z':
        numOfLetter=numOfLetter+1
    elif x>= '0' and x<='9':
        numOfDigit=numOfDigit+1
    elif x==' ':
        numOfWord=numOfWord+1
print("number of letter :",numOfLetter)
print("number of digit : ",numOfDigit)
print("number of Word",numOfWord +1)