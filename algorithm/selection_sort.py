#选择排序要素:
#以[2,4,3,7,5]为例
#1.总轮数=len(list)-1
#2.每轮次数=len(list)-1-index,但是应该写成range(i+1,n),
#第一次开始比较时是拿0索引的数和[1],[2],[3],[4]去比较
#时间复杂度:最多O(n²)，最少O(n)
list = [3,2,4,5,7]

def select_sort(my_list):
    n = len(my_list)
    for i in range(0,n-1):
        min_index = i
        count = 0
        for j in range(i+1,n):
            if my_list[min_index]>my_list[j]:
                min_index = j
        if min_index != i:
            count += 1
            my_list[min_index],my_list[i]= my_list[i],my_list[min_index]
        if count == 0:
            break
    return my_list




if __name__  == '__main__':
    result = select_sort(list)
    print(result)