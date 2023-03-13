#  PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_dollars(string):
    new_string =[]
    for i in range(0,len(string)):
        new_string.append(string[i])
        new_string.append(string[i])
        new_string.append(string[i])
    
    return " ".join(new_string)

print(paper_dollars('Mississippi'))
