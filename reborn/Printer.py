import datetime
from Enumerator import Enumerator

class Printer:
    def __init__(self, total):
        self.total = total
        self.enumerator = Enumerator(total)

    def print_ids(self, size):
        start_time = datetime.datetime.now()
        if size == 1:
            for h5 in range(1, self.total+1):
                # print("{}: {}".format([h5], self.enumerator.enumerate(h5)))
                print("{}".format(self.enumerator.enumerate(h5)))
        if size == 2:
            for h4 in range(1, self.total):
                for h5 in range(h4+1, self.total+1):
                    # print("{}: {}".format([h4, h5], self.enumerator.enumerate(h4, h5)))
                    print("{}".format(self.enumerator.enumerate(h4, h5)))
        if size == 3:
            for h3 in range(1, self.total-1):
                for h4 in range(h3+1, self.total):
                    for h5 in range(h4+1, self.total+1):
                        # print("{}: {}".format([h3, h4, h5], self.enumerator.enumerate(h3, h4, h5)))
                        print("{}".format(self.enumerator.enumerate(h3, h4, h5)))
        if size == 4:
            for h2 in range(1, self.total-2):
                for h3 in range(h2+1, self.total-1):
                    for h4 in range(h3+1, self.total):
                        for h5 in range(h4+1, self.total+1):
                            # print("{}: {}".format([h2, h3, h4, h5], self.enumerator.enumerate(h2, h3, h4, h5)))
                            print("{}".format(self.enumerator.enumerate(h2, h3, h4, h5)))
        if size == 5:
            for h1 in range(1, self.total-3):
                for h2 in range(h1+1, self.total-2):
                    for h3 in range(h2+1, self.total-1):
                        for h4 in range(h3+1, self.total):
                            for h5 in range(h4+1, self.total+1):
                                # print("{}: {}".format([h1, h2, h3, h4, h5], self.enumerator.enumerate(h1, h2, h3, h4, h5)))
                                print("{}".format(self.enumerator.enumerate(h1, h2, h3, h4, h5)))
        end_time = datetime.datetime.now()
        print("Elapsed time: {}".format(end_time - start_time))
    
    

printer = Printer(117)
printer.print_ids(int(input()))
