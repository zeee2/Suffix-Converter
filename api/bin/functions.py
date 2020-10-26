import re
import json
from hanspell import spell_checker

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

def convert_text(sc, txt, before, after):
    data = []
    if sc == 0:
        for part in re.split('[.,]\s+', txt):
            last = part[:2]
            part = replaceRight(part, before, after, 1)
            data.append(f"{part}\n") 
    elif sc == 1:
        for part in re.split('[.,]\s+', txt):
            last = part[:2]
            part = replaceRight(part, before, after, 1)
            part = [part]
            spell_chk = spell_checker.check(part)
            
            spell_result = spell_chk[0][2]
            data.append(f"{spell_result}\n")
    
    return {'result': data}
