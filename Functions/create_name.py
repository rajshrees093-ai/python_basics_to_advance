def create_name(first_name, middle_name, last_name):
    first_name=first_name.capitalize()
    middle_name=middle_name.capitalize()
    last_name=last_name.capitalize()
    return first_name+ " "+ middle_name + " " + last_name

full_name= create_name("Rajshree","","Sinha")
print(full_name)