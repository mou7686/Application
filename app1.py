import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    if w in data:
        return data[w]

    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean {} instead? Enter Y if Yes,or N if No: " .format(get_close_matches(w,data.keys())[0])).upper()
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."

    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ").lower()

output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)