import string


def count_words(sentence: str, n: int) -> list:
    if sentence is None:
        raise ValueError("sentence must not be null")

    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    words = set(sentence.split())

    counts = [(word, sentence.count(word)) for word in words]

    counts.sort(key=lambda word: (-word[1], word[0]))

    return counts[:n]
