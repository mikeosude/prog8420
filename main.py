def cls():
    os.system("clear")

def main(acname, acno):
    accountName = acname
    accountNo = acno
    showMenu()

def deposit(amount):
    global balance, previousTransaction
    balance += amount
    previousTransaction = amount

def withdraw(amount):
    global balance, previousTransaction
    balance = balance - amount
    previousTransaction = -amount

def getPreviousTransaction():
    if previousTransaction > 0:
        print('Your deposit:', getPreviousTransaction)
    elif previousTransaction < 0:
        print('Your withdrawal:', previousTransaction)
    else:
        print('There is no transaction.')
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print('Welcome to the Conestoga big data bank')
print('Where your money works')
input('Press Enter to continue...')

def showMenu():
    print('A. Go to Account')
    print('B. Open an Account')
