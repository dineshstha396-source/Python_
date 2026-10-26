# Python String Practice 



# Check whether a string contains only alphabetic characters,  only digits or a mixture of letters or digits. 


string=input("Enter a string: ")

if string.isalpha():
    print(f"'{string}' is only alphabetical characters.")
elif string.isnumeric():
    print(f"'{string}' is only digits.")
elif string.isalnum():
    print(f"'{string}' is both alphabetical characters and digits.")
else:
    print("None")

# Given "apple,banana,mango,orange", split it into a list, then join the list back into a string separated by " | ".

original="apple,banana,mango,orange"

comma=original.split(",")
final="|".join(comma)
print(f"Original : {original} \n final : {final}")

#Replace every occurrence of "bad" with "good" in a sentence. Then replace only the first occurrence.

sentence=input("Enter the sentence containing word bad: ")

# every occurance
al=sentence.replace('bad','good')
print(f"Final_1 : {al}")

# first occurance 

first=sentence.replace('bad','good',1)
print(f"final_2 : {first}")

# Find the first and last positions of a given character in a string. Handle the case where it does not exist.
sentence=input("Give me sentence: ")
char=input("Give me a character: ")

char=char.lower()
sentence=sentence.lower()
found=False
for i in sentence:
    if i==char:
        found=True
        break

if not found:
    print(f"{char} not found in given string.")
else:
    first_index=sentence.find(char)

    last_index=first_index
    index=0
    for i in sentence:
        if i==char:
            last_index=index
        index+=1

    print(f"The first and last position of {char} are {first_index} and {last_index} respectively.")

#  Count how many times each vowel occurs in a string and store the results in a dictionary.

ca=0
ce=0
ci=0
co=0
cu=0
sentence=input("Give me sentence: ")

sentence=sentence.lower()

for i in sentence:
    if i=='a':
        ca+=1
    elif i=='e':
        ce+=1
    elif i=='i':
        ci+=1
    elif i=='o':
        co+=1
    elif i=='u':
        cu+=1
dic={'a':ca
     ,'e':ce,
     'i':ci,
     'o':co,
     'u':cu}
print(dic)

# Remove punctuation from a sentence while preserving letters, digits, and spaces

sentence=input("Enter a sentence: ")

final=""
for i in sentence:
    if i.isalpha() or i.isnumeric() or i==" ":
        final+=i

print(final)

#Normalize a messy string such as " DATA analytics IS useful " into "Data analytics is useful".

messy=" DATA analytics IS useful "

final=messy.strip()
final=final.capitalize()

print(final)

#Given an email address, extract the username and domain. Validate that it contains exactly one @ symbol and nonempty parts on both sides.

email=input("Enter a email address: ")

count=0
for i in email:
    if i=="@":
        count+=1
if count>1:
    print(f"'{email}' contain more than one @.")
elif count==0:
    print(f"'{email}' is invalid")
else : 
    li=email.split("@")
    for i in li: 
        print(i)
        if i=="":
            print(f"'{email}' has empty part")    


#Write a text-cleaning function that strips whitespace, converts text to lowercase,
# removes repeated spaces, and replaces punctuation with nothing

def clean(sentence:str):
    '''A function that clean the messy sentence'''
    sentence=sentence.strip().lower()
    final=""
    for i in sentence:
        if i.isalpha() or i.isnumeric():
            final+=i
        elif i==" ":
            if final.endswith(" "):
                continue
            else:
                final+=i
        else:
            final+=""

    return final

data=input("Enter a sentence: ")
final=clean(data)
print(final)


