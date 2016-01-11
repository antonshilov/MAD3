import pprint
from math import sqrt, log, exp, pi
from random import random, uniform

pp = pprint.PrettyPrinter(indent=4)


def generate_mpc(m1, d1, m2, d2, n):
    v1 = v2 = 0.
    s = 1
    result = [[], []]
    for i in range(n):
        while not 0 < s < 1:
            # u1 = uniform(-1, 1)
            # u2 = uniform(-1, 1)
            v1 = 2 * uniform(-1, 1) - 1
            v2 = 2 * uniform(-1, 1) - 1
            s = v1 ** 2 + v2 ** 2
        x1 = v1 * sqrt(-2 * log(s) / s)
        x2 = v2 * sqrt(-2 * log(s) / s)
        y1 = sqrt(d1) * x1 + m1
        y2 = sqrt(d2) * x2 + m2
        result[0].append(y1)
        result[1].append(y2)
        s = 1
    return result


# Оценка матожидания
def get_exp_val_eval(rand_val):
    return sum(rand_val) / len(rand_val)


# Оценка дисперсии
def get_disp_eval(rand_val, exp_val):
    disp = 0.
    for i in rand_val:
        disp += (i - exp_val) ** 2
    disp /= len(rand_val) - 1
    return disp


# Априорная вероятность класса
def get_prior_class_prob(class_size, size):
    return class_size / size


# Определяем размер выборок
def generate_amount(p, n):
    res = [0, 0]
    for i in range(n):
        num = random()
        if num > p:
            res[0] += 1
        else:
            res[1] += 1
    return res[0], res[1]


# Вычисляем плотность вероятности
def get_prob_density(x1, x2, d1, d2, m1, m2):
    return exp(
            -0.5 * ((x1 - m1) / sqrt(d1)) ** 2 -
            0.5 * ((x2 - m2) / sqrt(d2)) ** 2) \
           / (2 * pi * sqrt(d1 * d2))


def classify(class1, class2, d11, d12, d21, d22, m11, m12, m21, m22, p1, p2):
    errors1 = errors2 = 0
    for i in range(len(class1[0])):
        density1 = get_prob_density(class1[0][i], class1[1][i], d11, d12, m11, m12)
        density2 = get_prob_density(class1[0][i], class1[1][i], d21, d22, m21, m22)
        result = density1 * p1 - density2 * p2
        if result < 0:
            errors1 += 1
    for i in range(len(class2[0])):
        density1 = get_prob_density(class2[0][i], class2[1][i], d11, d12, m11, m12)
        density2 = get_prob_density(class2[0][i], class2[1][i], d21, d22, m21, m22)
        result = density1 * p1 - density2 * p2
        if result > 0:
            errors2 += 1
    return errors1, errors2


def get_classifier_fault(n, d11, d12, d21, d22, m11, m12, m21, m22, p1, p2, k):
    # Размеры выборок для классов
    n1, n2 = generate_amount(p1, n)

    # Генерируем выборки МПК
    class1 = generate_mpc(m11, d11, m12, d12, n1)
    class2 = generate_mpc(m21, d21, m22, d22, n2)

    # Оценка априорной вероятности
    p1_eval = get_prior_class_prob(n1, n)
    p2_eval = get_prior_class_prob(n2, n)

    # Оценка матожидания
    m11_eval = get_exp_val_eval(class1[0])
    m12_eval = get_exp_val_eval(class1[1])
    m21_eval = get_exp_val_eval(class2[0])
    m22_eval = get_exp_val_eval(class2[1])

    # Оценка дисперсии
    d11_eval = get_disp_eval(class1[0], m11_eval)
    d12_eval = get_disp_eval(class1[1], m12_eval)
    d21_eval = get_disp_eval(class2[0], m21_eval)
    d22_eval = get_disp_eval(class2[1], m22_eval)

    errors1, errors2 = classify(class1, class2, d11_eval, d12_eval, d21_eval, d22_eval, m11_eval, m12_eval, m21_eval,
                                m22_eval, p1_eval, p2_eval)
    mist_prob1 = get_prior_class_prob(errors1, n)
    mist_prob2 = get_prior_class_prob(errors2, n)
    mist_prob = mist_prob1 + mist_prob2


get_classifier_fault(1000, 4, 5, 5, 6, 10, 12, 15, 17, 0.5, 0.5, 1000)
