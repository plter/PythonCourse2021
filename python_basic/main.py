# a = dict(name="陈云老师",age=20)
# a = {"name":"陈云"}
# print(a['name'])

# def hello(name, age):
#     print(f"Hello {name}, your age is {age}")
#
#
# hello(age=20,name="陈云老师")

# def add_numbers(a, b):
#     return a + b


# print(add_numbers(2, 3))


# def get_info():
#     return "Chen", 20
#
#
# name, age = get_info()
# print(name)


# data = (1, 2, 3, "Hello World")  # 元组
# print(data[0])


class A:
    def hello(self):
        print("Hello World")


a = A()
a.hello()


class B(A):
    pass


b = B()
b.hello()
