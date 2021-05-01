def re(list):
    length = len(list)
    if length < 2:
        return [list]
    else:
        first = list[0]
        pivot = first
        answer = []
        for i in range(length):
            curr = list[i]
            if i == 0:
                answer += [curr]
            else:
                if curr < first:
                    # this num may have a chance of other subsets
                    re(list[i:])
                elif curr > pivot:
                    pivot = curr
                    answer += [curr]
        return answer

print(re([]))
print(re([1]))
print(re([1,2]))
print(re([2,1]))

print(re([2,1,3,4]))
# [2, 3, 4], [1, 3, 4]
# Only 1 has a chance because it starts with 2. Need to find numbers less than 2

print(re([2,1,5,3,4]))
# [2, 5], [2, 3, 4], [1, 3, 4]
# Need to save the first number and also a current pivot
