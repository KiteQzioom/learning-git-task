shopping = {
    "piekarnia": ["chleb", "bułki", "pączki"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

shopping2 = {
    "piekarnia": [],
    "warzywniak": []

}

rzeczy_piekarnia = []
rzeczy_warzywniak = []

for index, (key,value) in enumerate(shopping.items()):
    for rzecz in value:
        if index == 0:
            rzeczy_piekarnia.append(rzecz.capitalize())
        elif index == 1:
            rzeczy_warzywniak.append(rzecz.capitalize())

shopping2["piekarnia"]=rzeczy_piekarnia
shopping2["warzywniak"]=rzeczy_warzywniak             

length = len(shopping["piekarnia"])+len(shopping["warzywniak"])
print("Lista zakupów")
for sklep, lista in shopping2.items():
    print(f"Idę do {sklep.capitalize()}, kupuję tu następujące rzeczy: {lista}")
print("W sumie kupuję " + str(length) + " produktów.")

print("udało się?")