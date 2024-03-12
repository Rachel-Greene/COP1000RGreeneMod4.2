# define number checks, return numbers
def checkInputNum(testNumeric):
  if testNumeric.isnumeric():
    return int(testNumeric)
  else:
    print(f"{testNumeric} is not a valid input. Please try again.")
    exit()

# define nested if for total bonus amount #
def bonusCalculation(bonusRange):
  if bonusRange <=30:
    return bonus1
  elif bonusRange > 30 and bonusRange <= 69:
    return bonus2
  elif bonusRange >= 70 and bonusRange <= 199:
    return bonus3
  else:
    return bonus4




bonus1 = 50.00
bonus2 = 75.00
bonus3 = 100.00
bonus4 = 200.00

#input
employeeName = input("Please enter employee Name: ")
baseNumShift = input("Number of shifts: ")
baseNumTransaction = input("Number of transactions: ")
baseNumDollarValue = input("Dollar value of transactions: ")

validNumShift = checkInputNum(baseNumShift)
validTransaction = checkInputNum(baseNumTransaction)
validDollarValue= checkInputNum(baseNumDollarValue)
totalRange = (validDollarValue /validTransaction) /validNumShift

finalBonus = bonusCalculation(totalRange)


print(totalRange)
print(finalBonus)