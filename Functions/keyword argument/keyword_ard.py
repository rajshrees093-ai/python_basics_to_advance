# keyword argument= an argument preceded by an identifier
#                   helps with readability
#                   order of arguments doesn't matter
#                   positional argument follows keyword argument
                  
def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

# hello("hello", "Mr.", "Spongebob", "Squarepants")
hello(first="spongebob", greeting="hey", last="squarepants", title="Mr.")