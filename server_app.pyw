from tendo import singleton
import ctypes
import sys
from package.tkinter_app import *


#ensures only one instance of this script is running
me = singleton.SingleInstance()



def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# If not admin run as admin and close script
if not is_admin():
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, __file__, None, 1)
    exit()


# Embed ico in the app icon
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

#Start tkinter app
root=Tk()
PORT=8000
tkinterapp= TkinterApp(root,PORT)
root.mainloop()

