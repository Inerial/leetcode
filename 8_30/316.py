class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []
        # 갯수, 스택에 있는가?, 스택
        
        for c in s:
            counter[c] -= 1
            ## 뽑아온 알파벳 갯수 감소
            if c in seen:
                continue
            ## 이미 스택에 있는 알파벳은 안뺌
            while stack and c < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            ## 이미 스택에 없는 알파벳이 나왔는데 스택 가장 뒤에있는 알파벳이 해당 알파벳보다 크고
            ## 스택 맨뒤에 있는 알파벳이 이후에 또 나올수 있으면 스택 맨뒤에 있는것을 빼고 seen에서도 뺌
            stack.append(c)
            seen.add(c)
            ## 추가
        return ''.join(stack)