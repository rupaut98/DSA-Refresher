def palindrome_check(head, tail):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    
    arr_reverse = []
    current = tail

    while current:
        arr_reverse.append(current.val)
        current = current.prev

    return arr == arr_reverse
