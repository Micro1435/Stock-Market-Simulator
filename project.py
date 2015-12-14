# Stock Market Simulator
# Michael Montella
# Oct 13, 2015

# CSCI 1300 Project 1

import random
import time

# Initial text that the user reads
print "Welcome to the Stock Market Simulator"
print ""
print "You have 3 stock options to buy"
print ""
print "Apple Inc: $111/share"
print "Amazon.com Inc: $548/share"
print "Tesla Motor Company: $219/share"
print ""
print "How many shares would you like to buy?"
applePrice = 111
amazonPrice = 548
teslaPrice = 219

aaplStock = open("aaplStock.txt", "w")
amznStock = open("amznStock.txt", "w")
tslaStock = open("tslaStock.txt", "w")

appleStock = int(raw_input("Apple Stock "))
aaplStock.write("%d \n" % appleStock)
amazonStock = int(raw_input("Amazon Stock "))
amznStock.write("%d \n" % amazonStock)
teslaStock = int(raw_input("Telsa Stock "))
tslaStock.write("%d \n" % teslaStock)

stockOptions = {"AAPL" : applePrice, "TSLA" : teslaPrice, "AMZN" : amazonPrice}

# Totals up the users initial investment

def buyStock():
	global appleShares
	global amazonShares
	global teslaShares
	global totalInvestment
	global stockOptions
	global rounds

	print "How many shares do you want to buy?"
	for i in stockOptions:											# Loops through the stock options dictionary
		if i == "AAPL":
			newAppleShares = int(raw_input("Apple Stock "))			# Gets the amount of new shares the user wants
			appleShares += newAppleShares							# Adds the new shares to existing shares
			aaplStock.write("%d" % appleShares)
			newAppleInvestment = newAppleShares * stockOptions[i]	# Multiplies new shares by the current price
		elif i == "AMZN":
			newAmazonShares = int(raw_input("Amazon Stock "))
			amazonShares += newAmazonShares
			amznStock.write("%d \n" % amazonShares)
			newAmazonInvestment = newAmazonShares * stockOptions[i]

		elif i == "TSLA":
			newTeslaShares = int(raw_input("Telsa Stock "))
			teslaShares += newTeslaShares
			tslaStock.write("%d \n" % teslaShares) 
			newTeslaInvestment = newTeslaShares * stockOptions[i]

	# Adds to your total investment
	totalInvestment = totalInvestment + (newAppleInvestment + newAmazonInvestment + newTeslaInvestment)

	print "Current total investment = $", totalInvestment
	print ""
	print "AAPL", appleShares
	print "AMZN", amazonShares
	print "TSLA", teslaShares

def sellStock():
	global appleShares
	global amazonShares
	global teslaShares
	global stockOptions
	global returnAmount
	global appleSharesSold
	global amazonSharesSold
	global teslaSharesSold

	print "How many shares do you want to sell?"
	for i in stockOptions:												# Loops through the stock options dictionary
		if i == "AAPL":
			appleSharesSold = int(raw_input("Apple Stock "))			# Gets the amount of shares to sel
			if appleSharesSold <= appleShares:							# Checks to make sure user has that many shares
				appleShares -= appleSharesSold							# Subtracts the amount sold from total shares
				aaplStock.write("%d \n" % appleShares)
				appleReturn = appleSharesSold * stockOptions[i]			# Multiplies the amount of shares sold by price
			else:
				print "You cannot sell more shares than you own!"
				break
		elif i == "AMZN":
			amazonSharesSold = int(raw_input("Amazon Stock "))
			if amazonSharesSold <= amazonShares:
				amazonShares -= amazonSharesSold
				amznStock.write("%d \n" % amazonShares)
				amazonReturn = amazonSharesSold * stockOptions[i]
			else:
				print "You cannot sell more shares than you own!"
		elif i == "TSLA":
			teslaSharesSold = int(raw_input("Telsa Stock "))
			if teslaSharesSold <= teslaShares:
				teslaShares -= teslaSharesSold
				tslaStock.write("%d \n" % teslaShares)
				teslaReturn = teslaSharesSold * stockOptions[i]
			else:
				print "You cannot sell more shares than you own!"
	# Adds to the total return
	returnAmount = returnAmount + (appleReturn + amazonReturn + teslaReturn)

	print "Total return = $", returnAmount
	print ""
	print "AAPL", appleShares
	print "AMZN", amazonShares
	print "TSLA", teslaShares

# Runs after the game is over
def final():
	aaplStock.close()
	amznStock.close()
	tslaStock.close()

	for i in stockOptions:
		if i == "AAPL":
			totalAppleAmount = appleShares * stockOptions[i]							
		elif i == "AMZN":
			totalAmazonAmount = amazonShares * stockOptions[i]
		elif i == "TSLA":
			totalTeslaAmount = teslaShares * stockOptions[i]

	# Total amount of money made
	grossSum = totalAppleAmount + totalAmazonAmount + totalTeslaAmount

	# Net amount of money made or lost
	netAmount = grossSum + returnAmount - totalInvestment

	print "You finished with" , appleShares, "Apple Shares"
	print "You finished with" , amazonShares, "Amazon Shares"
	print "You finished with" , teslaShares, "Telsa Shares"
	print ""
	print "Your initial investment was $", initialInvestment
	print "Your total investment was $", totalInvestment
	print ""
	if netAmount > 0:
		print "You made $", netAmount
	else:
		netAmount *= -1
		print "You lost $", netAmount

appleShares = appleStock
amazonShares = amazonStock
teslaShares = teslaStock

initialInvestment = (applePrice * appleStock) + (amazonPrice * amazonStock) + (teslaPrice * teslaStock)
totalInvestment = initialInvestment
returnAmount = 0


print "Your initial investment is $" + `initialInvestment`
print ""
print "In this simulator,you will have the chance to watch as the stock prices fluctuate in a simulated environment.  The goal of the game is to finish with the most money."
print ""
print "Before the game begins, you will have the chance to select how many rounds you would like to play.  Each round consists of one set of price changes.  For example, If you play 4 rounds, you will only have 4 chances to buy or sell your stock."
print ""
print "After each price change, you will have the option of buying more stock, selling stock, or none.  If you want to buy, type 'buy'. If you want to sell, type 'sell'. If you want to continue, press enter."
print ""
print "If you sell shares, make sure you are selling LESS THAN or EQUAL to the amount of shares that you have.  If you try sell more, you will lose your chance to sell any shares."
print ""
raw_input("Press enter to begin")
print ""
rounds = int(raw_input("How many rounds would you like to play? "))

for i in range (0, rounds):

	for item in stockOptions:	# Loops through each item in the dictionary

		def priceChange():
			global currentPrice
			result = random.randint(0, 100)
			if result >= 30:	# Decides if price will increase or decrease
				priceIncrease = random.uniform(0, 0.15)		# Increases by random amount
				currentPrice = currentPrice + (currentPrice * priceIncrease)	# Changes the current price
			else:
				priceDecrease = random.uniform(0, 0.15)
				currentPrice = currentPrice - (currentPrice * priceDecrease)
			return currentPrice

		currentPrice = stockOptions[item]	# Sets currentPrice to the stock option price
		stockOptions[item] = priceChange()	# Changes the stock's price depending on what the new price is through the function
		print item, " ", stockOptions[item]

	print ""
	print "Rounds left", rounds - i

	i += 1

	buyOrSell = raw_input()
# Get code to skip block if user does not input anything
	if buyOrSell == "buy":	# Checks to see if the user wants to buy more
		buyStock()
	elif buyOrSell == "sell":
		sellStock()
	else:
		time.sleep(0.1)

final()