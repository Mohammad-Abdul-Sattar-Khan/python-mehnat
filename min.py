def min(num_list):
    min = 10000
    for i in num_list:
        if i < min:
            min = i

    print(f"The minimum number is {min}")

min([12,1,2,3,4,5,6,7,10,13])
min([3, 6, 1, 8, 2])
min([12, 45, 2, 67, 34, 89])