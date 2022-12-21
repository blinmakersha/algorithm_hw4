
def twoCitySchedCost(costs):
    costs.sort(key=lambda x: x[0]-x[1])
    half = len(costs) // 2
    res = 0
    for el in costs:
        half -= 1
        if half < 0:
            res += el[1]
        else:
            res += el[0]
    return res


print(twoCitySchedCost([[259, 770], [448, 54],
                        [926, 667], [184, 139],
                        [840, 118], [577, 469]]))
