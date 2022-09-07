#!/usr/bin/env python3

with open('test1.txt', 'r', encoding='utf-8') as f:
    listl = []
    for line in f:
        strip_lines = line.strip()
        listli = strip_lines.split()
        print(listli)
        m = listl.append(listli)
    print(listl)
