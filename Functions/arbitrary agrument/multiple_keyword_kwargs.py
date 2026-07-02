def print_address(**kwargs):  #type of kwargs is dictionary
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_address(street="123 Mary street",
               city="Noida", 
               state="Uttar Pradesh", 
               pin="201134")