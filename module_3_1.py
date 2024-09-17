# Пухаева Алина Александровна
# Namespace
# 17.09.2024
# Notes: ctrl+alt+L

calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    return any(item.lower() == string for item in list_to_search)
print(string_info('December'))
print(string_info('January'))
print(string_info('Home'))
print(is_contains('Mathematics', ['Math', 'TheMatIcsMa', 'MaTHEMATICS']))
print(is_contains('jump', ['jumping', 'junk']))
print(is_contains('Homework', ['hw', 'home task', 'HW', 'home work']))
print(calls)