# class Employee:
#     a = 1
#     def show(self):
#         print(f"The class attribute of a is {self.a}")

# e = Employee()
# e.a = 45
# e.show() // 45 will be printed


class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")


e = Employee()
e.a = 45
e.show()  # 1 will be printed because of classmethod
