data_type = input()

if data_type == "int":
    a = int(input())
    b = int(input())
    if a == 0 and b == 0:
        print("Empty Ints")
    else:
        print(a + b)

elif data_type == "str":
    s = input()
    if not s:
        print("Empty String")
    else:
        print(s)

elif data_type == "list":
    lst_input = input()
    lst = lst_input.split()
    if not lst:
        print("Empty List")
    else:
        print(lst[-1])

else:
    print("Unknown type")
