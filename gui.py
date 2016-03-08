from datetime import datetime

import graph
from ui import Ui_Form
from сalculations import get_classifier_fault


class MainWindowSlots(Ui_Form):
    def calc(self):
        n = int(self.n.text())
        d1 = float(self.d11.text())
        d2 = float(self.d21.text())
        m1 = float(self.m11.text())
        m2 = float(self.m21.text())
        p1 = float(self.p1.text())
        k = int(self.k.text())
        c = float(self.c.text())
        q = float(self.q.text())
        core_type = self.core_type.currentIndex()
        res = get_classifier_fault(n, d1, d2, m1, m2, p1, k, c, q, core_type)
        self.m11_ev.setText(str(res['m11']))
        self.m21_ev.setText(str(res['m21']))
        self.d11_ev.setText(str(res['d11']))
        self.d21_ev.setText(str(res['d21']))
        self.p1_ev.setText(str(res['p1']))
        self.p2_ev.setText(str(res['p2']))
        self.n1_res.setText(str(res['n1']))
        self.n2_res.setText(str(res['n2']))
        self.p_mist1.setText(str(res['mist_prob1']))
        self.p_mist2.setText(str(res['mist_prob2']))
        self.p_mist.setText(str(res['mist_prob']))
        return None

    def set_time(self):
        # Получаем текущую метку времени в формате 'Ч:М:С'
        str_time = datetime.now().strftime('%H:%M:%S')
        # Присваиваем надписи на кнопке метку времени
        self.pushButton.setText(str_time)
        return None

    def graph_mistake_prob_n(self):
        d11 = float(self.d11.text())
        d12 = float(self.d12.text())
        d21 = float(self.d21.text())
        d22 = float(self.d22.text())
        m11 = float(self.m11.text())
        m12 = float(self.m12.text())
        m21 = float(self.m21.text())
        m22 = float(self.m22.text())
        p1 = float(self.p1.text())
        p2 = 1 - p1
        k = int(self.k.text())
        graph.mistake_prob_n(d11, d12, d21, d22, m11, m12, m21, m22, p1, p2, k)
        return None

    def graph_mistake_prob_p(self):
        n = int(self.n.text())
        d11 = float(self.d11.text())
        d12 = float(self.d12.text())
        d21 = float(self.d21.text())
        d22 = float(self.d22.text())
        m11 = float(self.m11.text())
        m12 = float(self.m12.text())
        m21 = float(self.m21.text())
        m22 = float(self.m22.text())
        k = int(self.k.text())
        graph.mistake_prob_p(n, d11, d12, d21, d22, m11, m12, m21, m22, k)
        return None

    def graph_mistake_prob_m(self):
        n = int(self.n.text())
        d11 = float(self.d11.text())
        d12 = float(self.d12.text())
        d21 = float(self.d21.text())
        d22 = float(self.d22.text())
        m11 = float(self.m11.text())
        m12 = float(self.m12.text())
        m21 = float(self.m21.text())
        m22 = float(self.m22.text())
        p1 = float(self.p1.text())
        p2 = 1 - p1
        k = int(self.k.text())
        graph.mistake_prob_m(n, d11, d12, d21, d22, m11, m12, m21, m22, p1, p2, k)
        return None

    def graph_mistake_prob_d(self):
        n = int(self.n.text())
        d11 = float(self.d11.text())
        d12 = float(self.d12.text())
        d21 = float(self.d21.text())
        d22 = float(self.d22.text())
        m11 = float(self.m11.text())
        m12 = float(self.m12.text())
        m21 = float(self.m21.text())
        m22 = float(self.m22.text())
        p1 = float(self.p1.text())
        p2 = 1 - p1
        k = int(self.k.text())
        graph.mistake_prob_d(n, d11, d12, d21, d22, m11, m12, m21, m22, p1, p2, k)
        return None
