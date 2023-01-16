
# Lists (arrays)

family = ["Dylan", "Christina", "Elijah", "Jonah", "Emma"]
lucky_numbers = [7, 14, 21, 28, 35, 49, 42]

family2 = family.copy()

family[4] = "Isabella"

print(family)
print(family[0])
print(family[-1])
print(family[2:])
print(family[1:3])

family.append("Baby #4?")
family.extend(lucky_numbers)
family.remove("Dylan")
family.insert(0, "Dylan")
family.insert(0, "Dylan")
print(family)

print(family.index("Jonah"))
print(family.count("Dylan"))

lucky_numbers.sort()
lucky_numbers.reverse()
print(lucky_numbers)

# Tuples CANNOT be changed

coordinates = (7,14)

print(coordinates[1])

