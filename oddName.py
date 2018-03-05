def main():
    user_name = input("please input your name: \n")
    while len(user_name) == 0:
        print("Name cannot be left blank.")
        user_name = input("please input your name: \n")
    for i in range(len(user_name)):
        # num = i % 2
        # if num == 1:
        if i % 2 == 1:
            print(user_name[i])

main()