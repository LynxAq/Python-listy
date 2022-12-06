import random

def word_dic(s):
    dic = {}
    s = s.lower()
    for x in s:
        if (x not in dic.keys()):
            dic[x] = 1
        elif (x in dic.keys()):
            dic[x] += 1
    return dic


def word_checker(s1,s):
    dic1 = word_dic(s)
    dic2 = word_dic(s1)
    for letter2 in s1:
        if letter2 in dic1.keys():
            if (dic2[letter2] <= dic1[letter2]):
                pass
            else:
                return None
        else:
            return None
    return s1


slowa = set(open('popularne_slowa.txt', encoding='utf8').read().split())

name = 'Boleslaw Prus'
set_slow = set()
set_slow1 = set()
set_iteracji = set()
for word in slowa:
    if word.isalpha():
        set_slow.add(word)

#print(set_slow)

for item in set_slow:
    if len(item) <= len(name):
        if word_checker(item,name) == item:
            set_slow1.add(item)

while len(set_iteracji) == 0:
    x = random.choice(list(set_slow1))
    length_left = len(name) - len(x) - 1 #-1 bo usuwamy spacje

    for slowo in set_slow1:
        if len(slowo) == length_left:
            if word_checker(x + ' ' + slowo,name) == x + ' ' + slowo:
                set_iteracji.add(x + ' ' + slowo)

print(set_iteracji)
