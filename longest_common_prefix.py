
def commonPrefix(strs):
    if strs[0] == "":
            return ""
    else:
        j = 0
        prefix = ""
        result = min(strs, key = len)
        max_j = len(result)
        while j < max_j:
            i = 0
            current_char = strs[i][j]
            count = 0
            while i < len(strs):
                if strs[i][j] == current_char:
                    count += 1
                i += 1
            
            if(count == len(strs)):
                prefix += current_char
            else:
                break
            j += 1
        
        print(prefix)





        
    





# print(strs[0][1])
strs = ["flower","flow","flight"]
commonPrefix(strs)
strs = [""]
commonPrefix(strs)
strs = ["cir" ,"car"]
commonPrefix(strs)