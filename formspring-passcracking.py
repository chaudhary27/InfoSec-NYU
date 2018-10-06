# Assignment # 2
# Using Python 2.7.10

# Name: Faisal Farooq
# Professor: Aspen Olmsted

import hashlib

formspring = open('./formspring/formspring.txt', 'r')

formspring_sha256 = set()

for line in formspring:
    formspring_sha256.add(line.replace("\n", ""))

password_list = open('./crackstation.txt', 'r')
output_file = open('formspring-cracked-passwords.txt', 'r+')

# iterating over password list
for each_line in password_list:
    # replacing the newline character with empty
    word_list = each_line.replace("\n", "")
    
    #obtaining sha-256 hash of the words in dictionary list
    hash_of_word_list = hashlib.sha256(word_list).hexdigest()

    # check if hash obtained from word list matches with formspring sha-256 list
    if hash_of_word_list in formspring_sha256:
        output_file.write(hash_of_word_list + " " + word_list + "\n")
        print(hash_of_word_list+" "+word_list)
