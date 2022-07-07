# ------ZEROS AND ONES TASK------

zero_string = '11000'

def get_index(string):
    index = 0
    for i in string:
        if i == '0':
            return index
        index += 1
    return 'no one zero'

z_c = get_index(zero_string)
print(f'zero starts in index - {z_c}  (first way)')

# or another way

try:
    z_c = zero_string.index('0')
    print(f'zero starts in index - {z_c}  (second way)')
except ValueError:
    print('no one zero')




# ------INTERSECTING RECTANGLES TASK------

def intersection(x1,y1,x2,y2,x3,y3,x4,y4):
    x_first = [x1,x2]
    x_second = [x3,x4]
    y_first = [y1, y2]
    y_second = [y3, y4]

    if max(x_first) < min(x_second) or max(y_first) < min(y_second) or min(y_first) > max(y_second):
        return False
    elif max(x_first) > min(x_second) and min(x_first) < min(x_second):
        intersection = max(x_first) - min(x_second)
        return f'rectangles intersect (crossing area - {intersection})'
    else:
        return 'rectangles intersect'
    



print(intersection(1,1,4,3,2,2,6,5))
