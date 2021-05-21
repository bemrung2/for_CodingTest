def solution(n, lost, reverse):
    reverse_del = set(reverse) - set(lost)
    lost_del = set(lost) - set(reverse)
    
    for i in reverse_del:
        if i-1 in lost_del:
            lost_del.remove(i-1)
        elif i+1 in lost_del:
            lost_del.remove(i+1)
    
    return n - len(lost_del)

# def solution(n, lost, reverse):
#     reverse_del = set(reverse) - set(lost)
#     lost_del = set(lost) - set(reverse)

#     for i in reverse_del:
#         if i-1 in lost_del:
#             lost_del.remove(i-1)
#         elif i+1 in lost_del:
#             lost_del.remove(i+1)

#     return n-len(lost_del)
