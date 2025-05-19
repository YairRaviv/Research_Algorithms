import re
import sys



# ----------------------------------------------------------------------- Question 1 ------------------------------------------------------------------------------------- 
def create_mails():
    f = open("mails.txt", "a")
    f.write("yai-rra@checkpoint.com\nyai-rra@checkpoint.com.\nyairav..iv@walla.com\n.yair@gmail.com\nsss@gmail..com\ng yai--rav.iv@walla.com")
    f.close()

def MailAddresses(file):
    """
    apply this function on mails.txt file should print:
    "Valid addesses:
    [yai-rra@checkpoint.com]

    InValid addesses:
    [yai-rra@checkpoint.com.
    yairav..iv@walla.com
    .yair@gmail.com
    sss@gmail..com
    g yai--rav.iv@walla.com]"
    """
    f = open(file, "r")
    # find all mail address
    emails = set(re.findall(r"[a-zA-Z0-9\._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9\._-]+", f.read()))
    valid = set()
    invalid = set()
    # filter the invalid mail addresses from all the addresses
    for w in emails:
        if w[0] in ['.' , '_' , '-'] or w[len(w)-1] in ['.' , '_' , '-']:
            invalid.add(w)
            continue
        else:
            for i in range(len(w) -1):
                if w[i] in ['.' , '_' , '-'] and w[i+1] in ['.' , '_' , '-']:
                    invalid.add(w)
                    break
        #append the valid addresses to the valid list
        if w not in invalid:
            valid.add(w)
    print("Valid addesses:\n",list(valid),"\n\n","InValid addesses:\n",list(invalid))


# ----------------------------------------------------------------------- Question 2 -------------------------------------------------------------------------------------

def last_call(f):
    """
    >>> f(2)
    4
    >>> f(2)
    'I already told you that the answer is 4'
    >>> f(5)
    25
    >>> f(2)
    'I already told you that the answer is 4'
    """
    def bar(arg, prev=[]):
        if arg in prev:
            return "I already told you that the answer is " + str(f(arg))
        else:
            prev.append(arg)
            return(f(arg))
    return bar

@last_call
def f(arg):
    return arg ** 2



# ----------------------------------------------------------------------- Question 3 -------------------------------------------------------------------------------------
class List(list):
    def __getitem__(self, item):
        """
        override the [] operator to return the desire value for the special syntax
        >>>print(List([1,2,3])[0])
        1
        >>>print(List([[0,0],[1,1]])[0,0])
        0
        >>>print(List([[0,0],[1,1],[4,4,4,4]])[2,1])
        4
        >>>print(List([[[1, 2, 3, 33], [4, 5, 6, 66]],[[7, 8, 9, 99], [10, 11, 12, 122]],[[13, 14, 15, 155], [16, 17, 18, 188]],])[0,1,3])
        66
        """
        lst = list(self)
        # check if the list dimention is 1
        if type(item) is int:
            return lst[item]
        dim = len(tuple(item))
        if dim == 0:
            return None
        tmp = lst[item[0]]
        for i in range(1,dim):
            tmp = tmp[item[i]]
        return tmp


# ----------------------------------------------------------------------- Question 4 -------------------------------------------------------------------------------------

#  link for 4 : https://www.codingame.com/ide/puzzle/there-is-no-spoon-episode-1


if __name__ == '__main__':
    import doctest
    create_mails()
    print(doctest.testmod())



