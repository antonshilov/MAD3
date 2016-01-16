import matplotlib.pyplot as plt

import сalculations as calc


def mistake_prob_n(d11, d12, d21, d22, m11, m12, m21, m22, p1, p2, k):
    data = [[], []]
    for i in range(5, 400):
        n = i * 2
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


def mistake_prob_m(n, d11, d12, d21, d22, m11, m12, m21, m22, p1, p2, k):
    data = [[], []]
    m21_ch = m21
    for i in range(1, 100):
        m21_ch += 0.2
        data[0].append(m21_ch - m11)
        data[1].append(
                calc.get_classifier_fault(n, d11, d12, d21, d22, m11, m12, m21_ch, m22, p1, p2, k)['mist_prob'])
    plt.plot(data[0], data[1], '-')
    print(data[0])
    print(data[1])
    plt.show()


def mistake_prob_d(n, d11, d12, d21, d22, m11, m12, m21, m22, p1, p2, k):
    data = [[], []]
    d21_ch = d21
    for i in range(1, 80):
        d21_ch += 0.1
        data[0].append(d21_ch - d11)
        res = 0
        for j in range(10):
            res += calc.get_classifier_fault(n, d11, d12, d21_ch, d22, m11, m12, m21, m22, p1, p2, k)['mist_prob']
        res /= 25
        data[1].append(res)
    plt.plot(data[0], data[1], '-')
    print(data[0])
    print(data[1])
    plt.show()

# mistake_prob_d(1000, 4, 5, 5, 6, 10, 12, 15, 17, 0.5, 0.5, 1000)
# mistake_prob_p(1000, 4, 5, 5, 6, 10, 12, 15, 17, 1000, )
