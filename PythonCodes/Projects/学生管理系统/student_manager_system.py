# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 15:11:35 2022

@author: 86185
"""

import student

class StudentManagerSystem(object):
    def __init__(self):
        self.stu_dicts = {}
    @staticmethod
    def show_menu() :
        # 显示菜单
        print('*' * 9)
        print('1.添加学生')
        print('2.删除学生')
        print('3.修改学生信息')
        print('4.查询学生信息')
        print('5.列出所有学生信息')
        print('6.退出系统')
        print('*' * 9)
    def remove_student(self):
        stu_id = input('请输入学号')
        if stu_id in self.stu_dicts:
            del self.stu_dicts[stu_id]
            print('学生已经删除')
        else:
            print('学生信息不存在，无法删除...')
    def modify_student(self):
        stu_id = input('请输入学号')
        if stu_id in self.stu_dicts:
            stu = self.stu_dicts[stu_id]
            stu.age = input('请输入新的年龄')
            print('信息修改完毕')
        else:
            print('学生信息不存在')
    def search_student(self):
        stu_id = input('请输入学号')
        if stu_id in self.stu_dicts:
            stu = self.stu_dicts[stu_id]
            print(stu)
        else:
            print(stu)
    def save(self):
        f = open('student.txt', 'w', encoding = 'utf-8')
        for stu in self.stu_dicts.values():
            f.write(str(stu) + '\n')
        f.close()
        
    
    def insert_student(self):
        stu_id = input('请输入学号:')
        if stu_id in self.stu_dicts:
            print('学生信息已经存在')
            return
        name = input('请输入姓名:')
        age = input('请输入年龄:')
        gender = input('请输入性别:')
        stu = student.Student(stu_id, name, age, gender)
        self.stu_dicts[stu_id] = stu 
        
    def show_all_info(self):
        for stu in self.stu_dicts.values():
            print(stu)
    def load_info(self):
        f = open('student.txt', 'r', encoding = 'utf-8')
        buf_list = f.readlines()
        for buf in buf_list:
            buf = buf.strip()
            info_list = buf.split(',')
            stu = student.Student(*info_list)
            stu_id = info_list[0]
            self.stu_dicts[stu_id] = stu
        f.close()
            
    def start(self):
        self.load_info()
        while True:
            self.show_menu()
            option = input('请输入操作编号')
            if option == '1':
                print('1.添加学生')
                self.insert_student()
            elif option == '2':
                print('2.删除学生')
                self.remove_student()
            elif option == '3':
                print('3.修改学生信息')
                self.modify_student()
            elif option == '4':
                print('4.查询单个学生信息')
                self.search_student()
            elif option == '5':
            # print('5.列出所有学生信息')
                self.show_all_info()
            elif option == '6':
                self.save()
                print('退出系统成功，欢迎下次使用')
                break
            else:
                print('输入有误，请重新输入')
                continue

        input('......回车键继续......')
        
    
