#Python Program to Count Most Frequent Words in a File
words = []
with open("C:\\Comfy\\Technical\\Python\\Sample Python Code\\Generate Fibonacci Series.py", "r") as f:
    for line in f:
        words.extend(line.split())

from collections import Counter
counts = Counter(words)
top5 = counts.most_common(5)
print(top5)
