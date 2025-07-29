# class Calculator:
#     number1=200
#     def add(self,a,b):
#         print("ok")
#         self.number1=a
#         self.number2=b
#         self.sum=a+b
#
# obj=Calculator()
#
# print(obj.add(8,9))

#practice

#create student class that takes name ,marks of 3 subjects as arguments in constructor.then create a method to print the average


class Student:
    def __init__(self,name,sub1,sub2,sub3):
        self.name=name

        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
    def avg(self):
        print("avg is :",(sub1+sub2+sub3)/3)
obj1=Student("amar",Student.avg)
print(obj1)
obj2=Student("Omkar",Student.avg)
print(obj2)




