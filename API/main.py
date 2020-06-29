from random import randrange

str = "adasdasad"
new_str=""
for i in str:
    try:
        new_str += i.upper() if bool(randrange(2)) else i
    except:
        new_str += i

print(new_str)