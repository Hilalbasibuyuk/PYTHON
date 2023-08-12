

import sys
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import pyqtSlot

@pyqtSlot() # @pyqtSlot() dekoratörü, PyQt'da sinyal ve yuva (slot) bağlantılarını yönetmek için kullanılır.
def say_hello():
 print("Button clicked, Hello!")


app = QApplication(sys.argv)
button = QPushButton("Click me")
button.clicked.connect(say_hello)
button.show()

app.exec()