# ------ZEROS AND ONES TASK------

zero_string = '11000'

def get_index(string):
    index = 0
    for i in string:
        if i == '0':
            return index
        index += 1
    return 'no one zero'

print(get_index(zero_string))

# or another way

try:
    print(zero_string.index('0'))
except ValueError:
    print('no one zero')




# ------INTERSECTING RECTANGLES TASK------

def intersection(x1,y1,x2,y2,x3,y3,x4,y4):
    pass

print(intersection(1,1,2,2,3,3,4,4))
