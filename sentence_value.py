def sentenceValue(sentence):
    # print(sentence)
    value = 0
    characters = "0abcdefghijklmnopqrstuvwxyz"
    for i in sentence:
        count = 0
        temp = 0
        length = len(i)
        for j in i:
            if(j.isupper()):
                count += 1
            if(j.islower() or j.isupper()):
                temp = temp + characters.index(j.lower())
        
        if(count == length):
            temp = temp*2
        value = value + temp
    
    print(value)
        

sentence = "abc ABC Abc"
sentence_list = list(sentence.split(" "))
# print(sentence_list[0][0])
sentenceValue(sentence_list)