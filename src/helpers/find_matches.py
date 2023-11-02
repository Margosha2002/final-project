def find_matches_func(texts_list, text):
    trimed_text = text.strip()
    result = list()
    for cmd in texts_list:
        if cmd.startswith(trimed_text):
            result.append(cmd.lstrip(trimed_text))
    return result
