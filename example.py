class ProgressBar(QDialog):
    def __init__(self,  parent=None):
        super(ProgressBar, self).__init__(parent)
        self.resize(500, 32) 
        self.progressBar = QProgressBar(self) 
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(99)  
        self.progressBar.setValue(0) 
        self.progressBar.setGeometry(QRect(1, 3, 499, 28)) 
        self.show()
    def setValue(self, value): 
        self.setWindowTitle(self.tr('Training...'))
        self.progressBar.setValue(value)
class pyqtbar():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.progressbar = ProgressBar() 
    def set_value(self,i):
        self.progressbar.setValue(i)
        QApplication.processEvents() 
    @property
    def close(self):
        self.progressbar.close()  
        self.app.exit()
class update_bar(QThread):
    def __init__(self,bar):
        super().__init__()
        self.bar = bar
        self.sig = 0
    def update(self,progress):
        self.bar.set_value(progress)
    def close(self):
        self.bar.progressbar.close() 
        self.bar.app.exit()
        
# The following only provides the core code, do not run directly
class example():
  self.bar = pyqtbar()
  self.thread_bar = update_bar(self.bar)
  self.thread_trn = Thread_trn()
  self.thread_trn.start(priority=QThread.HighestPriority)
  self.thread_trn._signal.connect(self.thread_bar.update)
  
