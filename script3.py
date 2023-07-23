#I have a clue on how i could have saved a space and time using a dictionaire maybe. I hope next time.

tfsa09 = 5000 + 5000 + 5000 + 5000 + 5500 + 5500 + 10000 + 5500 + 5500 + 5500 + 6000 + 6000 + 6000 + 6000
tfsa10 = 5000 + 5000 + 5000 + 5500 + 5500 + 10000 + 5500 + 5500 + 5500 + 6000 + 6000 + 6000 + 6000
tfsa11 = 5000 + 5000 + 5500 + 5500 + 10000 + 5500 + 5500 + 5500 + 6000 + 6000 + 6000 + 6000
tfsa12 = 5000 + 5500 + 5500 + 10000 + 5500 + 5500 + 5500 + 6000 + 6000 + 6000 + 6000
tfsa13 = 5500 + 5500 + 10000 + 5500 + 5500 + 5500 + 6000 + 6000 + 6000 + 6000
tfsa14 = 5500 + 10000 + 5500 + 5500 + 5500 + 6000 + 6000 + 6000 + 6000
tfsa15 = 10000 + 5500 + 5500 + 5500 + 6000 + 6000 + 6000 + 6000
tfsa16 = 5500 + 5500 + 5500 + 6000 + 6000 + 6000 + 6000
tfsa17 = 5500 + 5500 + 6000 + 6000 + 6000 + 6000
tfsa18 = 5500 + 6000 + 6000 + 6000 + 6000
tfsa19 = 6000 + 6000 + 6000 + 6000
tfsa20 = 6000 + 6000 + 6000
tfsa21 = 6000 + 6000
tfsa22 = 6000

birthYear = int(input("Please enter your birth year:"))
age = 2022 - birthYear
turn18 = birthYear + 18

if birthYear >= 2023:
    print("Please check if your birth year is correct and try again.")
if turn18 >= 2022:
    print("I'm truly sorry! TFSA Contribution room display information for 18 years or older.")


if turn18 <= 2009:
    print("Your age is", age, "and you turned 18 in", turn18)
    print("Your TFSA Contribution is:", tfsa09)

if turn18 == 2009:
    print("Your age is", age, "and you turned 18 in", turn18)
    print("Your TFSA Contribution is:", tfsa09)
if turn18 == 2010:
    print("Your age is", age, "and you turned 18 in", turn18)
    print("Your TFSA Contribution is:", tfsa10)
if turn18 == 2011:
    print("Your age is", age, "and you turned 18 in", turn18)
    print("Your TFSA Contribution is:", tfsa11)
if turn18 == 2012:
    print("Your age is", age, "and you turned 18 in", turn18)
    print("Your TFSA Contribution is:", tfsa12)
if turn18 == 2013:
    print("Your age is", age, "and you turned 18 in", turn18)
    print("Your TFSA Contribution is:", tfsa13)
if turn18 == 2014:
    print("Your age is", age, "and you turned 18 in", turn18)
    print("Your TFSA Contribution is:", tfsa14)
if turn18 == 2015:
    print("Your age is", age, "and you turned 18 in", turn18)
    print("Your TFSA Contribution is:", tfsa15)
if turn18 == 2016:
    print("Your age is", age, "and you turned 18 in", turn18)
    print("Your TFSA Contribution is:", tfsa16)
if turn18 == 2017:
    print("Your age is", age, "and you turned 18 in", turn18)
    print("Your TFSA Contribution is:", tfsa17)
if turn18 == 2018:
    print("Your age is", age, "and you turned 18 in", turn18)
    print("Your TFSA Contribution is:", tfsa18)
if turn18 == 2019:
    print("Your age is", age, "and you turned 18 in", turn18)
    print("Your TFSA Contribution is:", tfsa19)
if turn18 == 2020:
    print("Your age is", age, "and you turned 18 in", turn18)
    print("Your TFSA Contribution is:", tfsa20)
if turn18 == 2021:
    print("Your age is", age, "and you turned 18 in", turn18)
    print("Your TFSA Contribution is:", tfsa21)
if turn18 == 2022:
    print("Your age is", age, "and you turned 18 in", turn18)
    print("Your TFSA Contribution is:", tfsa22)


print("Thank you for checking")
