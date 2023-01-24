#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda m_list:
                    list(map(lambda sn: sn ** 2, m_list)), matrix))
