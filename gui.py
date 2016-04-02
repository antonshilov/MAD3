import graph
from ui import Ui_Form
from сalculations import get_classifier_fault, get_opt_h


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
        is_h_opt = self.is_h_opt.isChecked()
        if is_h_opt:
            res = get_opt_h(n, d1, d2, m1, m2, p1, k, core_type)
            self.h.setText(str(res['h']))
        else:
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

    def graph_mistake_prob_n(self):
        d11 = float(self.d11.text())
        d21 = float(self.d21.text())
        m11 = float(self.m11.text())
        m21 = float(self.m21.text())
        p1 = float(self.p1.text())
        k = int(self.k.text())
        c = float(self.c.text())
        q = float(self.q.text())
        core_type = self.core_type.currentIndex()
        graph.mistake_prob_n(d11, d21, m11, m21, p1, k, c, q, core_type)
        return None

    def graph_mistake_prob_p(self):
        n = int(self.n.text())
        d11 = float(self.d11.text())
        d21 = float(self.d21.text())
        m11 = float(self.m11.text())
        m21 = float(self.m21.text())
        k = int(self.k.text())
        c = float(self.c.text())
        q = float(self.q.text())
        core_type = self.core_type.currentIndex()
        graph.mistake_prob_p(n, d11, d21, m11, m21, k, c, q, core_type)
        return None

    def graph_mistake_prob_h(self):
        n = int(self.n.text())
        d11 = float(self.d11.text())
        d21 = float(self.d21.text())
        m11 = float(self.m11.text())
        m21 = float(self.m21.text())
        p1 = float(self.p1.text())
        k = int(self.k.text())
        core_type = self.core_type.currentIndex()
        graph.mistake_prob_h(n, d11, d21, m11, m21, p1, k, core_type)
        return None

    def graph_prob_density_core(self):
        n = int(self.n.text())
        d11 = float(self.d11.text())
        d21 = float(self.d21.text())
        m11 = float(self.m11.text())
        m21 = float(self.m21.text())
        p1 = float(self.p1.text())
        k = int(self.k.text())
        c = float(self.c.text())
        q = float(self.q.text())
        core_type = self.core_type.currentIndex()
        graph.prob_density_core(n, d11, d21, m11, m21, p1, k, c, q, core_type)
        return None
