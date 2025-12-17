# sentence = input("Enter your sentence : ")
# strings = sentence.split()
# longest = max(strings,key = len)
# print(longest)
    
sentence = input("Enter your sentence: ")
strings = sentence.split()
longest = ""

for word in strings:
    if len(word) > len(longest):
        longest = word

print(longest)
