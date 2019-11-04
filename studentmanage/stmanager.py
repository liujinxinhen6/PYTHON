a ='''
********************************
---
欢迎来到学生管理系统v1.0!
1.新建学生信息
2.显示学生信息
3.查询学生信息
4.删除学生信息
5.修改学生信息


0.退出系统
---
********************************
'''
students = [
    {
        'name:':'张三',
        'age:':'19',
        'chinese':'67',
        'math':'78'
    },
{
        'name:':'李四',
        'age:':'18',
        'chinese':'77',
        'math':'88'
    }

]
while True:
    # 程序主循环
    print(a)
    action = input("请输入操作: ")

    if action == "0":
        print("欢迎下次再来!")
        break
    elif action == "1":
        print("新建学生信息")
        name = input('请输入学生姓名: ')
        age = input('请输入学生年龄: ')
        chinese = input('前输入该学生语文成绩: ')
        math = input('请输入该学生数学成绩: ')
        student = {
            'name': name,
            'age': age,
            'chinese': chinese,
            'math': math

        }
        students.append(student)

    elif action == '2':
        print("显示学生信息")
        for student in students:
            print(student)
    elif action == '3':
        print("查询学生信息")
        name = input('请输入学生姓名: ')
        for student in students:
            if student['name'] == name:
                print(student)
        else:
            print('{}学生不存在!请重新输入!'.format(name))


    elif action == "4":
        print("删除学生信息")
    elif action == '5':
        print("修改学生信息")
    else:
        print("输入无效命令!请输入1-5!")