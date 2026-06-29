colors = ("blue", "yellow", "lavendar", "pink", "black")
print(type(colors))
print(colors)

print(colors.index("pink")) #returns the index of specific element
print(colors.count("yellow"))

#iteration
for color in colors:
    print(color)