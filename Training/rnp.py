roda = "Sorte"
lenght = len(roda)
print(lenght)

mosca = "voa"
upper = mosca.upper()
print(upper)


mosca = "VOA"
lower = mosca.lower()
print(lower)


predio = "Amadora"
replace = predio.replace("Amadora","Queluz")
print(replace)


string_variable = "Hello, World!"
lowercase_string = string_variable.lower()
print(lowercase_string)


split_words = "Casa na Montanha do Tio Antonio"
split = split_words.split( )
print(split)

#the bellow list of numbers are mutable that means they can be changed
numbers_list = [1,2,3,4,5]
print(numbers_list)

#the bellow list of numbers are inmutable (tuple) that means they can't be changed unless I go there and change them
numbe_list = (1,2,3,4,5)
print(numbe_list)

#Sets data type, we can add an item but not modify: commands are .add .remove .update
sets_list = {1, 2, 3, 4, 5}
print(sets_list)
sets_list.add(6)
print(sets_list)

# My Vmware data

Vmware_data = {
    "hostname":"ExSiV8",
    "Servers":{"Ip Address-1":"172.16.1.5","Ip Address-2":"172.16.1.4"},
    "Username":"root",
    "Password":"Rambo123!",

}

print(Vmware_data["Servers"]["Ip Address-2"])


#Boolean types

Server_up = True

if Server_up:
    print("Server is running")

else:
    print("Server is down")






a = 50
b = 10

is_equal = a == b
is_greater = a < b

print(is_equal)
print(is_greater)

#Write a Python program that performs the following operations on a given string:

# Input string

# text = "Python programming is fun and powerful!"

# Check if the string starts with a particular word and ends with a particular word.

text = "Python programming is fun and powerful!"

Python = True
powerful = True

if text.startswith("Python"):
    print("This is the first word")
else:
    print("this is not the first word")

if text.endswith("powerful"):
    print("this is the last word")
else:
    print("this is not the last word")



