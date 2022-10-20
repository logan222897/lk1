# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# what is a function v method
# what is an argument v parameter
# what is a variable e.g string,date and integer and float

def method_lk(lk1,lk2):
    lk3=lk1+lk2
    print(lk3)
def function_lk(lk1,lk2):
    lk3 = lk1 + lk2
    return(lk3)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def merge_sort(sequence):
    """
    Sequence of numbers is taken as input, and is split into two halves, following which they are recursively sorted.
    """
    if len(sequence) < 2:
        return sequence

    mid = len(sequence) // 2     # note: 7//2 = 3, whereas 7/2 = 3.5

    left_sequence = merge_sort(sequence[:mid])
    print("Left:")
    print(left_sequence)
    right_sequence = merge_sort(sequence[mid:])
    print("Right:")
    print(right_sequence)


    print("Merge starting between:")
    print(left_sequence)
    print("and")
    print(right_sequence)
    return merge(left_sequence, right_sequence)

def merge2(left,right):
    print(left)
    print(right)
    result=[]
    i = j = 0
    cnt=0
    print ("---------")
    while i < len(left) and j < len(right):
        if left[i] < right[i]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        cnt += 1
        print(cnt)
        print (result)
        result += left[i:]
        result += right[j:]
        print("-------")
        print (result)

def merge(left, right):
    """
    Traverse both sorted sub-arrays (left and right), and populate the result array
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result


def binatointeger(binary):
  number = 0
  for b in binary:
    number = (2 * number) + b
  return number


def alevel_june2020():

    x =int(input("Enter an integer greater than 1: "))
    product = 1
    factor = 0
    while product < x:
        factor = factor+1
        product = product*factor

    if x == product:
        product = product+1
        for n in range(1,factor):
            product = product*n
            print(n)
    else:
        print("No Result!")

    '''

    OUTPUT "Enter an integer greater than 1: "
INPUT X
Product ← 1
Factor ← 0
WHILE Product < X
 Factor ← Factor + 1
 Product ← Product * Factor
ENDWHILE
IF X = Product THEN
 Product ← 1
 FOR N ← 1 TO Factor
 Product ← Product * N
 OUTPUT N
 ENDFOR
ELSE
 OUTPUT "No result"
ENDIF

    '''



if __name__ == '__main__':


 alevel_june2020()

'''
# Print the sorted list.
#print(merge_sort([5, 2, 6, 8, 5, 8, 1]))

 # print(merge_sort([5, 2, 6]))
#
#print(binatointeger('1011111'))

    x=100101010
    y = int(bin(x)[2:])
    y=
    print(y)


#print(merge2([5, 2, 6],[4,7,6]))


# Press the green button in the gutter to run the script.

    #print_hi('PyCharm')
#    method_lk(10,20)
#     result_from_function=function_lk(4,8)
#     result_from_function=result_from_function+1
#     print(result_from_function)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''
