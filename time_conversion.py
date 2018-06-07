#===PROGRAM TO CONVERT TIME===
def timeConversion(s):
    hour = s[:2]    # to check for first two elements
    period = s[-2:] #check last two elements 
    if(period == 'PM'):  
        if(int(hour) < 12):  
            return str(int(hour) + 12) + s[2:-2]  #to add elements 2 to 3rd last (slicing is right exclusive) so that AM\PM won't get printed
        else:
            return s[:-2]   # so that AM and PM won't get printed
    else:
        if(period == 'AM'):  
            if(hour  == '12'):
                return ('00'+ s[2:-2])  
            else:
                return s[:-2]
        else:
            return s[:-2]

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)
    print(result)

