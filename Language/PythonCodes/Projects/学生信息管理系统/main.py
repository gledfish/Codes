
stu_list = []
#定义列表保存学生信息
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

def insert_student():
    # 添加学生信息
    name = input('请输入你的姓名:')
    for stu in stu_list:
        if stu['name'] == name:
            print('学生信息存在')
            return
    age = input('请输入你的年龄:')
    age = int(age)
    gender = input('请输入性别:')

    stu_dict = {'name':name, 'age':age, 'gender':gender}
    stu_list.append(stu_dict)
    print('学生信息添加成功')


def show_students():
    # 显示学生信息
    if len(stu_list) > 0:       
        for student in stu_list:
            print(f'姓名:{student["name"]}\n,年龄:{student["age"]}\n,性别:{student["gender"]}')
    else:
        print('目前没有学生信息')

def remove_student():
    # 删除学生信息
    name = input('请输入你的姓名:')
    for stu in stu_list:
        if stu['name'] == name:
            print('学生信息存在')
            stu_list.remove(stu)
            break
    else:
        print('学生信息不存在，无法删除')


def modify_student():
    # 修改学生信息
    name = input('请输入你的姓名:')
    for stu in stu_list:
        if stu['name'] == name:
            print('学生信息存在')
            stu['age'] = int(input('请输入新的年龄'))
            break
    else:
        print('学生信息不存在，无法修改')


def search_student():
    name = input('请输入你的姓名:')
    for stu in stu_list:
        if stu['name'] == name:
            print('学生信息存在')
            break
    else:
        print('学生信息不存在，无法删除')
        
while True:
    show_menu()
    option = input('请输入操作编号')
    if option == '1':
        print('1.添加学生')
        insert_student()
    elif option == '2':
        print('2.删除学生')
        remove_student()
    elif option == '3':
        print('3.修改学生信息')
        modify_student()
    elif option == '4':
        print('4.查询单个学生信息')
        search_student()
    elif option == '5':
        # print('5.列出所有学生信息')
        show_students()
    elif option == '6':
        print('退出系统成功，欢迎下次使用')
        break
    else:
        print('输入有误，请重新输入')
        continue

    input('......回车键继续......')



