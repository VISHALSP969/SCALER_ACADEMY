def unique(li):
    new=[]
    for i in li:
        if i not in new:
            new.append(i)
    return new

lst=[1,2,3,3,4,5,5,5,6,7,8,9]
r=unique(lst)
print(r)