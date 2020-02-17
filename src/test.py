class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head: ListNode) -> bool:
    if not head or not head.next: return False
    slow_curr, fast_curr = head.next, head.next.next
    while slow_curr != fast_curr:
        if not fast_curr or not fast_curr.next: return False
        slow_curr = slow_curr.next
        fast_curr = fast_curr.next.next
    return True
