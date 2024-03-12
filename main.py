# define number checks, return numbers
def checkInputNum (testNumeric):
  if testNumeric.isnumeric():
    return int(testNumeric)
  else:
    print(f"{testNumeric} is not a valid input. Please try again.")
    exit()

# define function for range calculation 
def computeRange(mathFunction):
  return validNumShift // validTransaction // validDollarValue


#input
employeeName = input("Please enter employee Name: ")
baseNumShift = input("Number of shifts: ")
baseNumTransaction = input("Number of transactions: ")
baseNumDollarValue = input("Dollar value of transactions: ")

validNumShift = checkInputNum(baseNumShift)
validTransaction = checkInputNum(baseNumTransaction)
validDollarValue= checkInputNum(baseNumDollarValue)
totalRange = computeRange()


print(totalRange)