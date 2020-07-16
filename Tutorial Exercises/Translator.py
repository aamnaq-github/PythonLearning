vowels = ["a", "e", "i", "o", "u"]

def translate (phrase):
    translation = ""
    for letter in phrase:
        if vowels.__contains__(letter.lower()):
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print("Translation: " + translate(input("Enter a phrase: ")))
