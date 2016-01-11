from datetime import datetime

from ui import Ui_MainWindow


class MainWindowSlots(Ui_MainWindow):
    def calc(self):
        self.label_16.setText("LOOOOOOOOOOOOL")
        return None

    def set_time(self):
        # Получаем текущую метку времени в формате 'Ч:М:С'
        str_time = datetime.now().strftime('%H:%M:%S')
        # Присваиваем надписи на кнопке метку времени
        self.pushButton.setText(str_time)
        return None
