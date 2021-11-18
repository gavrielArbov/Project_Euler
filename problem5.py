# Smallest multiple

number = 400000000
list = []
while number > 20:
    flag = True
    for i in range(11, 21):
        if number % i != 0:
            flag = False
    if flag == True:
        list.append(number)
    number -= 10
    flag = True



print(list)

