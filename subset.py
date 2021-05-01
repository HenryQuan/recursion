# You can assume that list is a list of DISTINCT integers
# See comments below for the expected outputs

def re(list):
    length = len(list)
    if length < 2:
        return [list]
    else:
        answer = []
        extra = []

        first = list[0]
        pivot = first
        for i in range(length):
            curr = list[i]
            if i == 0:
                answer += [curr]
            else:
                if curr <= first:
                    # potential subsets, go deeper
                    extra += re(list[i:])
                elif curr > pivot:
                    pivot = curr
                    re(list[i:])
                    answer += [curr]
        return [answer] + extra

print(re([]))
print(re([1]))
print(re([1,2]))
print(re([2,1]))

print(re([3, 2, 1]))
# [3], [2], [1]


print(re([2,1,3,4]))
# [2, 3, 4], [1, 3, 4]
# Only 1 has a chance because it starts with 2. Need to find numbers less than 2

print(re([2,1,5,3,4]))
# [2, 5], [2, 3, 4], [1, 5], [1, 3, 4]
# Need to save the first number and also a current pivot

print(re([4, 7, 6, 1, 3, 5, 8, 2]))
# [4, 7, 8], [4, 6, 8], [4, 5, 8], [1, 3, 5, 8], [1, 2]

print(re([3, 4, 6, 10, 2, 7, 1, 5, 8, 9]))
# [3, 4, 6, 10], [3, 4, 6, 7, 8, 9], [3, 4, 5, 8, 9], 
# [2, 7, 8, 9], [2, 5, 8, 9], [1, 5, 8, 9]
