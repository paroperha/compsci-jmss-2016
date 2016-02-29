# Write a program to read in words from the keyboard one at a time until the word "quit" is typed.
# Store them in a list then print them alphabetically

quitting = False
wordlist = []

while not quitting:
    word = input("Please input a word: ")
    if word != "quit":
        wordlist.append(word)
    else:
        quitting = True

wordlist.sort()

for item in wordlist:
    print(item)
