## Program written to calculate empolyee bonuses based on: ##
## sales, dollar value, number of shift ##

## Bonus Amount, fixed variables ##
BONUS1 = 50.00
BONUS2 = 75.00
BONUS3 = 100.00
BONUS4 = 200.00

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
    return BONUS1
  elif bonusRange <= 69:
    return BONUS2
  elif bonusRange <= 199:
    return BONUS3
  else:
    return BONUS4


#input
employeeName = input("Please enter employee name: ")

baseNumShift = input("Enter number of shifts: ")
validNumShift = checkInputNum(baseNumShift)

baseNumTransaction = input("Enter number of transactions: ")
validTransaction = checkInputNum(baseNumTransaction)

baseNumDollarValue = input("Enter transaction dollar value: ")
validDollarValue= checkInputNum(baseNumDollarValue)


totalRange = (validDollarValue /validTransaction) /validNumShift


## Outputs ##
finalBonus = bonusCalculation(totalRange)
print("-----")
print(f"Employee Name: {employeeName}")
print(f"Employee Bonus: {finalBonus}")
