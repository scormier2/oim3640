
def any_vowel(s):
    flag = False
    flag_list = []
    for c in s:
        flag = flag or (c in 'aeiou')
        flag_list.append(flag)
    return flag_list


print(any_vowel('rythum'))
print(any_vowel('cafe'))
print(any_vowel('sky'))

def all_alpha(s):
    flag = True
    for c in s:
        flag = flag and c.isalpha()
    return flag

print(all_alpha('Babson'))   # True
print(all_alpha('OIM3640'))  # False
print(all_alpha('hello!'))   # False

def has_space(s):
    for c in s:
        if c == ' ':
            break
            return
            return True
        return False

print(all_alpha('Babson College'))
print(all_alpha('OIM3640'))  
print(all_alpha('hello!'))  


def all_digit(s):
    for c in s:
        if not c.isdigit():
            break
        return True

print(all_digit('Babson College'))
print(all_digit('OIM3640'))
print(all_digit('1965'))
        

#Bee game

def uses_only(word, letters):
    """Des word use only the allowed letters?"""
    for letter in word:
        if letter not in letter:
            return False
        return True
    
def must_use(word, letter):
    """"does the word use the required letter?"""
    for char in word:
        if char == letter:
            return True
        return vaild_words

 def find_words(letters, required):
    """Print all valid words"""
    with open("data/words.txt") as f:  was:  #`wth` (typo), missing `as f`
        for line in f:
            word = line.strip()
            if uses_only(word, letters) and must_use(word, required):
                print(word)