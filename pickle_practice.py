# -*- coding: utf-8 -*-
import pickle


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Person {name: %s, age: %d}' % (self.name, self.age)


p1 = Person('홍길동', 23)

with open('person.pickle', 'wb') as f:
    pickle.dump(p1, f)  # 파일로 저장함
print(p1)  # Person {name: 홍길동, age: 23}

with open('person.pickle', 'rb') as f:
    p2 = pickle.load(f)  # 파일에서 읽어옴
print(p2)  # Person {name: 홍길동, age: 23}