def formart_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return ("Invalid inputs")
    name = f_name + " " + l_name
    return name.title()


f_name = input("Type your first name: ")
l_name = input("Type your last name: ")

outoput = formart_name(f_name, l_name)

print(outoput)
