import matplotlib.pyplot as plt
from matplotlib import interactive

import сalculations as calc


def mistake_prob_n(d11, d21, m11, m21, p1, k, c, q, core_type):
    data = [[0.], [0.]]
    for i in range(10, 110):
        n = i
        data[0].append(n)
        res = 0
        for j in range(10):
            res += calc.get_classifier_fault(n, d11, d21, m11, m21, p1, k, c, q, core_type)['mist_prob']
        res /= 10
        data[1].append(res)
    plt.plot(data[0], data[1], '-')
    print(data[0])
    print(data[1])
    plt.show()


def mistake_prob_p(n, d11, d21, m11, m21, k, c, q, core_type):
    data = [[], []]
    for i in range(10, 90):
        p1 = i / 100
        p2 = 1 - p1
        data[0].append(p1)
        res = 0
        for j in range(10):
            res += calc.get_classifier_fault(n, d11, d21, m11, m21, p1, k, c, q, core_type)['mist_prob']
        res /= 10
        data[1].append(res)
    plt.plot(data[0], data[1], '-')
    print(data[0])
    print(data[1])
    plt.show()


def mistake_prob_h(n, d11, d21, m11, m21, p1, k, core_type):
    data = [[], []]
    for i in range(1, 100):
        h = i / 100
        data[0].append(h)
        res = 0
        for j in range(10):
            res += calc.get_classifier_fault(n, d11, d21, m11, m21, p1, k, h, 0, core_type)['mist_prob']
        res /= 10
        data[1].append(res)
    plt.plot(data[0], data[1], '-')
    print(data[0])
    print(data[1])
    plt.show()


def prop_density_core(n, d11, d21, m11, m21, p1, k, c, q):
    interactive(False)
    n1, n2 = calc.generate_amount(p1, n)
    class1 = calc.generate_clt(m11, d11, n1, k)
    class2 = calc.generate_clt(m21, d21, n2, k)
    class1.sort()
    class2.sort()
    h = c * (n ** (-q))
    # Ядра
    for core_type in calc.core_types.values():
        data = []
        for el in class1:
            res = 0
            for i in range(10):
                res += calc.get_prob_density(class1, el, h, core_type)
            data.append((el, res / 10))
        for el in class2:
            res = 0
            for i in range(10):
                res += calc.get_prob_density(class2, el, h, core_type)
            data.append((el, res / 10))

        # data = sorted(data, key=lambda el: el[0])
        plt.plot(*zip(*data))

    data = []
    for el in class1:
        res = calc.normal_distribution_prob_density(el, m11, d11)
        data.append((el, res))
    for el in class2:
        res = calc.normal_distribution_prob_density(el, m21, d21)
        data.append((el, res))

    # data = sorted(data, key=lambda el: el[0])
    plt.plot(*zip(*data))

    plt.xlabel('X')
    plt.ylabel('f(x|1)')
    plt.legend(['rect', 'tri', 'epan', 'gauss', 'quad', 'normal dist'], loc='upper left')
    plt.show()

#
# def prop_density_core(n, d11, d21, m11, m21, p1, k, c, q):
#     interactive(False)
#     n1, n2 = calc.generate_amount(p1, n)
#     class1 = calc.generate_clt(m11, d11, n1, k)
#     class2 = calc.generate_clt(m21, d21, n2, k)
#     h = c * (n ** (-q))
#     for core_type in calc.core_types.values():
#         data = []
#         for el in class1:
#             data[0].append(el)
#             res = 0
#             for i in range(10):
#                 res += calc.get_prob_density(class1, el, h, core_type)
#             data[1].append(res / 10)
#         # for el in class2:
#         #     data[0].append(el)
#         #     res = 0
#         #     for i in range(10):
#         #         res += calc.get_prob_density(class2, el, h, core_type)
#         #     data[1].append(res / 10)
#         print(data[0])
#         print(data[1])
#         data[0].sort()
#         plt.plot(data[0], data[1])
#     plt.legend(['rect', 'tri', 'epan', 'gauss', 'quad'], loc='upper left')
#     plt.show()

# mistake_prob_d(1000, 4, 5, 5, 6, 10, 12, 15, 17, 0.5, 0.5, 1000)
# mistake_prob_p(1000, 4, 5, 5, 6, 10, 12, 15, 17, 1000, )
