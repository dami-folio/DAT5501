# GOAL: translate one phrase into another using defined rules.

# rules: a = 4, e = 3, o = 0, s = 5, i = 1

translation_dict = {
    "a": 4,
    "e": 3,
    "i": 1,
    "o": 0,
    "s": 5
}

def translate(phrase):
   translation = ""
   for letter in phrase:
       if letter.lower() in translation_dict:
            translation += str(translation_dict[letter.lower()])
       else:
           translation += letter
   return translation.upper()

print(translate(input("Tell me somethin' and I'll say it back my way! ")))
