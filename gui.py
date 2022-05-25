from PyQt5 import uic, QtWidgets
import userconfigs
import os

app = QtWidgets.QApplication([])
form = uic.loadUi('./PixBOT_GUI.ui')

form.username.setText(userconfigs.username)
form.password.setText(userconfigs.password)
form.link_sorteio.setText(userconfigs.link_sorteio)

        

def Save():
    username = form.username.text()
    password = form.password.text()
    link_sorteio = form.link_sorteio.text()
    
    configs = [username, password, link_sorteio]
    
    with open('userconfigs.py', 'w+') as user:
        user.write("username = '" + configs[0])
        user.write("'\npassword = '" + configs[1])
        user.write("'\nlink_sorteio = '" + configs[2] + "'")
        
    print("Novo Usuário Salvo")
    
def Executar():
    form.close()
    os.system('Executar.bat')


form.btnSalvar.clicked.connect(Save)
form.btnExecutar.clicked.connect(Executar)

form.show()
app.exec()