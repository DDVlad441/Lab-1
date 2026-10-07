def count_words(text):

    words = text.lower().split()
    counts = {}
    for word in words:

        word = word.strip(".,!?;:\"'()-—…«»")
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


text = input("Введіть текст: ")

word_counts = count_words(text)
print("Словник:", word_counts)

# список слів, що зустрічаються більше 3 разів
frequent_words = [word for word, count in word_counts.items() if count > 3]
print("Слова, що зустрічаються більше 3 разів:", frequent_words)