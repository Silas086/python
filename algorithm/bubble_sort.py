#冒泡排序要素:
#1.总轮数=len(list)-1
#2.每轮次数+索引=len(list)-1
#时间复杂度:最多O(n²)，最少O(n)
list = [3,2,4,5,7]
def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n-1):
        count = 0
        for j in range(n-1-i):
            if my_list[j]>my_list[j+1]:
                count += 1
                my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
        if count == 0:
            break
    return my_list

if __name__  == '__main__':
    result = bubble_sort(list)
    print(result)