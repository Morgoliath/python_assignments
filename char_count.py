sentence = input("Enter your sentence to count the characters in it: ").lower()
char_count = {}
for i in sentence:
  if i not in char_count.keys():
    char_count.update({i: sentence.count(i)})
print(char_count, end="")
