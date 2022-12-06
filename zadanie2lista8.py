def word_dic(s):
    dic = {}
    s = s.lower()
    for x in s:
        if (x not in dic.keys()):
            dic[x] = 1
        elif (x in dic.keys()):
            dic[x] += 1
    return dic

#print(word_dic('Titties'))

def word_checker(s1,s):
    dic1 = word_dic(s)
    dic2 = word_dic(s1)
    for letter2 in s1:
        if letter2 in dic1.keys():
            if (dic2[letter2] <= dic1[letter2]):
                pass
            else:
                print('Slowa nie da sie zbudowac')
                quit()
    return 'Słowo ' + s1 + ' da się zbudowac z ' + s

print(word_checker('motyl','lokomotywa'))