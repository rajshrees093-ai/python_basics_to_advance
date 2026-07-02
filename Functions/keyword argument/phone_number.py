def phone_num(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"
    
get_phone = phone_num(country=91, area=612, first=926 , last=521) 
print(get_phone)