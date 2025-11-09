def count_words(content):
    split_content = content.split()
    return len(split_content)

def count_chars(text):
    char_dict = {}
    for char in text:
        lowered = char.lower()
        if not (lowered in char_dict):
            char_dict[lowered] = 1
            continue

        char_dict[lowered] += 1

    return char_dict

def sort_on(items):
    return items["num"]

def get_char_report(chars):
    char_list = []
    for key in chars:
        char_list.append({"char": key, "num": chars[key]})
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list