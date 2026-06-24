class Solution:
    def operate(self, pairs):
        total = 0
        text = ""
        
        for num, word in pairs:
            total += num
            text += word
        
        print(total)
        print(text)
        print(len(text))