import pandas as pd
import numpy as np


chat_id = 345280072 # Ваш chat ID, не меняйте название переменной

def solution(control: np.ndarray, test: np.ndarray) -> bool:
    # Односторонний независимый t-тест
    t_stat, p_value = stats.ttest_ind(test, control, alternative='greater')
    
    # Уровень значимости
    alpha = 0.04
    
    # Отклоняем нулевую гипотезу, если p-значение меньше уровня значимости
    return p_value < alpha
