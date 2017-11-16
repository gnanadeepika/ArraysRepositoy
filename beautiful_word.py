import sys

w = input("Enter a string:").strip()

vowels=['a','e','i','o','u','y']

def beautiful_or_not(w):
    for i in range(1,len(w)-1):
        if w[i]==w[i-1] or w[i]==[i+1]:
            return False
        if w[i] in vowels and (w[i-1] in vowels or w[i+1] in vowels):
            return False
    return True

if beautiful_or_not(w)==True:
    print("yes beautiful")
else:
    print("Not beautiful")




#Print 'Yes' if the word is beautiful or 'No' if it is not.