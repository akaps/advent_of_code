def manhattan_distance(loc1, loc2):
    dist = 0
    for dim in enumerate(loc1):
        dist += abs(dim[1]-loc2[dim[0]])
    return dist
