def outer_fun(fun):
    def inner_fun(x,y):
        x=x+10
        y=y+10

        return fun(x,y)
        print("main function call")
    return inner_fun
@outer_fun #decorator----
def main_fun(x,y):
    return x+y
x=main_fun(5,6)
print(x)
# --------------------------------------
# var1=outer_fun(main_fun)
# var2=var1(5,5)
# print(var2)