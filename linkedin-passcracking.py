# Assignment # 2
# Using Python 2.7.10

# Name: Faisal Farooq
# Professor: Aspen Olmsted

import hashlib

linkedin = open('linkedin-SHA1.txt', 'r')
password_list = open('./dictionary-lists/human-onlycrackstation.txt', 'r')
output_file = open('linkedin-cracked-passwords.txt', 'r+')

# collecting hashed passwords in a set
linkedin_sha1 = set()
for each_line in linkedin:
    linkedin_sha1.add(each_line.replace('\n', ""))

# iterating over password list
for each_line in password_list:
    # replacing the newline character with empty
    word_list = each_line.replace("\n", "")
    
    # generating sha-1 hash for the words in dictionary list
    hash_of_word_list = hashlib.sha1(word_list).hexdigest()

    # check if hash obtained from word list matches with linked sha-1 list
    if hash_of_word_list in linkedin_sha1:
        output_file.write(hash_of_word_list + " " + word_list + "\n")
        print(hash_of_word_list+" "+word_list)
