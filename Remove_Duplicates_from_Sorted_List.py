class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        prev = head
        current = head.next
        while current!=None:
            if prev.val==current.val:
                temp = current.next
                prev.next = current.next
                current = temp
            else:
                prev = prev.next
                current=current.next
        return head
