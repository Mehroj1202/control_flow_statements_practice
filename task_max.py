def find_max(a,b,c):
    """
    Find the maximum number.
    Args:

        a: int
        b: int
        c: int
    return:
        int
    """
    if a<b<c:
        return c
    if a<c<b:
        return b
    if b<a<c:
        return c
print(find_max(-1,12,3))

# Example:
# find_max(1,2,3) -> 3
# find_max(-1,12,3) -> 12

def find_max_idx(a,b,c):
    """
    Find the index of the maximum number.
    Args:
        a: int
        b: int
        c: int
    return:
        int
    """
    if a<b<c:
        return 3
    if a<c<b:
        return 2
    if b<c<a:
        return 1
print(find_max_idx(1,3,4))
print(find_max_idx(-1,12,3))

# Example:
# find_max_idx(10,2,13) -> 3
# find_max_idx(-1,12,3) -> 2