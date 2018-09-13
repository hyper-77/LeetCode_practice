import chaintable

a=chaintable.ChainTable()

for i in range(7):
    a.append(i)

print(a)

def swapNode(head):
    dummy=chaintable.Node(-1)
    cur=dummy
    dummy._next=head
    while not cur._next==None and not cur._next._next==None:

        a=cur._next
        b=cur._next._next

        t=b._next
        cur._next=b
        b._next=a
        a._next=t

        cur=a

    return dummy._next


chaintable.print_chain(swapNode(a.head))
#----------------------------------------------------------------------------------


def swapNode_recur(head): # implement swap node by recursion
    if  head==None or  head._next==None:return head

    else:
        a = head
        b = head._next
        t = b._next
        a._next = swapNode_recur(t)
        b._next = a
        return b


b=chaintable.ChainTable()

for i in range(7):
    b.append(i)

print(b)
chaintable.print_chain(swapNode_recur(b.head))




