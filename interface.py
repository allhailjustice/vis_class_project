import sys
from graphlet import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt, QSize
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from utilities import test, training, clear

class App(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'Final Project'
        self.width = 1400
        self.height = 550
        self.initUI()
    
    def initUI(self):
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button1 = QPushButton('Training', self)
        button1.setStyleSheet("font: 20pt Comic Sans MS")
        button1.move(10,0)
        button1.resize(100,70)
        button1.clicked.connect(self.prepare)
        
        button2 = QPushButton('Test', self)
        button2.setStyleSheet("font: 20pt Comic Sans MS")
        button2.move(120,0)
        button2.resize(100,70)
        button2.clicked.connect(self.test)
        
        button3 = QPushButton('Clear', self)
        button3.setStyleSheet("font: 20pt Comic Sans MS")
        button3.move(230,0)
        button3.resize(100,70)
        button3.clicked.connect(self.clear)
        
        title1 = QLabel(self)
        title1.setText('Estimated Layout')
        title1.setStyleSheet("font: 30pt Comic Sans MS")
        title1.adjustSize()
        title1.move(650,15)
        
        title2 = QLabel(self)
        title2.setText('Real Layout')
        title2.setStyleSheet("font: 30pt Comic Sans MS")
        title2.adjustSize()
        title2.move(650,470)
        
        self.m1 = QLabel(self)
        self.m1.setPixmap(QPixmap(''))
        self.m1.adjustSize()
        self.m1.move(0,70)
        
        self.m2 = QLabel(self)
        self.m2.setPixmap(QPixmap(''))
        self.m2.adjustSize()
        self.m2.move(0,520)
        
        self.m3 = QLabel(self)
        self.m3.setPixmap(QPixmap(''))
        self.m3.adjustSize()
        self.m3.move(450,70)
        
        self.m4 = QLabel(self)
        self.m4.setPixmap(QPixmap(''))
        self.m4.adjustSize()
        self.m4.move(450,520)
        
        self.m5 = QLabel(self)
        self.m5.setPixmap(QPixmap(''))
        self.m5.adjustSize()
        self.m5.move(950,70)
        
        self.m6 = QLabel(self)
        self.m6.setPixmap(QPixmap(''))
        self.m6.adjustSize()
        self.m6.move(950,520)
        
        self.show()
    
    @pyqtSlot()
    def prepare(self):
        training()
    
    @pyqtSlot()
    def test(self):
        self.m1.hide()
        self.m2.hide()
        self.m3.hide()
        self.m4.hide()
        self.m5.hide()
        self.m6.hide()
        test()
        m1 = QLabel(self)
        m1.setPixmap(QPixmap('estimated_layout.png').scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        m1.adjustSize()
        m1.move(0,70)
        m2 = QLabel(self)
        m2.setPixmap(QPixmap('real_layout.png').scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        m2.adjustSize()
        m2.move(0,520)
        m3 = QLabel(self)
        m3.setPixmap(QPixmap('estimated_layout2.png').scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        m3.adjustSize()
        m3.move(450,70)
        m4 = QLabel(self)
        m4.setPixmap(QPixmap('real_layout2.png').scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        m4.adjustSize()
        m4.move(450,520)
        m5 = QLabel(self)
        m5.setPixmap(QPixmap('estimated_layout3.png').scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        m5.adjustSize()
        m5.move(950,70)
        m6 = QLabel(self)
        m6.setPixmap(QPixmap('real_layout3.png').scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        m6.adjustSize()
        m6.move(950,520)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5
        self.m6 = m6
        self.m1.show()
        self.m2.show()
        self.m3.show()
        self.m4.show()
        self.m5.show()
        self.m6.show()

    @pyqtSlot()
    def clear(self):
        self.m1.hide()
        self.m2.hide()
        clear()
        self.m1.setPixmap(QPixmap('estimated_layout.png'))
        self.m2.setPixmap(QPixmap('real_layout.png'))
        self.m1.show()
        self.m2.show()
        QApplication.processEvents()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
