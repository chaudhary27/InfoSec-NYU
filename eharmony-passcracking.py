# Assignment # 2
# Using Python 2.7.10

# Name: Faisal Farooq
# Professor: Aspen Olmsted 

import hashlib

eharmony = open('eharmony passwords.txt', 'r')

# collecting hashed passwords in a set
eharmony_md5 = set()
for each_line in eharmony:
    eharmony_md5.add(each_line.replace('\r\n', ""))

password_list = open('crackstation.txt', 'r')
output_file = open('eharmony-cracked-passwords.txt', 'r+')

# iterating over password list
for each_line in password_list:
    # replacing the newline character with empty and converting to uppercase
    word_list = each_line.replace("\n", "").upper()
    
    #obtaining md5 hash of the uppercase word
    hash_of_uppercase_word = hashlib.md5(word_list).hexdigest()

    # check if hash obtained from word list matches with eharmony md5 list
    if hash_of_uppercase_word in eharmony_md5:
        output_file.write(hash_of_uppercase_word+ " "+ word_list + "\n")
        print(hash_of_uppercase_word+" "+word_list)
