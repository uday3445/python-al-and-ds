def  update(l,i,v):
    """

    :param l: list of values
    :param i:  index
    :param v: value to replace
    :return:
    """
    if i>=0 and i<len(l):
        l[i]= v
        return True
    else:
        v=v+1
        return False


ns=[1,2,3,4,5]


z=8
print(update(ns,2,z))

print(update(ns,8,z))

print(update(ns,4,z))