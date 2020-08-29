class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let = []
        dig = []
        while len(logs) >= 1:
            str = logs.pop(0)
            if (str.split(' ')[1]).isalpha():
                let.append(str)
            else:
                dig.append(str)
                
        let.sort(key=lambda x: (x.split(" ", maxsplit=1)[1], x.split(" ", maxsplit=1)[0]))
        
        # for i in range(len(let)-1):
        #     for j in range(i , len(let)):
        #         left = let[i].split(' ',maxsplit=1)
        #         right = let[j].split(' ',maxsplit=1)
        #         if left[1] > right[1] :
        #             let[i], let[j] = let[j], let[i]
        #         elif left[1] == right[1]:
        #             if left[0] > right[0]:
        #                 let[i], let[j] = let[j], let[i]
        return let + dig