def task_1() -> None:
    i: int = 30
    f: float = 2.23
    s: str = "Привет!"
    l: list = [1, 2, 3, 4, 5]
    b:bool = True
    print(type(i))
    print(type(f))
    print(type(s))
    print(type(l))
    print(type(b))

print (task_1())


def task_2(a=[1,2,3,5,8,13,21]):
    return a[0:3]
print (task_2())

def task_3(x):
    return x * x
print (task_3(4))