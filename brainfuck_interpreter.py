#!/usr/bin/env python2
'''
One of my maths lecturers at Bristol University set us a task to answer what
is the sequence:
>+++++[<++>-]<+++ >++++[>+++<-]>[<++++>-] 
<.+< . >. < . >-> >
+++++>+< [ >[> >+>+< < <-] > > >[< < <+> > >-]< < < >[<+>-]
< < < <[>+> > > > >+< < < < < <-] >[<+>-] > >
[< <+> > > > >+< < <-] < <[> >+< <-]> > > > >.[-] 
< < < < < < < .  > > > > > > [<+>-]< < <-]
begining of.
Being a computer scientist i didn't bother to do it by hand and wrote the 
interpreter instead.

It is however missing the input ',' command.
'''

__author__ = "Adomas Venčkauskas"
__date__ = "2014-02"

import sys
import re



class BrainfuckInterpreter(object):
    commands = {
        '>': 'next',
        '<': 'prev',
        '+': 'inc',
        '-': 'dec',
        '[': 'jnz',
        ']': 'ctz',
        '.': 'prt',
    }

    def __init__(self, code, memsize=20):
        self.code = code
        self.memory = [0] * memsize
        self.mem_ptr = 0
        self.ptr = 0

    def next(self):
        self.mem_ptr += 1

    def prev(self):
        self.mem_ptr -= 1

    def inc(self):
        self.memory[self.mem_ptr] += 1

    def dec(self):
        self.memory[self.mem_ptr] -= 1

    def jnz(self):
        brackCount = 0
        if(self.memory[self.mem_ptr] == 0):
            self.ptr += 1
            while(self.code[self.ptr] != ']' or brackCount != 0):
                if(self.code[self.ptr] == '['): brackCount -= 1
                elif(self.code[self.ptr] == ']'): brackCount += 1
                self.ptr += 1

    def ctz(self):
        brackCount = 0
        if(self.memory[self.mem_ptr] != 0):
            self.ptr -= 1
            while(self.code[self.ptr] != '[' or brackCount != 0):
                if(self.code[self.ptr] == '['): brackCount += 1
                elif(self.code[self.ptr] == ']'): brackCount -= 1
                self.ptr -= 1

    def prt(self):
        # print self.memory[self.mem_ptr]
        print chr(self.memory[self.mem_ptr])

    def interpret(self):
        while self.ptr < len(self.code):
            c = self.code[self.ptr]
            if(not re.match('[ \t\n]', c)): 
                method = getattr(self, BrainfuckInterpreter.commands[c])
                method()
            self.ptr += 1

if __name__ == '__main__':
    if(len(sys.argv) > 2): 
        interpreter = BrainfuckInterpreter(sys.argv[1], sys.argv[2])
    else:
        interpreter = BrainfuckInterpreter(sys.argv[1])
    interpreter.interpret()
