# switch statement (match-case statement) = An alternative to using many 'elif' statements
#                                           execute some code if a value matches a 'case'
#                                           Benefits: cleaner and syntax is more readible

# def week_days(day):
#     if day ==1:
#         return "it is sunday"
#     elif day==2:
#         return "it is monday"
#     elif day==3:
#         return "it is tuesday"
#     elif day==4:
#         return "it is wednesday"
#     elif day==5:
#         return "it is thursday"
#     elif day==6:
#         return "it is friday"
#     elif day==7:
#         return "it is saturday"
#     else:
#         return "invalid day!"
    
# print(week_days(5))



#using switch cases
def week_days(day):
    match day:
        case 1:
            return "it is sunday"
        case 2:
            return "it is monday"
        case 3:
            return "it is tuesday"
        case 4:
            return "it is wednesday"
        case 5:
            return "it is thursday"
        case 6:
            return "it is friday"
        case 7:
            return "it is saturday"
        case _:
            return "invalid day!"
    
print(week_days(5))