# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 15:11:22 2022

@author: 86185
"""

class Student(object):
    def __init__(self, stu_id, name, age, gender):
        self.stu_id = stu_id
        self.gender = gender
        self.name = name
        self.age = age
    def __str__(self):
        return f'学号:{self.stu_id}\n姓名:{self.name}性别:{self.gender}\n年龄:{self.age}'
        
    
stu = Student(1, "严", 19, '男')
print(stu)