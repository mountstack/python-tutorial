
# info = {
#     "name": "Rijwan", 
#     "roll_no": 100, 
#     "is_married": False
# } 

# print(info["name"])


# Exercise 
num = "17527"
# One Seven Five Two Seven

result = ""
digits = {
    "0": "zero", 
    "1": "One", 
    "2": "Two", 
    "3": "Three", 
    "4": "four", 
    "5": "Five", 
    "6": "Six", 
    "7": "Seven", 
    "8": "Eight", 
    "9": "Nine"
}

for d in num:
    result = result + digits[d] + " "

print(result)
