import matplotlib.pyplot as plt

import Calculations as calc


def mistake_prob_n(d11, d12, d21, d22, m11, m12, m21, m22, p1, p2, k):
    data = [[], []]
    for i in range(1, 20):
        n = i * 40
        data[0].append(n)
        data[1].append(
                calc.get_classifier_fault(n, d11, d12, d21, d22, m11, m12, m21, m22, p1, p2, k)['mist_prob'])
    plt.plot(data[0], data[1], '-')
    print(data[0])
    print(data[1])
    plt.show()


def mistake_prob_p(n, d11, d12, d21, d22, m11, m12, m21, m22, k):
    data = [[], []]
    for i in range(1, 100):
        p1 = i / 100
        p2 = 1 - p1
        data[0].append(p1)
        data[1].append(
                calc.get_classifier_fault(n, d11, d12, d21, d22, m11, m12, m21, m22, p1, p2, k)['mist_prob'])
    plt.plot(data[0], data[1], '-')
    print(data[0])
    print(data[1])
    plt.show()


mistake_prob_n(4, 5, 5, 6, 10, 12, 15, 17, 0.5, 0.5, 1000)
mistake_prob_p(1000, 4, 5, 5, 6, 10, 12, 15, 17, 1000, )
