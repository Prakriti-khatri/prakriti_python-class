from collections import Counter
text="""
python is an amazing programming language.python is fun to learn and powerful to use.
"""
words=text.lower().split()
words_count =Counter(words)
print("word frequencies")
for word,count in words_count.items():
    print(f"{word}:{count}")

from queue import Queue
task_queue =Queue()
tasks=["task 1:clean the room","task 2:write python code","task 3: read a book"]
for task in tasks:
    task_queue.put(task)
    print("processing tasks")
    while not task_queue.empty():
        print(task_queue.get())

from collections import deque
import random
deck =deque([f"{value}of{suit}"for value in["2","3","4","5","6","7","8","9","10","jack","Queen","king","Ace"]for suit in["hearts","diamonds","clubs","spades"]])
random.shuffle(deck)
player1=[]
player2=[]
for _ in range(3):
 player1.append(deck.popleft())
 player2.append(deck.popleft())
print("player 1's hand")
print(player1)
print("\nplayer 2's hand")
print(player2)

