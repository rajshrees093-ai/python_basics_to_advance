def shipping_label(*args, **kwargs):  #can accept both args and kwargs and args is followed by the kwargs but if vice versa then it will show error
    for arg in args:
        print(arg, end=" ")
    print()
    # for value in kwargs.values():
    #     print(value, end=" ")

    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}")
    print(f"{kwargs.get('state')}")
    print(f"{kwargs.get('pincode')}")


shipping_label("Mr.", "Dipak", "Ranjan", "Advocate",
               street="123 xyz street",
               apt="101",
               city="noida",
               state="uttar pradesh",
               pincode="211045")
