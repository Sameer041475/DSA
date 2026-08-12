class solution:
    def uniqueOrder(self, n, arr):
        # Write your code here…
        result = []

        for i in range(len(arr)):
            if arr.count(arr[i]) == 1:
                result.append(arr[i])

        return result