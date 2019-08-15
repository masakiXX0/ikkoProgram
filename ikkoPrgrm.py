import random
from customQueue import CustomQueue

ikkoList = ["ど", "ん", "だ", "け"]

# メイン
def main():
    queue = CustomQueue(4)
    counter = 0

    while True:
        char = getRandomAtChar()
        queue.enqueue(char)
        print(char)
        counter+=1

        if queue.join_queue_string() == "どんだけ":
                print("どんだけ～！")
                print("出力 : " + str(counter) + "回")
                return

# ikkoListからランダムに文字を取得
def getRandomAtChar():
    return ikkoList[random.randint(0, 3)]

if __name__ == "__main__":
    main()