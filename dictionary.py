import sys
from vocabulary.vocabulary import Vocabulary as vb

from PySide.QtCore import *
from PySide.QtGui import *

from ui_dictionary import  Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		




if __name__== '__main__':
	app = QApplication(sys.argv)
	frame = MainWindow()
	textEdit = vb.meaning(lineEdit)
	frame.show()
	sys.exit( app.exec_() )


