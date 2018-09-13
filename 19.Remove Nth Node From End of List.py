import chaintable

def print_chain(temp): # given the head of chain ,then print the whole chain
    string = ''
    while not temp == None:
        string += str(temp.data) + ' '
        temp = temp._next
    print(string)

a=chaintable.ChainTable()

for i in range(6):
    a.append(i)

print(a)


def  removeNthFromEnd(head,  n):
    if head._next==None:return None
    pre=head
    cur=head
    for i in range(n):
        cur=cur._next
    if cur==None: return head._next
    while not cur._next==None:
        cur=cur._next
        pre.pre._next

    pre._next=pre._next._next

    return head


print_chain(removeNthFromEnd(a.head,5))



