import random
from customQueue import CustomQueue

queue = CustomQueue(4)
ikkoList = ["ど", "ん", "だ", "け"]

def main():
    num = 0
    while num < 10:
        getRandomAtChar()
        num += 1

def getRandomAtChar():
    num = random.randint(0, 3)
    print(ikkoList[num])

if __name__ == "__main__":
    main()