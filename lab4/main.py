from scripts.Strategy_1plus1 import Strategy_1plus1
import os

def main():
    # print(os.listdir('lab4/scripts'))
    oneplusone = Strategy_1plus1(10.0,1.1,100)
    oneplusone.start()

if __name__ == "__main__":
    main()
 