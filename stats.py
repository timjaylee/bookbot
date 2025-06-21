def word_count(file_contents):
    num_words = len(file_contents.split())
    return num_words

def char_count(file_contents):
    num_char = {}
    unique_char = set(file_contents.lower())
    for c in unique_char:
        num_char[c] = 0
    char_list = list(file_contents.lower())
    for c in char_list:
        num_char[c] += 1
    return num_char

def sort(dict):
    def sort_on(items):
        return items["num"]
    sorted_dict = []
    for c in dict:
        sorted_dict.append({"char" : c, "num" : dict[c]})
    sorted_dict.sort(reverse = True, key = sort_on)
    return sorted_dict