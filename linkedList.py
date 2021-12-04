
def reverseList(head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev

num = [1,2,3,4,5]
print(reverseList(num))
    