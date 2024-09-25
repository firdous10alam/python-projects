# Here one thing I need to understand is if I replace story with keyword what will happen.
# Here I learned about how to use set and dictionary.
# Also learned about replace function.

with open("project/story.txt", "r") as f:
    story = f.read()

words = set()
start_of_word = -1

target_start = '<'
target_end = '>'

for i, char in enumerate(story):    # Here i == index value.

    if char == target_start:
        start_of_word = i
    
    if char == target_end and start_of_word != -1:   # Here i represent index value and char represent actual value
        word = story[start_of_word: i + 1]           # 0 to n-1
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input(f"Enter the answer {word}: ")
    answers[word] = answer
   
for word in words:
    story = story.replace(word, answers[word])

print(story)