# You can assume that list is a list of DISTINCT integers
# See comments below for the expected outputs

def all(list):
    length = len(list)
    if length == 0:
        return [[]]
    else:
        answer = []

        minimum = list[0]
        pivot = minimum
        for i in range(length):
            curr = list[i]
            if i == 0:
                answer += subset(list)
            elif curr <= minimum:
                    minimum = curr
                    # less than the first number but also a larger number before
                    # 4, 1, 3, 8 -> only 1 should go deeper but 3 shouldn't because 1 is before
                    answer += subset(list[i:])
        return answer

def subset(list):
    """
    Get all subsets of the first number
    """
    answer = []
    if len(list) > 0:
        head = list[0]
        larger = [x for x in list if x > head]
        if len(larger) > 0:
            minimum = larger[0]
            for i in range(len(larger)):
                curr = larger[i]
                if i == 0 or curr < minimum:
                    answer += [[head] + greater(larger[i:])]
                    minimum = curr
        else:
            answer += [[head]]
        return answer
            
def greater(list):
    """
    Get all numbers greater than the pivot which starts with the first number.
    It keeps increasing to the current max number.
    """
    pivot = list[0]
    answer = [pivot]
    for x in list:
        if x > pivot:
            answer += [x]
            pivot = x
    return answer

print(subset([3,2,1]))
print(subset([2,1,5,3,4,10,8,6,7]))
# [2, 5, 10], [2, 5, 8], [2, 5, 6, 7], [2, 3, 4, 10], [2, 3, 4, 8], [2, 3, 4, 6, 7]
print(all([2,1,5,3,4,10,8,6,7]))

print(all([]))
print(all([1]))
print(all([1,2]))
print(all([2,1]))

print(all([3, 2, 1]))
# [3], [2], [1]

print(all([2,1,3,4]))
# [2, 3, 4], [1, 3, 4]
# Only 1 has a chance because it starts with 2. Need to find numbers less than 2

print(all([2,1,5,3]))
# [2, 5], [2, 3], [1, 5], [1, 3]

print(all([2,1,5,3,4]))
# [2, 5], [2, 3, 4], [1, 5], [1, 3, 4]
# Need to save the first number and also a current pivot

print(all([4, 7, 6, 1, 3, 5, 8, 2]))
# [4, 7, 8], [4, 6, 8], [4, 5, 8], [1, 3, 5, 8], [1, 2]

print(all([3, 4, 6, 10, 2, 7, 1, 5, 8, 9]))
# [3, 4, 6, 10], [3, 4, 6, 7, 8, 9], [3, 4, 5, 8, 9], 
# [2, 7, 8, 9], [2, 5, 8, 9], [1, 5, 8, 9]
