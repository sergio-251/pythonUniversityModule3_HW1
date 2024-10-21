# Пространство имён

def count_calls():
    global calls
    calls += 1

def string_info(s: str):
    count_calls()
    return len(s), s.upper(), s.lower()

def is_contains(s: str, lst: list):
    count_calls()
    return s.lower() in (item.lower() for item in lst)

calls = 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)