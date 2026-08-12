class solution:
    def totalListeningMinutes(self, N,K,M,songs,favoriteArtists):
        # Write your code here...
        total = 0
        for i , j in songs:
            if i >= K and j in favoriteArtists:
                total += i
        return total
                