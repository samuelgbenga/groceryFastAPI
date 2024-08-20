def findSubstring(s, words):
    # 1 if empty return empty []
    if not s or not words:
        return []

    #2 get word length
    word_length = len(words[0])

    #3 total words
    total_words = len(words)

    #4 get total length of all words
    concat_length = word_length * total_words

    #5 init dictionary
    word_count = {}

    #6 Count frequency of each word in the words array
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    #7 init result list
    result_indices = []

    #8 Slide over the string s with windows of size concat_length
    for i in range(len(s) - concat_length + 1):

        #8.1 init seen words
        seen_words = {}

        # 8.1 loop through the total word
        for j in range(total_words):

            #8.1.1 Get the next word from the string
            word_index = i + j * word_length
            word = s[word_index:word_index + word_length]

            # 8.1.2 loop through the word count
            if word in word_count:
                # 8.1.2.1 increase the word count
                seen_words[word] = seen_words.get(word, 0) + 1


                # 8.1.2.1 If the word frequency exceeds the required frequency, break
                if seen_words[word] > word_count[word]:
                    break
            # 8.1.3 break
            else:
                break

        else:
        # 8.2 If all words matched, store the starting index
            result_indices.append(i)

    return result_indices

# Example 1
s1 = "barfoothefoobarman"
words1 = ["foo", "bar"]
print(findSubstring(s1, words1))  # Output: [0, 9]

# Example 2
s2 = "wordgoodgoodgoodbestword"
words2 = ["word", "good", "best", "word"]
print(findSubstring(s2, words2))  # Output: []

# Example 3
s3 = "barfoofoobarthefoobarman"
words3 = ["bar", "foo", "the"]
print(findSubstring(s3, words3))  # Output: [6, 9, 12]
