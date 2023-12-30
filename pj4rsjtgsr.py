from PyQt6.QtWidgets import *

class An (method) tiklama: (self: Self@AnaPencere -> None
    def tiklama(self):
        alert = QMessageBox()
        alert.setText("Tıkladın!")
        alert.exec()

    def__init__(self):
        super().__init__()

        yatayicerik = QHBoxLayout()
        dikeyicerik1 = QVBoxLayout()
        dikeyicerik2 = QVBoxLayout()
        dikeyicerik3 = QVBoxLayout()
        dikeyicerik4 = QVBoxLayout()

        dikeyicerik1.addWidget(QPushButton("Dene"))
        buton1 = QPushButton("Tıkla")
        buton.clicked.connect(self.tiklama)

        dikeyicerik4.addWidget(QLabel("Label widgeti"))

        dikeyicerik1.addWidget(buton1)
        dikeyicerik1.addWidget(QPushButton("Buton3"))
