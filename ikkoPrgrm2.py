import random

IKKO_LIST = ["ど", "ん", "だ", "け"]

def main():
    """メイン関数"""
    queue = []

    while True:
        char = IKKO_LIST[random.randint(0, 3)]
        print(char)
        
        if len(queue) == len(IKKO_LIST):
            queue.pop(0)
        queue.append(char)

        if queue == IKKO_LIST:
                print("どんだけ～！")
                return


if __name__ == "__main__":
    main()