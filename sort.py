# use to check if the array is sorted
def is_sorted(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False
    # print(ls)
    return True


def insertion_sort(li):
    # implement your algorithm here
    j = 0
    for i in range(1,len(li)-1):
        j = i
        # print(j)
        while j > 0:
            if li[j] < li[j-1]:
                li[j-1], li[j] = li[j], li[j-1]
                j -= 1
            else: 
                j -= 1
        # print(li)

# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4, 41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

insertion_sort(li)
# should return True, because insertion sort is an in-place sort
print(is_sorted(li))
