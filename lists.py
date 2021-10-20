luckyNumbers = [4, 8, 3, 2, 5, "Yolo"]

luckyNumbers.append('fuckYou')
luckyNumbers.pop(0)

copyNumbers = list(luckyNumbers)
copyNumbers.pop(0)
copyNumbers.insert(0, 'hello world')


luckyNumbers.sort()

print(copyNumbers)

print(luckyNumbers)
