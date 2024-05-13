from ui.interface import Ui_MainWindow
from PyQt5.QtWidgets import * 
from PyQt5.uic import loadUi

class ArticleFilterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionArticles.triggered.connect(self.show_articles_page)
        self.ui.actionSettings.triggered.connect(self.show_settings_page)




    def show_articles_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ArticlesPage)
    
    def show_settings_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.SettingsPage)


app = QApplication([])
window = ArticleFilterApp()
window.show()
app.exec_()