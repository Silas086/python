list = [88,423,34,1,5,999]

def insert_sort(my_list):
    n = len(my_list)
    for i in range(1,n):
        for j in range(i,0,-1):
            if my_list[j] < my_list[j-1]:
                my_list[j],my_list[j-1] = my_list[j-1],my_list[j]
            else:
                break
    return my_list
if __name__ == '__main__':
    result = insert_sort(list)
    print(result)
