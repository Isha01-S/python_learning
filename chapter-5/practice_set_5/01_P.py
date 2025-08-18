'''Write a program to create a dictionary of hindi words with values as their English translation.
Provide user with an option to look it up.'''

words = {'madad':'help',
         'kursi':'chair',
         'billi': 'cat'
         }

word = input("Name the word you want the meaning of : ")

print(words[word])