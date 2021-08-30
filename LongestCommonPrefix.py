class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    
        #strs = ["flower","flow","flight"]

        l = zip(*strs)
        #l = [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
        
        #empty prefix string
        prefix = ""
        
        for i in l:
            if len(set(i))==1:
                #add to index zero of prefix 
                prefix += i[0]
            else:
                break
        return prefix
