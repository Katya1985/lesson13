calls = 0


def count_calls():
    global calls


def string_info(string):
    global calls
    calls += 1
    for i in string_info:
        string_info = str
    return [len(string), string.upper, string.lower]


def is_contains(string, list_to_search):
    global calls
    for i in list_to_search:
        return string.lower() in i.lower()


print(string_info)
print(is_contains)
