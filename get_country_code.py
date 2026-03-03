country_code={"India":"0091","Austalia":"0025","Nepal":"00977",}

print("the country code for India-",end=(""))
print(country_code.get("India","not found"))

print("the country code for America-",end=(""))
print(country_code.get("America","not found"))