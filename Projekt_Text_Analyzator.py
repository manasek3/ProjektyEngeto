uzivatel = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
oddelovac = "-" * 50
texts = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
print(oddelovac)
print("Welcome to the app. Please log in:")

username = input("USERNAME: ")
password = input("PASSWORD: ")

while uzivatel.get(username) != password:
    print("Wrong username or password! Try again")
    username = input("USERNAME: ")
    password = input("PASSWORD: ")
else:
    print(oddelovac)

print("We have", len(texts), "texts to be analyzed")
volba = input("Enter a number btw. 1 and 3 to select: ")

while not volba.isnumeric() or int(volba) not in range(1,4):
    print("Invalid input! Try again")
    volba = input("Enter a number btw. 1 and 3 to select: ")
else:
    volba = int(volba)
    print(oddelovac)

text_list = [slova.strip(".,") for slova in texts[volba-1].split()]
text_pocet_title = 0
text_pocet_upper = 0
text_pocet_lower = 0
text_pocet_numeric = 0
soucet_cisel_text = 0
dict_graph = {}

for i in text_list:
    dict_graph[len(i)] = dict_graph.setdefault(len(i), 0) + 1

    if i.istitle():
        text_pocet_title += 1

    elif i.isupper():
        text_pocet_upper += 1

    elif i.islower():
        text_pocet_lower += 1

    elif i.isnumeric():
        text_pocet_numeric += 1
        soucet_cisel_text += float(i)



print(f"""
There are {len(text_list)} words in the selected text.
There are {text_pocet_title} titlecase words.
There are {text_pocet_upper} uppercase words.
There are {text_pocet_lower} lowercase words
There are {text_pocet_numeric} numeric strings.
""")
print(oddelovac)

for klic, hodnota in sorted(dict_graph.items()):
    print(klic, "*" * hodnota, hodnota)

print(oddelovac)
print("If we summed all the numbers in this text we would get:",soucet_cisel_text)