import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 300)
        MainWindow.setMinimumSize(600, 300)
        MainWindow.setWindowTitle("Employee Database")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_heading = QtWidgets.QLabel(self.centralwidget)
        self.label_heading.setGeometry(QtCore.QRect(120, 10, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_heading.setFont(font)
        self.label_heading.setAlignment(QtCore.Qt.AlignCenter)
        self.label_heading.setObjectName("label_heading")
        self.label_heading.setText("Python Lab EL - Employee Database")

        self.label_subheading = QtWidgets.QLabel(self.centralwidget)
        self.label_subheading.setGeometry(QtCore.QRect(120, 30, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_subheading.setFont(font)
        self.label_subheading.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subheading.setObjectName("label_subheading")
        self.label_subheading.setText("Made by Aakrisht Tiwary and Atharva Agarwal")

        self.label_note = QtWidgets.QLabel(self.centralwidget)
        self.label_note.setGeometry(QtCore.QRect(20, 240, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_note.setFont(font)
        self.label_note.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.label_note.setWordWrap(False)
        self.label_note.setObjectName("label_note")
        self.label_note.setText('''NOTE: To search for an employee record enter the 
            Employee ID and click on Search Employee''')

        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(20, 60, 65, 16))
        self.label_name.setObjectName("label_name")

        self.label_department = QtWidgets.QLabel(self.centralwidget)
        self.label_department.setGeometry(QtCore.QRect(20, 100, 91, 16))
        self.label_department.setObjectName("label_department")

        self.label_id = QtWidgets.QLabel(self.centralwidget)
        self.label_id.setGeometry(QtCore.QRect(20, 140, 71, 16))
        self.label_id.setObjectName("label_id")

        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(120, 60, 163, 22))
        self.lineEdit_name.setObjectName("lineEdit_name")

        self.lineEdit_department = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_department.setGeometry(QtCore.QRect(120, 100, 163, 22))
        self.lineEdit_department.setObjectName("lineEdit_department")

        self.lineEdit_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_id.setGeometry(QtCore.QRect(120, 140, 163, 22))
        self.lineEdit_id.setObjectName("lineEdit_id")

        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(70, 180, 151, 31))
        self.pushButton_add.setObjectName("pushButton_add")

        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search.setGeometry(QtCore.QRect(70, 210, 151, 31))
        self.pushButton_search.setObjectName("pushButton_search")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(300, 60, 281, 222))
        self.plainTextEdit.setObjectName("plainTextEdit")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Employee Database"))
        self.label_name.setText(_translate("MainWindow", "Name:"))
        self.label_department.setText(_translate("MainWindow", "Department:"))
        self.label_id.setText(_translate("MainWindow", "ID:"))
        self.pushButton_add.setText(_translate("MainWindow", "Add Employee"))
        self.pushButton_search.setText(_translate("MainWindow", "Search Employee"))

class EmployeeDatabaseApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.employee_data = {}

        self.pushButton_add.clicked.connect(self.add_employee)
        self.pushButton_search.clicked.connect(self.search_employee)

    def add_employee(self):
        name = self.lineEdit_name.text()
        department = self.lineEdit_department.text()
        id_number = self.lineEdit_id.text()

        if name and department and id_number:
            self.employee_data[id_number] = {"name": name, "department": department}
            self.plainTextEdit.appendPlainText(f"Employee added: ID: {id_number}, Name: {name}, Department: {department}")
            self.lineEdit_name.clear()
            self.lineEdit_department.clear()
            self.lineEdit_id.clear()
        else:
            self.plainTextEdit.appendPlainText("Please fill all fields")

    def search_employee(self):
        id_number = self.lineEdit_id.text()

        if id_number in self.employee_data:
            employee = self.employee_data[id_number]
            self.plainTextEdit.appendPlainText(
                f"Employee found: ID: {id_number}, Name: {employee['name']}, Department: {employee['department']}")
        else:
            self.plainTextEdit.appendPlainText(f"Employee with ID: {id_number} not found")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = EmployeeDatabaseApp()
    mainWindow.show()
    sys.exit(app.exec_())