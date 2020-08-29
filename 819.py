class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        output = {}
        bestnum = 0
        beststring = ''
        paragraph = list(paragraph.lower())
        for i in range(len(paragraph)):
            if not paragraph[i].isalpha():
                paragraph[i] = ' '
        paragraph = ''.join(paragraph)
        
        for strs in paragraph.split():
            if strs in output:
                output[strs] += 1
            else:
                output[strs] = 1
        for s, n in output.items():
            if s in banned:
                continue
            if bestnum < n:
                beststring = s
                bestnum = n
                
        return beststring

import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        output = {}
        beststring = ''
        paragraph = list(paragraph.lower())
        for i in range(len(paragraph)):
            if not paragraph[i].isalpha():
                paragraph[i] = ' '
        paragraph = ''.join(paragraph)
        
        for s, n in collections.Counter(paragraph.split()).most_common():
            if s not in banned:
                return s
        
        return beststring