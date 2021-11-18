from scripts.DataSet import DataSet
from scripts.KMeans import KMeans
import os

def main():
    # print(os.listdir('lab3/data'))
    dataset = DataSet('baba')
    dataset.read_data('lab3/data/spiralka.txt', (0,1))

    dataset.kmean(m=4, n=100)

if __name__ == "__main__":
    main()
 