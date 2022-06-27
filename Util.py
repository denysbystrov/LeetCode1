

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def convert_array_to_list(num_array: list) -> ListNode:
    prev_node = None
    start_node = None
    for num in num_array:
        new_node = ListNode(num)
        if prev_node:
            prev_node.next = new_node
        else:
            start_node = new_node
        prev_node = new_node

    return start_node


def convert_list_to_array(node: ListNode) -> list:
    num_array = []
    current_node = node
    while current_node:
        num_array.append(current_node.val)
        current_node = current_node.next

    return num_array