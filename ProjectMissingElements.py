def check_list(n, range_list):
    fullList = set(range(1, n + 1))

    return fullList-range_list

# Get two values from one input in form eg. [1,2,3,4] 10
range_list, n = input('Please enter the range list and N number:').split('],')

# Get string ['1','2','3','4','5'] and convert it to real list type, with int values
#range_list = range_list.strip('][').split(',')
#range_list = map(int,range_list)
#range_list = set(range_list)

# Short version
range_list = set(map(int, range_list.strip('][').split(',')))
# Cast n to int
n = int(n)

print(check_list(n, range_list))