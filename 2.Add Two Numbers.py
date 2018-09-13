import chaintable

a=chaintable.ChainTable()
b=chaintable.ChainTable()

for i in range(3):
    a.append(i)
    b.append(i+6)

a.append(4)
b.append(9)
b.append(3)
print(a)
print(b)


def addTwoNumber(n1,n2):
    dummy=chaintable.Node(-1)
    cur=dummy

    carry=0
    while(not n1==None and not n2==None):
        digit=(n1.data+n2.data+carry)%10
        carry=(n1.data+n2.data+carry)//10
        n1=n1._next
        n2=n2._next

        cur._next=chaintable.Node(digit)

        cur=cur._next


    while (not n1==None):
        digit = (n1.data  + carry) % 10
        carry = (n1.data  + carry) // 10
        n1 = n1._next

        cur._next= chaintable.Node(digit)

        cur = cur._next

    while (not n2 == None):
        digit = (n2.data + carry) % 10
        carry = (n2.data + carry) // 10
        n2 = n2._next

        cur._next= chaintable.Node(digit)

        cur = cur._next

    if carry>0:
        cur._next= chaintable.Node(carry)
        print(cur)
        cur = cur._next


    return dummy._next

chaintable.print_chain(addTwoNumber(a.head,b.head))



