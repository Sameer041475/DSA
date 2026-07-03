class solution:
    def insert(self, s, x):
        s.add(x)

    def print_contents(self, s):
        for x in sorted(s):
            print(x, end=" ")
        print()

    def erase(self, s, x):
        s.discard(x)

    def find(self, s, x):
        return 1 if x in s else -1

    def size(self, s):
        return len(s)