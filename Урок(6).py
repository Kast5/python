Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Задание-1

with open('nginx_logs.txt', 'r', encoding="utf-8") as f:
    requests_list = []
    for line in f:
        remote_addr = line[:line.find(' ')]
        request_type = line[line.find('"') + 1:line.find('"') + 4]
        requested_resource = line[line.find('/d'):line.find('HTTP') - 1]
        tuple_requests = (remote_addr, request_type, requested_resource)
        requests_list.append(tuple_requests)
        print(tuple_requests)

# Задание-2

with open('nginx_logs.txt', 'r', encoding="utf-8") as f:
    remote_addr_list = [line[:line.find(' ')] for line in f]

addr_max = max(set(remote_addr_list), key=remote_addr_list.count)
print(addr_max, remote_addr_list.count(addr_max))

# Задание-3

from itertools import zip_longest
import json

with open('users.csv', 'r', encoding='utf-8') as name,\
        open('hobby.csv', 'r', encoding='utf-8') as hobby:
            names = name.read().splitlines()
            hobbys = hobby.read().splitlines()

if len(names) < len(hobbys):
    print(1)
else:
    users_hobby = dict(zip_longest(names, hobbys, fillvalue=None))
    print(users_hobby)
    with open('users_hobby_dict(3_задание).txt', 'w') as f:
        json.dump(users_hobby, f, ensure_ascii=False)

# Задание-4

from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as name, \
        open('hobby.csv', 'r', encoding='utf-8') as hobby:
    names = name.read().splitlines()
    hobbys = hobby.read().splitlines()

users_hobby_gen = ((names, hobbys) for names, hobbys in zip_longest(names, hobbys, fillvalue=None))

with open('users_hobby(4_задание).txt', 'w') as f:
    for user_hobby in users_hobby_gen:
        f.write(f'{user_hobby[0]}: {user_hobby[1]}\n')

# Задание-5

import sys

users, hobby, combined = sys.argv[1:]
if __name__== '_main_':
    from itertools import zip_longest
    with open(users, 'r', encoding='utf-8') as name, \
            open(hobby, 'r', encoding='utf-8') as hobby:
        names = name.read().splitlines()
        hobbys = hobby.read().splitlines()

    users_hobby_gen = ((names, hobbys) for names, hobbys in zip_longest(names, hobbys, fillvalue=None))

    with open(combined, 'w') as f:
        for user_hobby in users_hobby_gen:
            f.write(f'{user_hobby[0]}: {user_hobby[1]}\n')
    exit()

# Задание-6

import sys

if __name__== '_main_':
    interval = list(map(int, sys.argv[1:]))
    with open('bakery.csv') as f:
        text = f.readlines()
        if len(interval) == 2:
            for line in text[interval[0] - 1:interval[1]]:
                print(line.strip())
        elif len(interval) == 1:
            for line in text[interval[0] - 1:]:
                print(line.strip())
        else:
            for line in text:
                print(line.strip())
    exit()

# Задание-7

import sys

with open('sales.txt', 'r+', encoding='utf-8') as f:
    values = (value for value in f.readlines())
    count_strings = int(sys.argv[1])
    cursor_place = 0
    for value in values:
        if count_strings == 1:
            f.seek(cursor_place)
            f.writelines(sys.argv[2])
            break
        else:
            cursor_place += len(value)
            count_strings -= 1
            continue
    if count_strings > 1:
        print('Такой строчки не существует')