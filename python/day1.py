from typing import Mapping

def readfile():
    left: list[int]=[]
    right: list[int]=[]
    with open("../inputs/day1.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            splitline = line.split('   ')
            left.append(int(splitline[0]))
            right.append(int(splitline[1]))
        file.close()
        return (left, right)


def part1():
    (left,right) = readfile()
    sortedleft = sorted(left)
    sortedright = sorted(right)
    distanceScore = 0
    for i in range(len(sortedleft)):
        distanceScore += abs(sortedleft[i] - sortedright[i])
    return distanceScore


def part2():
    (left,right) = readfile()
    map: Mapping[int,int] = {}
    for i in right:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
    score=0
    for i in left:
        if i in map:
            score+=i*map[i]
    return score


print(part1())
print(part2())
