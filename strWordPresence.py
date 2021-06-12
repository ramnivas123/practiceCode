wordlist = input("enter the sentence")
wordlist.split()
word = input("enter the word")
if word in wordlist:
    print(f"{word} is present")
else:
    print(f"{word} is not present")