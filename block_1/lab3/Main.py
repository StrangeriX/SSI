from scripts.lab3.DataSet import DataSet

def main():
    dataset = DataSet('baba')
    dataset.read_data('block_1/data/spiralka.txt', (0, 1))

    dataset.kmean(m=4, n=100)

if __name__ == "__main__":
    main()
 