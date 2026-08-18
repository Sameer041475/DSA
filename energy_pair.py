class solution:
    def energyPairs(self, n, energy):
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                if energy[i] * energy[i] == energy[j] * energy[j]:
                    count += 1

        return count