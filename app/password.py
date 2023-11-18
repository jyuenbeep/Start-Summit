import random

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = []

for i in ( list(range(33, 47+1)) + list(range(58, 64+1)) + list(range(91, 96+1)) + list(range(123, 126+1))):
    SYMBOLS.append( chr(i) )

# user_input = input()

# user can put in multiple words
def create_password(s):
    no_space_string = s.replace(" ", "")

    while len(no_space_string) <= 6:
        no_space_string += LETTERS[int(random.random()*26)]

    temp_list = list(no_space_string)
    
    for i in range(0, len(temp_list)):
        random_num = int(random.random()*4)
        if random_num == 0:
            temp_list.append(NUMBERS[ int(random.random()*(len(NUMBERS)-1)) ])
        elif random_num == 1:
            temp_list.append(SYMBOLS[ int(random.random()*(len(SYMBOLS)-1)) ])
        elif random_num == 2:
            temp_list[i] = temp_list[i].upper()
        else:
            temp_list[i] = temp_list[i].lower()
            
    random.shuffle(temp_list)
    
    new_password = ''.join(temp_list)

    return no_space_string + new_password

# print( create_password("northeastern") )

WEAK0 = "Weak password. Can be cracked INSTANTLY"
WEAK1 = "Weak password. Can be cracked IN A FEW SECONDS"
WEAK2 = "Weak password. Can be cracked IN A FEW MINUTES"
WEAK3 = "Weak password. Can be cracked IN A FEW HOURS"
WEAK4 = "Weak password. Can be cracked IN A FEW DAYS"
MEDIUM0 = "Decent password. Could be cracked in LESS THAN A YEAR"
MEDIUM1 = "Decent password. Could be cracked in A FEW YEARS (1-20)"
STRONG = "Strong password. Cannot be cracked for 100+ years!!"

# passwords do not have spaces
def analyze_password(s):
    lowercased = s.lower()
    temp_list = list(lowercased)
    pw_length = len(lowercased)
    
    # checks if password contains only numbers
    if all(character in NUMBERS for character in temp_list):
        if pw_length <= 11:
            return WEAK0
        elif pw_length <= 13:
            return WEAK1
        elif pw_length <= 15:
            return WEAK2
        elif pw_length <= 16:
            return WEAK3
        elif pw_length <= 19:
            return WEAK4
        elif pw_length <= 20:
            return MEDIUM1

    # checks if passwords contains only letters
    elif all(character in LETTERS for character in temp_list):
        if pw_length <= 6:
            return WEAK0
        elif pw_length <= 7:
            return WEAK1
        elif pw_length <= 8:
            return WEAK2
        elif pw_length <= 9:
            return WEAK3
        elif pw_length <= 10:
            return WEAK4
        elif pw_length <= 11:
            return MEDIUM0
        elif pw_length <= 12:
            return MEDIUM1
        elif pw_length <=20:
            return STRONG
    elif any(character in temp_list for character in LETTERS+NUMBERS):
        if pw_length <= 6:
            return WEAK0
        elif pw_length <= 7:
            return WEAK1
        elif pw_length <= 8:
            return WEAK2
        elif pw_length <= 9:
            return WEAK3
        elif pw_length <= 10:
            return WEAK4
        elif pw_length <= 11:
            return MEDIUM1
        else:
             return STRONG
    # checks if password contains any special characters
    elif any(character in temp_list for character in SYMBOLS):
        if pw_length <= 5:
            return WEAK0
        elif pw_length <= 6:
            return WEAK1
        elif pw_length <= 7:
            return WEAK2
        elif pw_length <= 8:
            return WEAK3
        elif pw_length <= 9:
            return MEDIUM0
        elif pw_length <= 20:
            return STRONG
    # passwords with length > 20 
    else:
        return "This analyzer can only return results for passwords up to a length of 20, but if your password is more than 20 numbers long, it should be pretty strong"


# print("123:" + analyze_password("123"))
# print("northeastern" + analyze_password("northeastern") )
# print("a*fjklDW112321" + analyze_password("a*fjklDW112321"))