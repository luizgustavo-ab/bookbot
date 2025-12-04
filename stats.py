def get_num_words(file_contents):
    count_words = file_contents.split()
    return len(count_words)

def count_letters(text):
    letters = {}
    text = text.lower()
    for char in text:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1 
    return letters

def sort_order(items):
    return items["num"]

def chars_dict_to_sorted_list(items):
    result = []
    for char in items:
        result.append({"char": char, "num": items[char]})
    
    result.sort(reverse=True, key=sort_order)

    return result