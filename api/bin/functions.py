import re
import json

def replaceRight(original, old, new, count_right):
    repeat=0
    text = original
    old_len = len(old)
    
    count_find = original.count(old)
    if count_right > count_find :
        repeat = count_find
    else :
        repeat = count_right

    while(repeat):
      find_index = text.rfind(old)
      text = text[:find_index] + new + text[find_index+old_len:]

      repeat -= 1
      
    return text

def convert_text(txt, before, after):
    data = []
    for part in re.split('[.,]\s+', txt):
        last = part[:2]
        part = replaceRight(part, before, after, 1)

        data.append(part)

        print(f"----------------------\n{last}\n--------------------")
    return {'result': data}
