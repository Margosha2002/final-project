def check_is_match(value, search_pattern):
    string_lower = str(value).lower()
    return string_lower.find(search_pattern.lower()) != -1
