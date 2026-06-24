# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        current=dummy
        while list1 and list2:
            if list1.val<=list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next
        if list1:
            current.next=list1
        else:
            current.next=list2
        return dummy.next
def build_linked_list(values):
    dummy=ListNode()
    current=dummy
    for v in values:
        current.next=ListNode(v)
        current=current.next
    return dummy.next
def print_linked_list(head):
    result=[]
    while head:
        result.append(head.val)
        head=head.next
    return result

list1=build_linked_list([1,2,4])
list2=build_linked_list([1,3,4])
obj=Solution()
merged=obj.mergeTwoLists(list1,list2)
print(print_linked_list(merged))