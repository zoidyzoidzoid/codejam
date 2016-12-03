#!/usr/bin/env python3

n = int(input())

pad = {
    'a': '2',
    'b': '22',
    'c': '222',
    'd': '3',
    'e': '33',
    'f': '333',
    'g': '4',
    'h': '44',
    'i': '444',
    'j': '5',
    'k': '55',
    'l': '555',
    'm': '6',
    'n': '66',
    'o': '666',
    'p': '7',
    'q': '77',
    'r': '777',
    's': '7777',
    't': '8',
    'u': '88',
    'v': '888',
    'w': '9',
    'x': '99',
    'y': '999',
    'z': '9999',
    ' ': '0'
}

for case in range(n):
    x = input()
    result = ''
    last_char = 0

    for char in x:
        if char not in pad:
            raise Exception('wat: {}'.format(char))

        if pad[char][0] == last_char:
            result += ' '

        result += pad[char]

        last_char = result[-1]

    print('Case #{}: {}'.format(case + 1, result))

