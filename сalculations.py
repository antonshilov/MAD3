import pprint
from math import sqrt, log, exp, pi
from random import random, uniform

pp = pprint.PrettyPrinter(indent=4)
# http://www.machinelearning.ru/wiki/index.php?title=%D0%AF%D0%B4%D0%B5%D1%80%D0%BD%D0%BE%D0%B5_%D1%81%D0%B3%D0%BB%D0%B0%D0%B6%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5
core_types = {'rect': 0, 'tri': 1, 'epan': 2, 'gauss': 3, 'quad': 4}


def generate_mpc(m1, d1, m2, d2, n):
    v1 = v2 = 0.
    s = 1
    result = [[], []]
    for i in range(n):
        while not 0 < s < 1:
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


def generate_clt(m, d, n, k):
    result = []
    for i in range(n):
        value = 0.
        for j in range(k):
            value += random() - 0.5
        value *= sqrt(d) * sqrt(12 / k)
        value += m
        result.append(value)
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
def calc_core(core_type, x):
    result = 0.
    val = abs(x)
    if core_type == core_types['rect']:
        if val <= 1:
            return 0.5
    elif core_type == core_types['tri']:
        if val <= 1:
            return 1 - x
    elif core_type == core_types['epan']:
        if val <= 1:
            return 0.75 * (1 - x ** 2)
    elif core_type == core_types['gauss']:
        if val <= 1:
            return ((2 * pi) ** (-0.5)) * exp(-(x ** 2) / 2)
    elif core_type == core_types['quad']:
        if val <= 1:
            return (15 / 16) * (1 - x ** 2)
    return result


def get_prob_density(sample, val, h, core_type):
    res = 0
    for el in sample:
        x = (val - el) / h
        res += (1 / h) * calc_core(core_type, x)
    return res / len(sample)


def classify(class1, class2, core_type, c, q):
    errors1 = errors2 = 0
    sample_len = len(class1) + len(class2)
    p1_eval = get_prior_class_prob(len(class1), sample_len)
    p2_eval = get_prior_class_prob(len(class2), sample_len)
    h = c * (sample_len ** (-q))

    for el in class1:
        density1 = get_prob_density(class1, el, h, core_type)
        density2 = get_prob_density(class2, el, h, core_type)
        result = density1 * p1_eval - density2 * p2_eval
        if result < 0:
            errors1 += 1
    for el in class2:
        density1 = get_prob_density(class1, el, h, core_type)
        density2 = get_prob_density(class2, el, h, core_type)
        result = density1 * p1_eval - density2 * p2_eval
        if result > 0:
            errors2 += 1
    return errors1, errors2


def get_classifier_fault(n, d11, d21, m11, m21, p1, k, c, q, core_type):
    # Размеры выборок для классов
    n1, n2 = generate_amount(p1, n)

    # Генерируем выборки МПК
    # if k >= 12:
    class1 = generate_clt(m11, d11, n1, k)
    class2 = generate_clt(m21, d21, n2, k)
    # else:
    #     class1 = generate_mpc(m11, d11, m12, d12, n1)
    #     class2 = generate_mpc(m21, d21, m22, d22, n2)

    # Оценка априорной вероятности
    p1_eval = get_prior_class_prob(n1, n)
    p2_eval = get_prior_class_prob(n2, n)

    # Оценка матожидания
    m1_eval = get_exp_val_eval(class1)
    m2_eval = get_exp_val_eval(class2)

    # Оценка дисперсии
    d1_eval = get_disp_eval(class1, m1_eval)
    d2_eval = get_disp_eval(class2, m2_eval)

    errors1, errors2 = classify(class1, class2, core_type, c, q)
    mist_prob1 = get_prior_class_prob(errors1, n)
    mist_prob2 = get_prior_class_prob(errors2, n)
    mist_prob = mist_prob1 + mist_prob2
    return {'n1': n1, 'n2': n2, 'p1': p1_eval, 'p2': p2_eval, 'm11': m1_eval, 'm21': m2_eval,
            'd11': d1_eval, 'd21': d2_eval,
            'mist_prob1': mist_prob1, 'mist_prob2': mist_prob2, 'mist_prob': mist_prob}


def get_opt_h(n, d11, d21, m11, m21, p1, k, core_type):
    n1, n2 = generate_amount(p1, n)

    # Генерируем выборки МПК
    # if k >= 12:
    class1 = generate_clt(m11, d11, n1, k)
    class2 = generate_clt(m21, d21, n2, k)
    # else:
    #     class1 = generate_mpc(m11, d11, m12, d12, n1)
    #     class2 = generate_mpc(m21, d21, m22, d22, n2)

    # Оценка априорной вероятности
    p1_eval = get_prior_class_prob(n1, n)
    p2_eval = get_prior_class_prob(n2, n)

    # Оценка матожидания
    m1_eval = get_exp_val_eval(class1)
    m2_eval = get_exp_val_eval(class2)

    # Оценка дисперсии
    d1_eval = get_disp_eval(class1, m1_eval)
    d2_eval = get_disp_eval(class2, m2_eval)
    a = 0
    b = 1
    l = b - a
    m = (a + b) / 2
    res = tuple()
    res_m = 0
    while l > 0.001:
        h1 = a + l / 4
        h2 = b - l / 4
        res1 = classify(class1, class2, core_type, h1, 0)
        res1 = sum(res1)
        res2 = classify(class1, class2, core_type, h2, 0)
        res2 = sum(res2)
        res = classify(class1, class2, core_type, m, 0)
        res_m = sum(res)
        if res1 < res_m:
            b = m
            m = h1
        elif res_m > res2:
            a = m
            m = h2
        else:
            a = h1
            b = h2
        l = b - a
    mist_prob1 = get_prior_class_prob(res[0], n)
    mist_prob2 = get_prior_class_prob(res[1], n)
    mist_prob = mist_prob1 + mist_prob2
    return {'n1': n1, 'n2': n2, 'p1': p1_eval, 'p2': p2_eval, 'm11': m1_eval, 'm21': m2_eval,
            'd11': d1_eval, 'd21': d2_eval,
            'mist_prob1': mist_prob1, 'mist_prob2': mist_prob2, 'mist_prob': mist_prob, 'h': m}


def normal_distribution_prob_density(x, m, d):
    res = -((x - m) ** 2 / (2 * d))
    res = exp(res) / (sqrt(d * 2 * pi))
    return res

# get_opt_h(100, 2, 2, 10, 12, 0.4, 12, 3)
