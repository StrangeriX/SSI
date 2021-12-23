from scripts.lab6.greedy_pointer import GreedyPointer
from scripts.bitmap import Bitmap
from scripts.drawer import Drawer


def main():
    wzorzec1 = [[0, 0, 0, 1],
                [0, 0, 1, 1],
                [0, 1, 0, 1],
                [0, 0, 0, 1],
                [0, 0, 0, 1]
                ]
    wzorzec2 = [[0, 1, 1, 1],
                [1, 0, 0, 1],
                [0, 0, 1, 0],
                [0, 1, 0, 0],
                [1, 1, 1, 1]
                ]
    wzorzec3 = [[1, 1, 1, 0],
                [0, 0, 0, 1],
                [1, 1, 1, 1],
                [0, 0, 0, 1],
                [1, 1, 1, 0],
                ]
    testowa = [[1, 1, 1, 1],
               [0, 0, 0, 1],
               [1, 1, 1, 1],
               [0, 0, 1, 1],
               [1, 1, 1, 1]
               ]
    a = GreedyPointer()
    test = Bitmap((5, 4))
    test.set_matrix(testowa)
    a.add_reference_bitmap(wzorzec1)
    a.add_reference_bitmap(wzorzec2)
    a.add_reference_bitmap(wzorzec3)
    draw = Drawer(a.reference_bitmaps[0].size)
    test = draw.start()
    a.classify(test)


if __name__ == "__main__":
    main()
