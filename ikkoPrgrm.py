import random
from customQueue import CustomQueue


IKKO_LIST = ["ど", "ん", "だ", "け"]
CHEKC_STRING = "".join(IKKO_LIST)


def main():
    """メイン関数"""
    queue = CustomQueue(4)
    counter = 0

    while True:
        char = get_random_atchar()
        print(char)
        
        queue.enqueue(char)
        counter+=1

        if queue.join_queue_string() == CHEKC_STRING:
                print("どんだけ～！")
                print("出力 : " + str(counter) + "回")
                return


def get_random_atchar():
    """IKKO_LISTからランダムに文字を取得"""
    return IKKO_LIST[random.randint(0, 3)]


if __name__ == "__main__":
    main()