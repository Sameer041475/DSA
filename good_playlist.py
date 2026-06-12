class solution:
    def countGoodPairs(self, A, k):
        freq = {}
        count = 0

        for num in A:
            rem = num % k
            complement = (k - rem) % k

            count += freq.get(complement, 0)
            freq[rem] = freq.get(rem, 0) + 1

        return count