def can_king_move(start,target):
    x1,y1=start
    x2,y2=target

    if abs(x1-x2)<=1 and abs(y1-y2)<=1:
        if 1<=x2<=8 and 0<y2<9:
            return True
    return False

#Пример использования

start_position=(7,7)
target_position=(8,8)

if can_king_move(start_position,target_position):
    print("Король может сделать этот ход")
else:
    print("Король не может сделать этот ход")

