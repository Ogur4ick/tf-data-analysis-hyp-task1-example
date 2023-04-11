import pandas as pd
import numpy as np


chat_id = 968976840. # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    p = (x_success + y_success)/(x_cnt + y_cnt)
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    se  = (p*(1-p)*(1/x_cnt + 1/y_cnt))**0.5
    z = (p2 - p1) / se
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return z > 1.64 # Ваш ответ, True или False
