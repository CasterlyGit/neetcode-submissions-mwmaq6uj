class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        output = ''

        for index, ch in enumerate(strs[0]):

            for s in strs[1:]:

                if index >= len(s) or s[index] != ch:
                    return output

            output += ch

        return output