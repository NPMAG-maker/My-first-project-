def word_counter(word_receptor):
        words = word_receptor.split()
        return len(words)


def count_characters(text):
    counts = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in counts:
            counts[lower_char] += 1
        else:
            counts[lower_char] = 1
    return counts




def sort_characters(counts_dict):
    result = []
    for char, num in counts_dict.items():
        result.append({"char": char, "num": num})
    result.sort(key=sort_on, reverse=True)
    return result

def sort_on(item):
    return item["num"]




