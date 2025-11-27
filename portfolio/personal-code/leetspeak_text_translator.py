# GOAL: translate one phrase into another using defined rules.

# rules: a = 4, e = 3, o = 0, s = 5, i = 1

translation_dict = { # translation dictionary designed according to the translation rules.
    "a": 4,
    "e": 3,
    "i": 1,
    "o": 0,
    "s": 5
}

def translate(phrase):
   translation = "" # empty string to contain the translated phrase later on. 
   for letter in phrase:
       if letter.lower() in translation_dict: # checks if the lowercase character can be found in the translation dictionary.
            translation += str(translation_dict[letter.lower()]) # if the character can be found in the dictionary, find the key under the same name and swap 'letter' with the key's value.
       else:
           translation += letter # otherwise, add the letter onto the translation string as it is
   return translation.upper() # returns the translation in uppercase to complete the function.

print(translate(input("Tell me somethin' and I'll say it back my way! ")))
