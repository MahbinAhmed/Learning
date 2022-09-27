# BUBBLE SORT (Inefficient) --->>>

def bubble_sort(list):
    for j in range(len(list)-1):
        swapped = False
        for i in range(len(list)-1-j):
            if list[i] > list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
                swapped = True
        if not swapped:
            break
#     return list

# INSERTION SORT (Inefficient) --->>>

def insertion_sort(list):
    for i in range(len(list)):
        element = list.pop(i)
        j = i-1
        while j >= 0 and list[j] > element:
            j -= 1
        list.insert(j+1,element)
    return list

# MERGE SORT (Efficient) --->>>
def merge(num1,num2):
    array = []
    i,j = 0,0
    while i < len(num1) and j < len(num2):
        if num1[i]<=num2[j]:
            array.append(num1[i])
            i += 1
        else:
            array.append(num2[j])
            j += 1
    first_list_tail = num1[i:]
    second_list_tail = num2[j:]
    return array+first_list_tail+second_list_tail
def merge_sort(list):
    if len(list) <= 1:
        return list
    mid_index = len(list)//2
    left_half = list[:mid_index]
    right_half = list[mid_index:]
    left_half_sorted = merge_sort(left_half)
    right_half_sorted = merge_sort(right_half)
    sorted_list = merge(left_half_sorted,right_half_sorted)
    return sorted_list

# QUICK SORT (Efficient) --->>>
def rearrenger(list,start=0,end=None):
    # if end is None:
    #     end = len(list)-1
    l,r = start,end-1
    while r>l:
        if list[l]<=list[end]:
            l += 1
        elif list[r]>=list[end]:
            r -= 1
        else:
            list[l],list[r]=list[r],list[l]
    if list[l]>list[end]:
        list[l],list[end]=list[end],list[l]
        return l
    # if list[r]>list[end]:
    #     list[r],list[end]=list[end],list[r]
    #     return r
    else:
        return end

def quick_sort(list,start=0,end=None):
    if end is None:
        end = len(list)-1
    if start<end:
        pivot = rearrenger(list,start,end)
        quick_sort(list,start,pivot-1)
        quick_sort(list,pivot+1,end)
    return list


test1 = [2, 6, 3, 4, 6, 2, 1]
test2 = [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]
test3 = [3, 5, 6, 8, 9, 10, 99]
test4 = [99, 10, 9, 8, 6, 5, 3]
test5 = [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]
test6 = []
test7 = [23]
test8 = [42, 42, 42, 42, 42, 42, 42]
test_list = [test1,test2,test3,test4,test5,test6,test7,test8]
# random.shuffle(test3)
# print(test3)
# print(bubble_sort(test3))
# print(insertion_sort(test1))
# print(merge_sort(test1))
# print(quick_sort(test1))
# for i in test_list:
    # print(bubble_sort(i))
    # print(insertion_sort(i))
    # print(merge_sort(i))
    # print(quick_sort(i))

class Notebook:
    def __init__(self,title,usernmae,likes) -> None:
        self.title = title
        self.username = usernmae
        self.likes = likes
    def __repr__(self) -> str:
        return f"Notebook <\"{self.title}\" : {self.username}>: {self.likes} likes"

def simple_compare(x,y):
    if x>y:
        return "lesser"
    elif x<y:
        return "greater"
    else:
        return "equal"

def merge(list1,list2,compare):
    array = []
    i,j = 0,0
    while i<len(list1) and j<len(list2):
        result = compare(list1[i],list2[j])
        if result=="lesser" or result=="equal":
            array.append(list1[i])
            i += 1
        else:
            array.append(list2[j])
            j += 1
    return array+list1[i:]+list2[j:]

def merge_sort(list,compare=simple_compare):
    if len(list)<=1:
        return list
    half_index = len(list)//2
    left_half = list[:half_index]
    right_half = list[half_index:]
    left_half_sorted = merge_sort(left_half,compare)
    right_half_sorted = merge_sort(right_half,compare)
    return merge(left_half_sorted,right_half_sorted,compare)


def compare_likes(obj1,obj2):
    if obj1.likes>obj2.likes:
        return "lesser"
    elif obj1.likes<obj2.likes:
        return "greater"
    elif obj1.likes==obj2.likes:
        return "equal"

def compare_title(obj1,obj2):
    if obj1.title>obj2.title:
        return "greater"
    elif obj1.title<obj2.title:
        return "lesser"
    else:
        return "equal"


nb0 = Notebook('pytorch-basics', 'aakashns', 373)
nb1 = Notebook('linear-regression', 'siddhant', 532)
nb2 = Notebook('logistic-regression', 'vikas', 31)
nb3 = Notebook('feedforward-nn', 'sonaksh', 94)
nb4 = Notebook('cifar10-cnn', 'biraj', 2)
nb5 = Notebook('cifar10-resnet', 'tanya', 29)
nb6 = Notebook('anime-gans', 'hemanth', 80)
nb7 = Notebook('python-fundamentals', 'vishal', 136)
nb8 = Notebook('python-functions', 'aakashns', 74)
nb9 = Notebook('python-numpy', 'siddhant', 92)

notebook_list = [nb0,nb1,nb2,nb3,nb4,nb5,nb6,nb7,nb8,nb9]
# for i in notebook_list:
#     print(i)
sorted_notebook_list = merge_sort(notebook_list,compare_title)
for i in sorted_notebook_list:
    print(i)