#!/usr/bin/python3
# author - rapheal owoyemi (@DesignerRapheal)
for i in range(ord('a'), ord('z') + 1):
    if chr(i) != 'e' and chr(i) != 'q':
        print('{:c}'.format(i), end='')
