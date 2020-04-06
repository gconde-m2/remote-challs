from argparse import ArgumentParser
import sys
import os

morse = {
'a': '-',
'b':'-...', 
'c':'-.-.', 
'd':'-..', 
'e':'.', 
'f':'..-.', 
'g':'--.', 
'h':'....', 
'i':'..', 
'j':'.---', 
'k':'-.-', 
'l':'.-..', 
'm':'--', 
'n':'-.', 
'o':'---', 
'p':'.--.', 
'q':'--.-', 
'r':'.-.', 
's':'...', 
't':'-', 
'u':'..-', 
'v':'...-', 
'w':'.--', 
'x':'-..-', 
'y':'-.--', 
'z':'--..',
' ':' '
}

str = ''
i = 0;
y = 0;
if len(sys.argv) != 2 or not sys.argv[1]:
    print("<a-zA-Z string>")
    exit()
else :
    while i < len(sys.argv[1]):
        if sys.argv[1][i] in morse:
            y = 1
        else:
            y = 0
            break
        i = i + 1
    if y == 1:
        msg = sys.argv[1]
        for char in msg:
            str = str + (morse[char])
        print(str)
        exit()
    else:
        print("<a-zA-Z string>")
        exit()