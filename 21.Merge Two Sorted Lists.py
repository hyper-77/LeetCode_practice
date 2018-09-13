import chaintable,random
def print_chain(temp): # given the head of chain ,then print the whole chain
    string = ''
    while not temp == None:
        string += str(temp.data) + ' '
        temp = temp._next
    print(string)

a=chaintable.ChainTable()
b=chaintable.ChainTable()

random1=[]
random2=[]
for i in range(random.randint(5,20)):
    random1.append(random.randint(1,50))

random1.sort()

for i in range(random.randint(5,15)):
    random2.append(random.randint(1,50))

random2.sort()

for k in random1:
    a.append(k)

for k in random2:
    b.append(k)


print(a)
print(b)

def mergeTwoSortedList(l1,l2):
    dummy=chaintable.Node(-1)
    cur=dummy
    while not l1 ==None and not l2==None:
        if l1.data<l2.data:
            cur._next=l1
            l1=l1._next
        else:
            cur._next=l2
            l2=l2._next
        cur=cur._next

    if l1==None:
        cur._next=l2
    else :
        cur._next=l1

    return dummy._next




print_chain(mergeTwoSortedList(a.head,b.head))
#---------------------------------------------------------------------------------------------------------------------------------------------
c=chaintable.ChainTable()
d=chaintable.ChainTable()

random1=[]
random2=[]
for i in range(random.randint(5,20)):
    random1.append(random.randint(1,50))

random1.sort()

for i in range(random.randint(5,15)):
    random2.append(random.randint(1,50))

random2.sort()

for k in random1:
    c.append(k)

for k in random2:
    d.append(k)


print(c)
print(d)


def mergeTwoSortedList_recur(l1,l2):
    if l1 == None:return l2
    if l2==None:return l1

    if l1.data<l2.data:
        l1._next=mergeTwoSortedList_recur(l1._next,l2)
        return l1
    else:
        l2._next = mergeTwoSortedList_recur(l1, l2._next)
        return l2


print_chain(mergeTwoSortedList_recur(c.head,d.head))
