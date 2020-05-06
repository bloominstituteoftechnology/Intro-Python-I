# # catalog what we already know
# define what medain means
# the middle element of all the elements once they're sorted
# figure out how to calculate it
# how do we deal with an even number of numbers?
# when should we handle the sorting?


class MedianFetcher:
    def __init__(self):
        # define all the attributes on 'self'
        self.median = None
        self.numbers = []

    # inserts the value n inton our class
    def insert(self, n):
        # where do you store n?
        # maybe we store it in self.median?
        # what happens when we insert more values?
        self.numbers.append(n)
        self.numbers.sort()  # sorts the list in-place

    def get_median(self):
        if len(self.numbers) == 0:
            return None
        # figure out if the length of the numbers list is odd or even
        mid = len(self.numbers) // 2
        if len(self.numbers) % 2 == 1:
            # if it's odd, then we can just pick the middle number
            # how do we get the middle number of a list?
            # take the length, divide it by 2
            return self.numbers[mid]
        else:
            # if it's even, get the average of the two middle numbers
            # grab the elment right before the mid element
            return (self.numbers[mid-1] + self.numbers[mid]) / 2

        def something(self):
            return 1


medianFetcher = MedianFetcher()
print(medianFetcher.get_median())
medianFetcher.insert(5)
print(medianFetcher.get_median())
medianFetcher.insert(10)
print(medianFetcher.get_median())  # returns 7.5
medianFetcher.insert(100)
print(medianFetcher.get_median())  # returns 10
medianFetcher.insert(1)
medianFetcher.insert(2)
print(medianFetcher.get_median())
