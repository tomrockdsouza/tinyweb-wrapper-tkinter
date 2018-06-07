
#ensures only one instance of this script is running
from tendo import singleton
me = singleton.SingleInstance()


import ctypes, sys
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# If not admin run as admin and close script
if not is_admin():
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    exit()


# Embed ico in the app icon
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

#import the tkinter app
from package.tkinter_app import *
root=Tk()
PORT=8000
tkinterapp= TkinterApp(root,PORT)
root.mainloop()

