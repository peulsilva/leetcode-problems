# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # edge cases

        # if l1 is None and l2 not is None:
        #     return 

        def linked_list_to_number(l : ListNode):
            n = 0
            power = 0
            while l is not None : 
                n += l.val * 10**power
                power += 1

                l = l.next
            return n

        def number_to_list(n : int):
            l = None
            n = str(n)
            for digit in n:
                if l is None:
                    l = ListNode(digit)
                    continue

                else:
                    temp = ListNode(digit)
                    temp.next = l
                    l = temp

            return l


        l1_number = linked_list_to_number(l1)
        l2_number = linked_list_to_number(l2)

        s = l1_number + l2_number

        return number_to_list(s)
        