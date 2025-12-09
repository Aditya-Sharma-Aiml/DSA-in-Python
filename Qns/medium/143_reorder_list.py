class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        # Find the half of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None
        # Reverse the second half of the list
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        
        first = head
        second = prev
        # Create the new list
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

        # Time Complexity O(n)
        # Space Complexity O(1)