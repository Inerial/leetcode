class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        # print(list({'a':[1,2,3], 'b':[1,2,3]}.values()))
        for s in strs:
            if ''.join(sorted(s)) in output:
                output[''.join(sorted(s))] += [s]
            else:
                output[''.join(sorted(s))] = [s]
                
        return list(output.values())