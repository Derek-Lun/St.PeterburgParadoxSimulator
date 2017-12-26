import random

totalRound = 1000
roundCounter = sum = coinFlipResult = coinFlipCounter = 0

while (roundCounter < totalRound):
	roundCounter += 1
	roundResult = 2
	while (random.randint(0, 1) == 1):
		coinFlipCounter += 1
		coinFlipResult += 1
		roundResult *= 2
	coinFlipCounter += 1
	sum += roundResult
	print str(roundCounter) + " return is: " + str(roundResult);

print "coinFlipAvg: " + str(coinFlipResult/float(coinFlipCounter))
print "sum: " + str(sum)
print "avg: " + str(sum/float(totalRound))