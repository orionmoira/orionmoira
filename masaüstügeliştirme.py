import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QMessageBox, QFormLayout
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class LoginScreen(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Giriş Ekranı')

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        layout = QFormLayout()
        layout.addRow('Kullanıcı Adı:', self.username_input)
        layout.addRow('Şifre:', self.password_input)

        login_button = QPushButton('Giriş Yap')
        login_button.clicked.connect(self.login)

        layout.addRow(login_button)

        self.setLayout(layout)

    def login(self):
        # Burada gerçek bir kimlik doğrulama yapılması gerekebilir.
        # Bu örnekte sadece basit bir kontrol yapılıyor.
        if self.username_input.text() == 'kullanici' and self.password_input.text() == 'sifre':
            self.main_app.show_main_page()
            self.close()
        else:
            QMessageBox.warning(self, 'Hata', 'Kullanıcı adı veya şifre hatalı', QMessageBox.Ok)


class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Ana Sayfa')

        bmi_label = QLabel('Vücut Kitle İndeksi (BMI) Hesapla')

        self.height_input = QLineEdit()
        self.weight_input = QLineEdit()

        calculate_button = QPushButton('Hesapla')
        calculate_button.clicked.connect(self.calculate_bmi)

        layout = QVBoxLayout()
        layout.addWidget(bmi_label)
        layout.addWidget(QLabel('Boy (cm):'))
        layout.addWidget(self.height_input)
        layout.addWidget(QLabel('Kilo (kg):'))
        layout.addWidget(self.weight_input)
        layout.addWidget(calculate_button)

        self.setLayout(layout)

    def calculate_bmi(self):
        height = float(self.height_input.text()) / 100  # Boyu metre cinsine çevir
        weight = float(self.weight_input.text())

        bmi = weight / (height ** 2)

        QMessageBox.information(self, 'BMI Sonucu', f'Vücut Kitle İndeksi (BMI): {bmi:.2f}', QMessageBox.Ok)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.login_screen = LoginScreen(self)
        self.main_page = MainPage()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('PyQt Uygulaması')
        self.setGeometry(100, 100, 400, 300)

        # Veritabanını başlat
        self.init_database()

        # Uygulama başladığında giriş ekranını göster
        self.login_screen.show()

    def init_database(self):
        # SQLite veritabanını başlat
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('data.db')

        if not db.open():
            QMessageBox.critical(None, 'Hata', 'Veritabanına bağlanılamadı', QMessageBox.Ok)
            sys.exit(1)

        # Tabloyu oluştur
        query = QSqlQuery()
        query.exec_("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")

    def show_main_page(self):
        # Giriş başarılıysa ana sayfayı göster
        self.login_screen.close()
        self.main_page.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = MyApp()
    sys.exit(app.exec_())
