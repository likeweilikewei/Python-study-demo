#! /usr/bin/env python
# -*- coding=utf-8 -*-


class Word(str):

    def __eq__(self, other):
        return len(self) == len(other)

    def __like(self):
        print('like')

w1 = Word('likesss')
print(w1)
print(type(str(1)))
print(type(Word(1)))
print(Word(1))
print(Word([1,2]))
print(Word('abcd')[2])
w2 = Word('wewe')
print('{} = {}? {}'.format(w1,w2,w1==w2))
print(str,type(str))
print(Word,type(Word))
print(Word.__dict__)
print(Word.__name__)
w1._Word__like()
