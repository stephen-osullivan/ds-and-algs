def binary_search(l:list, v):
    """searches for a value in a sorted list using binary search"""
    if v is None: 
        return None
    start, end = 0, len(l) 
    while start != end: # triggers if the one element list does not contain v
        guess = (start + end) // 2 # if length of list is n, then returns (n+1)/2 for n odd,  n/2 for n even
        if l[guess] == v:
            return guess
        elif l[guess] < v:
            start = guess + 1
        else:
            end = guess -1
    return None # triggers of len(l) == 0

if __name__ == '__main__':
    # some test cases
    test_cases = [
        dict(input=dict(l=[1,2,3,4,5], v=5), output = 4),
        dict(input=dict(l=[1,2,3,4,5], v=6), output = None),
        dict(input=dict(l=list(range(1000)), v=1), output = 1),
        dict(input=dict(l=[], v= 10), output=None),
        dict(input=dict(l=[1,2,3,4], v=None), output=None),
        dict(input=dict(l=[1], v = 1),output=0)
    ] 

    for idx, test in enumerate(test_cases):
        try:
            binary_search(**test['input']) == test['output'], f'Test {idx} failed.'
        except Exception as e:
            print(f'Test {idx} failed with error:')
            raise e
    print('All tests passed.')
