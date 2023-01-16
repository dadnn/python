
# Basics ----

def say_hi(name, age):
    print("Hello " + name)
    print("You are " + str(age))



def cube(num):
    return num*num*num

result = cube(7)
print(str(result) + " Industries")



# If Statements ----

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are a tall Female")
else:
    print ("You are a short Female.")

if is_male or is_tall:
    print("You are either a male or tall")
else:
    print ("You are either not male or not tall or both.")



# If Statement Comparisons ----

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(38, 59, 1))



# While Loops ----

i = 1

while i <= 10:
    print(i)
    i += 1

print("Done with loop.")

