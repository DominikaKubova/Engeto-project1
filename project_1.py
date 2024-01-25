"""
project_1.py: 1st project for ENGETO online academy
Autohor: Dominika Kubová
email: dominika.kubova@gmail.com   
Discord: dominika_50263
"""

TEXTS = ["""Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. """,
"""At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
"""The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present."""
]

#separator
separator = 80 * "="

#List of registered users
REGISTERED_USERS = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}

#Preview of texts for user before requesting a choise
def text_preview():
    print("You can analyze following", len(TEXTS), "texts: \n") 

    for n in range(len(TEXTS)):
        print("This is text number", n+1, "\n" )
        print(TEXTS[n], "\n")




#User chooses which text is analyzed.
def text_choise():
    chosen_number_of_text =  input("Choose the number of text you want to analyze.")
    if not chosen_number_of_text.isdecimal() or not int(chosen_number_of_text) in range(len(TEXTS)):
        print("There is no text avaliable with number", chosen_number_of_text, "or you did not enter a number")
    else:
        print("Let's analyze text number", chosen_number_of_text)
        analyzed_text_index = int(chosen_number_of_text) - 1
        final_choise = TEXTS[analyzed_text_index] 
    return final_choise


#TEXT ANALYZE#
def text_analyze(final_choise):
    print(final_choise)

    list_of_words = final_choise.split()

    number_words = len(list_of_words)
    print("\nThere are ", number_words, "words in the selected text.")

    number_words_1st_cap = find_words_1st_cap(list_of_words)
    print("There are ", number_words_1st_cap, "titlecase words.")

    number_words_all_cap = find_words_all_cap(list_of_words)
    print("There are", number_words_all_cap, "uppercase words.")

    number_words_lower_cap = find_words_all_lowercase(list_of_words)
    print("There are", number_words_lower_cap, "lowecase words.")

    number_count = find_count_numbers(list_of_words)
    print("There are", number_count, "numeric strings.")

    sum_all_numbers = find_sum_all_numbers(list_of_words)
    print("The sum of all numbers is: ", sum_all_numbers, ".")

   
    lenght_graph = count_lenght_of_words(list_of_words)
    draw_graph(lenght_graph)



#Finding words with 1st letter upper case
def find_words_1st_cap(list_of_words):
    count = 0
    for word in list_of_words:  
        if word[0].isupper():
            count += 1
    return count

#Finding words in all CAPS 
#I also count 30N as allcap
def  find_words_all_cap(list_of_words):
    count = 0
    for word in list_of_words:
        if word.isupper():
            count += 1
    return count

#Finding words in lower case
def find_words_all_lowercase(list_of_words):
    count = 0
    for word in list_of_words:
        if word.islower():
            count += 1
    return count

#Finding number of integers

def find_count_numbers(list_of_words):
    count = 0
    for word in list_of_words:
        if word.isdecimal():
            count += 1
    return count

#Finding the sum of all numbers
def find_sum_all_numbers(list_of_words):
    sum_of_numbers = 0
    for word in list_of_words:
        if word.isdecimal():
            sum_of_numbers = sum_of_numbers + int(word)
    return sum_of_numbers

#Finding lenght of words

def count_lenght_of_words(list_of_words):
    lenght_of_words = {}
    for word in list_of_words:
        word = word.strip(",.")
        word_lenght = len(word)
        if word_lenght in lenght_of_words.keys():
            occurance = lenght_of_words.get(word_lenght)
            lenght_of_words.update({word_lenght : (occurance + 1)})
        else:
            lenght_of_words.update({word_lenght : 1})    
    return(lenght_of_words)

#Drawing a graph based on input from function count_lenght_of_words()

def draw_graph(lenght_of_words):
    small_separator = 80 * "-"
    print(small_separator)
    print("LEN|    OCCURANCES   |NR.    ")
    print(small_separator)
    for key in sorted(lenght_of_words.keys()):
        print(key, "|", lenght_of_words.get(key) * "*", "|", lenght_of_words.get(key))
    

## MAIN CODE ##

#User will insert login details
user = input("Insert your username: ")
password = input("Insert you password: ")

print(separator)


#If user put correct login, text can be analyzed. If not, programme is closed.
if REGISTERED_USERS.get(user) == password:
    print("Welcome", user, "! Let's analyze texts!")
    print(separator)
    #function for text preview
    text_preview()
    print(separator)
    #function for text choise
    final_choise = text_choise()
    print(separator)
    #function for text analyzing 
    text_analyze(final_choise)
    print(separator)
else:
    print("Sorry, you are not registered. Closing the program.")