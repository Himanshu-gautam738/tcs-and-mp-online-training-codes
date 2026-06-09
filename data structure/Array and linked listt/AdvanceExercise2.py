def group_anagrams(words):
    result = {}
    for word in words:
        key = "".join(sorted(word))
        if key not in result:
            result[key] = []
        result[key].append(word)
    return list(result.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
