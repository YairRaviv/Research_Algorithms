
# ------------------------------------------------- Question 1 - safe call---------------------------------------------
from typing import Any
import collections


def safe_call(f ,**kwargs):
    annotations = f.__annotations__
    for k ,v in kwargs.items():
        # checks only the arguments that has an annotation in f definition ,
        # if the type of one of the arguments doesn't match to the corresponding annotation -> "safe_call" raising an Exception.
        if k in annotations and annotations[k] is not type(v):
            raise Exception("Wrong type!")
    # o.w -> calls f with kwargs
    return f(**kwargs)


# ------------------------------------------------- Question 2 - BFS --------------------------------------------------

def breadth_first_search(start:Any,end:Any,neghibor_function):
    # initalize help lists
    visited = []
    queue = []
    parents = {}

    visited.append(start)
    queue.append(start)
    # while the queue is not empty
    while queue:
        tmp = queue.pop(0)
        # iterate over tmp's neghibors
        for neghibor in neghibor_function(tmp):
            if neghibor == end:
                parents[neghibor] = tmp
                break
            if neghibor not in visited:
                parents[neghibor] = tmp
                visited.append(neghibor)
                queue.append(neghibor)
        #if we found path to "end" during the loop
        if end in parents.keys():
            break
    # if there is no way between start to end
    if end not in parents.keys():
        return []
    # restore the path between start t end
    tmp = end
    path = [end]
    while parents[tmp] != start:
        path.append(parents[tmp])
        tmp = parents[tmp]
    path.append(start)
    return path[::-1]


def four_neighbor_function(node:Any)->list:
    (x,y) = node
    return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]



# ---------------------------------------------------Question 3 - deep sorted-----------------------------------------

def print_sorted(lst:Any):
    print(rec_sort(lst))

def rec_sort(lst:Any):

    # different cases - dict or another structure
    if type(lst) is dict:
        for x in lst:
            # if one of the items is a structure - recursive call
            if type(lst[x]) in [list, tuple, dict, set]:
                lst[x] = rec_sort(lst[x])
        # finally sort the input structure
        return dict(sorted(lst.items()))
    for i,x in enumerate(lst):
        # if one of the items is a structure - recursive call
        if type(x) in [list , tuple , dict , set]:
            lst[i] = rec_sort(x)
    # finally sort the input structure
    if type(lst) is tuple:
        return tuple(sorted(lst,key=lambda x:str(x)))
    if type(lst) is set:
        return set(sorted(lst,key=lambda x:str(x)))
    return sorted(lst,key=lambda x:str(x))





# ----------------------------------------------------Question 4 - Coding game ---------------------------------------------
# link : https://www.codingame.com/ide/puzzle/the-descent


