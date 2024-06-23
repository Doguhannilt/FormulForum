from ui.interface import Ui_MainWindow
from PyQt5.QtWidgets import * 
from actions.read_config import MainConfig, SaveSettings
from actions.mongo_functions import get_collection_names, read_table_data
from actions.mail_functions import MainMail, CheckEmail

class ArticleFilterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.config_path = "./config.json"

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Menü buton tetikliyicileri
        self.ui.actionArticles.triggered.connect(self.ShowArticlesPage)
        self.ui.actionSettings.triggered.connect(self.ShowSettingsPage)
        self.ui.ConfirmBtn.clicked.connect(lambda: self.StatusBtnClicked("confirm"))
        self.ui.DenyBtn.clicked.connect(lambda: self.StatusBtnClicked("reject"))
        self.ui.SuspectBtn.clicked.connect(lambda: self.StatusBtnClicked("problem"))

        # Ayarlar Sayfası buton tetikliyicileri
        self.ui.SaveBtn.clicked.connect(self.SaveConfig)

        # Ayarlar Sayfası 'mongo input' tetikliyicisi
        self.ui.MongoInput.returnPressed.connect(self.ConnectMongo)
        result = MainConfig(self.config_path)
        if not result[0]:
            self.ShowArticlesPage()
        else:
            self.ShowSettingsPage()
            self.StatusBarShowMessage("Lütfen Ayarlarınızı Kaydedin", color="yellow", timeout=2000)


    def StatusBarShowMessage(self, message, color="white", timeout=3000):
        self.ui.statusbar.setStyleSheet(f"color: {color};")  # Metin rengini yeşil yapar
        self.ui.statusbar.showMessage(message, timeout)


    def ConnectMongo(self):
        #Veri tekrarnı önlemek için fonksiyon her çalıştığında combobox ları temizliyoruz
        self.ui.Table1Combo.clear()
        self.ui.Table2Combo.clear()
        #Girilen url den mongo ya bağlanıp tablo isimlerini çekmeye çalışıyorum
        self.ui.MongoInput.setDisabled(True)
        mongo_url = self.ui.MongoInput.text()
        try:
            result = get_collection_names(mongo_url)
            if result[0]:
                names = result[1]
                for name in names:
                    self.ui.Table1Combo.addItem(name)
                    self.ui.Table2Combo.addItem(name)
                self.StatusBarShowMessage("Tablo isimleri çekildi", color="green", timeout=2000)
            else:
                self.StatusBarShowMessage("Tablo isimleri çekilemedi", color="red", timeout=2000)
            
        except Exception as err:
            print(err)

        self.ui.MongoInput.setDisabled(False)

    def NextPost(self, data):
        if self.count < len(data) - 1:
            self.count += 1
            self.ui.PostTitle.setText(data[self.count]['title'])
            self.ui.PostContent.clear()
            self.ui.PostContent.appendPlainText(data[self.count]['text'])

        return self.count
    
    def BackPost(self, data):
        if self.count > 0:
            self.count -= 1
            self.ui.PostTitle.setText(data[self.count]['title'])
            self.ui.PostContent.clear()
            self.ui.PostContent.appendPlainText(data[self.count]['text'])

        return self.count

    def ShowArticlesPage(self):
        result = MainConfig(self.config_path)
        if not result[0]:
            self.ui.stackedWidget.setCurrentWidget(self.ui.ArticlesPage)
            mongo_url = result[1][2]
            table1 = result[1][3]
            result_data = read_table_data(mongo_url, table1)
            if result_data[0]:
                self.articles = result_data[1]
                self.count = -1
                self.NextPost(self.articles)
                self.StatusBarShowMessage(f"'{table1}'  İsimli Tablo Başarılı bir şekilde okundu", color="green", timeout=3000)
                self.ui.NextPostBtn.clicked.connect(lambda: self.NextPost(self.articles))
                self.ui.BackPostBtn.clicked.connect(lambda: self.BackPost(self.articles))
            else:
                self.StatusBarShowMessage(f"'{table1}'  İsimli Tablo Okunurken Bir Sorun Oluştu", color="red", timeout=3000)
        else:
            self.StatusBarShowMessage("Lütfen Ayarlarınızı Kaydedin", color="yellow", timeout=2000)   
    
    def ShowSettingsPage(self):
        #Veri tekrarnı önlemek için sayfa her açıldığında inputları temizliyoruz
        self.ui.EmailInput.clear()
        self.ui.PasswordInput.clear()
        self.ui.MongoInput.clear()
        self.ui.Table1Combo.clear()
        self.ui.Table2Combo.clear()

        result = MainConfig(self.config_path)
        self.ui.stackedWidget.setCurrentWidget(self.ui.SettingsPage)
        if not result[0]:
            self.ui.EmailInput.setText(result[1][0])
            self.ui.PasswordInput.setText(result[1][1])
            self.ui.MongoInput.setText(result[1][2])
            self.ui.Table1Combo.addItem(result[1][3])
            self.ui.Table1Combo.setCurrentIndex(0)
            self.ui.Table2Combo.addItem(result[1][4])
            self.ui.Table2Combo.setCurrentIndex(0)

    def SaveConfig(self):
        email = self.ui.EmailInput.text()
        password = self.ui.PasswordInput.text()
        mongo = self.ui.MongoInput.text()
        table1 = self.ui.Table1Combo.currentText()
        table2 = self.ui.Table2Combo.currentText()
        mail_result = CheckEmail(email, password)
        if len(email) > 0 and len(password) > 0 and len(mongo) > 0 and len(table1) > 0 and len(table2) > 0:
            if not mail_result:
                self.StatusBarShowMessage("E-Posta veya Parola hatalı", color="red", timeout=2000)
            else:
                result = SaveSettings(self.config_path, email, password, mongo, table1, table2)
                if not result[0]:
                    self.StatusBarShowMessage("Ayarlar kaydedilirken sorun oluştu", color="red", timeout=2000)
                else:
                    self.StatusBarShowMessage("Ayarlar başarıyla kaydedildi", color="green", timeout=2000)
        else:
            self.StatusBarShowMessage("Tüm kutuları doldurunuz", color="red", timeout=2000)

    def StatusBtnClicked(self, status):
        article = self.articles[self.count]
        result = MainConfig(self.config_path)
        if not result[0]:
            sender_email = result[1][0]
            password = result[1][1]
            receiver_email = article["mail"]
            article_content = f'{article["title"]}\n{article["text"]}'
            author = article["username"]
            MainMail(sender_email, password, receiver_email, article_content, author, status)

app = QApplication([])
window = ArticleFilterApp()
window.show()
app.exec_()