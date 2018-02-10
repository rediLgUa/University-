from homework4.lesson5Inclass import *
import unittest

class NewClass(Employer):
    '''description'''
    def __init__(self, *args,**kwargs):
        Employer.__init__(self,*args,**kwargs)
        self.skills = []

    def increase_salary(self):
        self.salary*=2

    def add_skill(self, new_skill):
        self.skills.append(new_skill)

    def add_skills(self,*skills_list):
        #self.skills+=skills_list
        self.skills.extend(skills_list)

var = NewClass(salary=100)
var.increase_salary()

var.add_skill("Python")
var.add_skills('C++','test','c#',3)

print(var.skills)

print(var.salary)


