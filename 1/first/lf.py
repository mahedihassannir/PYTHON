# nameList = ['Harsh', 'Pratik', 'Bob', 'Dhruv']
# print (nameList[1][-1])


# Allah = True
# MSW = True
# Ibrahim=True

# if Allah and MSW == True and Ibrahim==True :
#     print("Allah Akbar")


# count = 0

# while count < 3:
#     count += 1
#     print(count)


# def func():
#     global s
#     s += "he he he "
#     print(s)

# s = "Python is super easy"
# func()


# def func():
#     pass


# items = ["Allah", "Mohammed (SW)", "Azrail"]
# items = {"name": "mahedi", "age": 17}


# args and kwargs


# def every_one(*args):
#     for items in args:
#         print(items)


# persons = ["Mahedi", "PY", "JS THE KING"]
# every_one(*persons)


# make closure func


def func1():
    a = 10

    def func2():
        return a

    return func2


closure = func1()
result = closure()
print(result)
