class solution:
    def chocolatePopularity(self, n, chocolates):
        freq = {}

        for chocolate in chocolates:
            freq[chocolate] = freq.get(chocolate, 0) + 1

        result = list(freq.keys())

        result.sort(key=lambda x: (-freq[x], x))

        return result