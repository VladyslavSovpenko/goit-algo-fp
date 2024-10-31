class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value} -> {self.next}"

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def get_middle(head):
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def sorted_merge(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.value <= right.value:
        result = left
        result.next = sorted_merge(left.next, right)
    else:
        result = right
        result.next = sorted_merge(left, right.next)
    return result

def merge_sort(head):
    if not head or not head.next:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    return sorted_merge(left, right)

def merge_two_sorted_lists(l1, l2):
    dummy = ListNode(0)
    tail = dummy

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2
    return dummy.next

if __name__ == "__main__":
    head = ListNode(4, ListNode(3, ListNode(1, ListNode(5))))
    print("Початковий список:", head)

    reversed_list = reverse_linked_list(head)
    print("Реверсований список:", reversed_list)

    sorted_list = merge_sort(reversed_list)
    print("Відсортований список:", sorted_list)

    list1 = ListNode(1, ListNode(3, ListNode(5)))
    list2 = ListNode(2, ListNode(4, ListNode(6)))
    merged_list = merge_two_sorted_lists(list1, list2)
    print("Об'єднаний відсортований список:", merged_list)
