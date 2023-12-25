import re

words = { 'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4','five':'5',
          'six':'6','seven':'7', 'eight':'8','nine':'9'}
total = 0

def get_calibration(line):
    res = []
    n = len(line)
    for i in range(n):
        if  ord('0')<= ord(line[i]) <= ord('9'):
            res.append((int(line[i]),i))
    return res

def get_calibration_words(line):
    res = []
    n = len(line)
    
    for i in range(n):
        for k,v in words.items():
            if i + len(k) <  n:
                start = i
                end = i + len(k)
                if k == line[start:end]:
                    res.append((int(v),i)) 
    return res               

  



with open("day_1.txt","r") as f:
    lines = f.readlines()
    for line in lines:
        figures = get_calibration(line)
        numbers_words = get_calibration_words(line)
        res = figures + numbers_words 
        res = sorted(res, key= lambda x:x[1])
        print(f'\n\n{line}',res,'\n*****\n')
        total += res[0][0] * 10 + res[-1][0]

print(total)
