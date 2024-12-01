
def readfile():
    left=[]
    right=[]
    with open("../../inputs/day1.txt", "r") as file:
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
    print(distanceScore)


def part2():
    (left,right) = readfile()
    similarityscore = 0
    for i in range(len(left)):
        countLinR = 0
        for j in range(len(right)):
            if left[i] == right[j]:
                countLinR += 1
        similarityscore += left[i]*countLinR
    print(similarityscore)

part1()
part2()
