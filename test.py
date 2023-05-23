import unittest
from function import count_words


class TestCountWords(unittest.TestCase):
    def test_count_words(self):
        sentence = "baz bar foo foo zblah zblah zblah baz toto bar"
        size = 3

        expected = [
            ("zblah", 3),
            ("bar", 2),
            ("baz", 2),
        ]
        output = count_words(sentence, size)

        self.assertEqual(expected, output)

    def test_count_words_with_empty_sentence(self):
        sentence = ""
        size = 2

        expected = []
        output = count_words(sentence, size)

        self.assertEqual(expected, output)

    def test_count_words_with_size_greater_then_result_number(self):
        sentence = "foo bar foo baz"
        size = 10

        expected = [("foo", 2), ("bar", 1), ("baz", 1)]
        output = count_words(sentence, size)

        self.assertEqual(expected, output)

    def test_count_words_with_punctuation(self):
        sentence = "aaz foo aaz bar."
        size = 2

        expected = [("aaz", 2), ("bar", 1)]
        output = count_words(sentence, size)

        self.assertEqual(expected, output)

    def test_count_words_with_none_value(self):
        sentence = None
        size = 2

        self.assertRaises(ValueError, lambda: count_words(sentence, size))

    def test_count_words_with_same_number(self):
        sentence = "foo bar pop"
        size = 3

        expected = [("bar", 1), ("foo", 1), ("pop", 1)]
        output = count_words(sentence, size)

        self.assertEqual(expected, output)

    def test_count_words_when_size_is_zero(self):
        sentence = "arv arv foo deb"
        size = 0

        expected = []
        output = count_words(sentence, size)

        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
