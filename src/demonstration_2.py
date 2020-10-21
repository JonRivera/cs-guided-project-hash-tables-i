"""
You've uncovered a secret alien language. To your surpise, the language is made
up of all English lowercase letters. However, the alphabet is possibly in a
different order (but is some permutation of English lowercase letters).

You need to write a function that, given a sequence of words written in this
secret language, and the order the alphabet, will determine if the given words
are sorted "alphabetically" in this secret language.

The function will return a boolean value, true if the given words are sorted
"alphabetically" (based on the supplied alphabet), and false if they are not
sorted "alphabetically".

Example 1:

```plaintext
Input: words = ["lambda","school"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'l' comes before 's' in this language, then the sequence is
sorted.
```

Example 2:

```plaintext
Input: words = ["were","where","yellow"], order = "habcdefgijklmnopqrstuvwxyz"
Output: false
Explanation: As 'e' comes after 'h' in this language, then words[0] > words[1],
hence the sequence is unsorted.
```

Example 3:

```plaintext
Input: words = ["lambda","lamb"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first four characters "lamb" match, and the second string is
shorter (in size.) According to lexicographical rules "lambda" > "lamb",
because 'd' > '∅', where '∅' is defined as the blank character which is less
than any other character (https://en.wikipedia.org/wiki/Lexicographic_order).
```


Notes:

- order.length == 26
- All characters in words[i] and order are English lowercase letters.
"""

# were given words in a list
# were give an order based on an alphabet
# detemine if the words are sorted based on alphabet

#plan
# create has map of the alphabet assign each word a number
# create a for loop over two words
#



def are_words_sorted(words, alpha_order):
    """
    Inputs:
    words: List[str]
    alpha_order: str

    Output:
    bool
    """
    # Your code here

    dict1 = {}
    for index, char in enumerate(words):
        dict1[char] = index
    for word in words:
        for index, char in enumerate(word):
            if index+1<len(word) and dict1[word[index]] < dict1[word[index+1]]:
                continue
            else:
                return False
    return


def isAlienSorted(self, words, order):
    order_index = {c: i for i, c in enumerate(order)}

    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]

        # Find the first difference word1[k] != word2[k].
        for k in xrange(min(len(word1), len(word2))):
            # If they compare badly, it's not sorted.
            if word1[k] != word2[k]:
                if order_index[word1[k]] > order_index[word2[k]]:
                    return False
                break
        else:
            # If we didn't find a first difference, the
            # words are like ("app", "apple").
            if len(word1) > len(word2):
                return False

    return True



