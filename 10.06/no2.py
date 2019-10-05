# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        preNode = ListNode(0)
        lastNode = preNode
        val = 0
        while val or l1 or l2:
            val,cur = divmod(val + (l1.val if l1 else 0) + (l2.val if l2 else 0) ,10)
            lastNode.next = ListNode(cur)
            lastNode = lastNode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return preNode.next



def generateList(l:list) -> ListNode:
    preNode = ListNode(0)
    lastNode = preNode
    for val in l:
        lastNode.next = ListNode(val)
        lastNode = lastNode.next
    return preNode.next

def printList(l:ListNode):
    while l:
        print("%d, " %(l.val),end='')
        l = l.next
    print('')

if __name__ == '__main__':
    l1 = generateList([1,5,8])
    l2 = generateList([9,1,2,9])
    printList(l1)
    printList(l2)
    s = Solution()
    sum = s.addTwoNumbers(l1,l2)
    printList(sum)


