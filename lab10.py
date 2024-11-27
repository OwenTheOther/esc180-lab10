##Problem 1

# part a:
#base case is power(x, 0) = 1 for any x
#therefore for non-negative n, power(x, n) = x*power(x, n-1)

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

#part 3: call tree for power(2, 3)

# power(2, 0)
#         \
#         /1
# power(2, 1)
#         \
#         /1*2
# power(2, 2)
#         \
#         /1*2*2
# power(2, 3)
#         \
#          \1*2*2*2

##Problem 2
def sum_digits(str):
    if len(str) == 0:
        return 0
    else:
        return int(str[0]) + sum_digits(str[1:])


#problem 3
def split_list(L, S):
    ret = [[]]
    split_num = 0
    for i in L:
        if i in S:
            split_num += 1
            ret.append([])
        else:
            ret[split_num].append(i)
    return ret




if __name__ == "__main__":
    print(power(2, 3))
    print(sum_digits("123"))
    print(split_list([1, 2, 6, 4, 5, 3, 7], [3, 6])) 


        

