def nameValidator(name):
    if type(name) is not type(""):
        return "Error: Your argument has to be a string."
    listName = name.split(" ")
    if len(listName) != 2:
        return "Error: Name should both and only contain your first and last name"
    elif (listName[0].isalpha()) == False or (listName[1].isalpha()) == False or name.count(" ") != 1:
        return "Error: Name should only contain alphabets and/or should not have more than one space."
    elif 5 > len(listName[0]) or 20 < len(listName[0]) or 5 > len(listName[1]) or 20 < len(listName[1]):
        return "Error: The length of the first and/or last name should be between 5 and 20, both inclusive."

    return "Validation successful"


print(nameValidator(12345))
print(nameValidator("Jonathan"))
print(nameValidator("Jonathan Ayomide Kolawole"))
print(nameValidator("Jonathan Kol77awole"))
print(nameValidator("Jonatvhvhvjhhcncvcncnvfugkkgkgjbkbkjlnlhan Kolawole"))
print(nameValidator("Jonathan Kolawole    "))
print(nameValidator("   Jonathan Kolawole"))
print(nameValidator("Jonathan Kolawole"))
