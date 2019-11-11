#面向对象
#类、对象
class Student():
    sum = 0
    name = 'qiyue'
    age = 0        #类变量
    def __init__(self,name,age):#self可以换成任意其他字符
        self.name = name
        self.age = age #self。实例变量 赋初值
        print(self.name)
        print(name)
        #print('student')

    def do_homework(self):
        print('do homework')




student1 = Student('liujinxin',18)
# student2 = Student('sdjh',28)
# print(student1.name + str(student1.age))
# print(student2.name + str(student2.age))
# print(Student.name)
# print(Student.age)





