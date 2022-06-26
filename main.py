
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    result = None
    current_node = None
    carry = 0
    while l1 is not None and l2 is not None:
        s = l1.val + l2.val + carry
        digit = s%10
        new_node = ListNode(digit)
        if current_node is not None:
            current_node.next = new_node
        if result is None:
            result = new_node
        current_node = new_node
        carry = int(s/10)
        l1 = l1.next
        l2 = l2.next

    while l1 is not None:
        s = l1.val + carry
        digit = s%10
        new_node = ListNode(digit)
        if current_node is not None:
            current_node.next = new_node
        if result is None:
            result = new_node
        current_node = new_node
        carry = int(s/10)
        l1 = l1.next

    while l2 is not None:
        s = l2.val + carry
        digit = s % 10
        new_node = ListNode(digit)
        if current_node is not None:
            current_node.next = new_node
        if result is None:
            result = new_node
        current_node = new_node
        carry = int(s/10)
        l2 = l2.next

    if carry > 0:
        new_node = ListNode(carry)
        current_node.next = new_node

    return result


"""Number 3: Longest Substring without repeating characters"""


def length_of_longest_substring(s: str) -> int:
    character_hash_table = {}
    character_queue = []
    longest_length = 0
    for i in range(len(s)):
        c = s[i]
        if c in character_hash_table:
            if len(character_queue) > longest_length:
                longest_length = len(character_queue)
            while character_queue[0] != c:
                remove_c = character_queue.pop(0)
                character_hash_table.pop(remove_c)
            character_queue.pop(0)
            character_queue.append(c)
        else:
            character_hash_table[c] = 0
            character_queue.append(c)

    if len(character_queue) > longest_length:
        longest_length = len(character_queue)

    return longest_length
