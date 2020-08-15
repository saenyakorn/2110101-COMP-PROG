import numpy as np

def sum_2_rows( M ):
    return M[::2] + M[1::2] 
def sum_left_right( M ):
    return (M.T[:][:M.T.shape[0]//2] + M.T[:][M.T.shape[0]//2:]).T  
def sum_upper_lower( M ):
    return M[:][:M.shape[0]//2] + M[:][M.shape[0]//2:] 
def sum_4_quadrants( M ):
    Top,Bot = (M[:][:M.shape[0]//2]),(M[:][M.shape[0]//2:])
    TL,TR = Top.T[:][:Top.T.shape[0]//2].T,Top.T[:][Top.T.shape[0]//2:].T
    BL,BR = Bot.T[:][:Bot.T.shape[0]//2].T,Bot.T[:][Bot.T.shape[0]//2:].T
    return TL + TR + BL + BR
def sum_4_cells( M ):
    QT,QB = M[:][::2],M[:][1::2]
    QTL,QTR = QT.T[:][::2].T,QT.T[:][1::2].T
    QBL,QBR = QB.T[:][::2].T,QB.T[:][1::2].T
    return QTL + QTR + QBL + QBR
def count_leap_years( years ):
    return sum(((years-543)%400==0) | (((years-543)%4==0)&((years-543)%100!=0)))

exec(input().strip())

# print(count_leap_years(np.array([2143, 2543, 2544, 2643, 2562, 2559, 2560, 2561, 2547, 2562, 2563])))