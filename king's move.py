def can_king_move(start,target):
    x1,y1=start
    x2,y2=target

    if abs(x1-x2)<=1 and abs(y1-y2)<=1:
        if 0<x2<9 and 1<=y2<=8:
            return True
    return False

start_position=(4,4)
target_position=(5,5)

if can_king_move(start_position,target_position):
    print('Король может сделать этот ход')
else:
    print('Король не может сделать этот ход')