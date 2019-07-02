strn=input("")
vow=["a","e","i","o","u"]
cons=["b","c","d","f","g","h","j","k","l","m","n","s","p","q","r","t","v","w","x","y","z"]
if(strn in vow):
    print("Vowel")
elif(strn in cons):
    print("Consonant")
else:
    print("Invalid")

