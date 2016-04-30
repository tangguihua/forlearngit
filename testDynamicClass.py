# -*- coding: utf-8 -*-
from types import MethodType
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May',\
'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
    
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
   
class Student1(object):
     __slots__ = ('name','age')  

class GraduatedStudent(Student1):
    pass
    
def testStudent():        
    def set_age(self,age):
            self.age = age 
    
    def set_score(self, score):
        self.score = score
    Student.set_score = set_score
    
    s = Student()
    s.name =  'Micheal'
    s.set_age = MethodType(set_age,s)
    s.set_age(25)
    print s.age
    s.set_score(100)
    print s.score
    
    s2 = Student()
    '''s2.set_age(25)
    s2.age'''       #this part will cause error
    s2.set_score(100)
    print s2.score
    
def testStudent1():
    s3 = Student1()
    s3.name = 'Tom'
    s3.age = 20
    s3.score = 90 #do not has the attribute 'score'

g = GraduatedStudent()
g.score = 99 
print g.score  