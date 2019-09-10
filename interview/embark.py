class Histogram:

    def __init__(self, bin_size, input):
      self.bin_size = bin_size
      self.input = input

    def execute(self):
        print('execute')

        self.bins = range(0, 20, 5)

        self.results = [0]*len(self.bins)
        print(self.results)

        print(self.bins)

        for ndx1 in input:
          temp = ndx1 // self.bin_size
          self.results[temp] = self.results[temp]+1
          print("%d %d" % (ndx1, temp))

        print(self.results)

    def pretty_print(self, max_width):
        max_element = -1
        for ndx1 in self.results:
            print("ndx1:%d" % ndx1)
            if ndx1 > max_element:
                max_element = ndx1

        delta = max_width//max_element
        print("delta:%d" % delta)
        print("max element:%d" % max_element)
#        if max_element > max_width:
#            delta = max_width/max_element
#        else:
#            delta = 1

        counter = 0
        for ndx1 in self.results:
            print("%d %s" %(self.bins[counter], "#"* int(ndx1*delta)))
            counter += 1


print('start')

if __name__ == '__main__':
    print('main')

    input = [1, 6, 7, 11, 11, 12]

    histogram = Histogram(5, input)
    histogram.execute()
    histogram.pretty_print(10)

print('stop')
