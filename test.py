def midpoints(list):
    '''
    :param list: List of length n
    :return: List of length n-1 that include the midpoints of the original list
    '''
    midpoint = []
    for i in range(len(list)):
        try:
            midpoint.append(list[i]+(list[i+1]-list[i])/2)
        except:
            break

    return midpoint

list = [1,2,4,8,16]
for i in range(len(list)):
    print(i)