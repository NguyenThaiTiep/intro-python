# search
import re
# hh:mm:ssPM
txt = "12:45:54PM"
(hour,minutes,seconds,type) = re.search(r'([0-9]{2})\:([0-9]{2})\:([0-9]{2})(PM|AM)',txt).groups()
# format date 

if type == "PM" :
        hour = int(hour)
        if(hour > 12): hour += 12
        hour %= 24
else :
        hour = int(hour) % 12 
if(hour < 10):
    hour = f'0{hour}'    
print(f"{hour}:{minutes}:{seconds}:{type}")
