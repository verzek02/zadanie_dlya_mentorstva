def find_max_word(text):
    words = text.split()
    word_points = {}
    for i in words:
        word_points[i] = word_points.get(i, 0) + 1
    max_word = max(word_points, key=word_points.get)

    return max_word


text = input('Введите предложение:')
result = find_max_word(text)
print("Наиболее часто встречающееся слово:", result)



