from tkinter import *
from tkinter import ttk
import webbrowser
from tkinter import messagebox
from .cmd_manage import *


class TkinterApp:
    
    OFF=0
    BUSY=1
    ACTIVE=2
    DENIED=3

    def __init__(self,master,port):
        #port NUMBER
        self.port=port
        #root object
        self.master=master

        #comand prompt object manager
        self.cmd=CommandManage(port)

        #get app state
        self.APP_STATE = self.cmd.test_server_running()

        self.master.title("TinkerServerCGI")
        self.master.resizable(False, False)

        # create a non-resizable Sub Frame
        self.mainframe = Frame(self.master,padx=3, pady=3) 
        self.mainframe.pack()
        
        #Start Stop Server Button
        self.start_stop_button = ttk.Button(self.mainframe,text="Start Server" ,command=self.start_server_button)
        self.start_stop_button.grid(row=0,column=0,pady=3,padx=3)

        #Launch Button
        self.launch_button = ttk.Button(self.mainframe,text="Launch App",state=DISABLED,command=self.launch_server_button)
        self.launch_button.grid(row=0,column=1,pady=3,padx=3)

        #State Label
        self.state_label=Label(self.mainframe,text="",borderwidth=2,relief=SUNKEN,background="white")
        self.state_label.grid(row=1,columnspan=2,pady=3,padx=3,ipady=10,sticky='wen')

        #playinitial state
        self.play_app_state()
        master.wm_iconbitmap("tkinterApp.ico")

        #assigns a function to define closing the app behaviour
        master.protocol("WM_DELETE_WINDOW", self.on_closing)
 
    #when start or stop server button is pressed
    def start_server_button(self):
        self.APP_STATE = self.cmd.test_server_running()
        if self.APP_STATE == self.ACTIVE:
            self.cmd.start_server()
            self.APP_STATE=self.cmd.test_server_running()
            self.play_app_state()
        elif self.APP_STATE == self.OFF:
            self.cmd.kill_task()
            self.APP_STATE=self.cmd.test_server_running()
            if self.APP_STATE==self.OFF:
                self.play_app_state(self.DENIED)
            else:
                self.play_app_state()
        else:
            self.play_app_state()
 

    def  app_template_change(self,ssbText,lbState,labelText,labelcolor):
        self.start_stop_button.configure(text=ssbText)
        self.launch_button.configure(state=lbState)
        self.state_label.configure(text=labelText,foreground=labelcolor)

    #make changes to the app as per the current state
    def play_app_state(self):
        server_state=self.APP_STATE
        if server_state==self.OFF:
            self.app_template_change("Stop Server",NORMAL,"Application Active ("+str(self.port)+")","green")
        elif server_state==self.BUSY:
            self.app_template_change("Start Server",DISABLED,"Port ("+str(self.port)+") is busy","red")
        elif server_state==self.ACTIVE:
            self.app_template_change("Start Server",DISABLED,"","black")
        else:
            self.app_template_change("Stop Server",NORMAL,"Access Denied","red")
        
    
            
    #start webpage is browser and minimize the app
    def launch_server_button(self):
        webbrowser.open('http://localhost:8000/', new = 2)
        self.master.wm_state('iconic')

    def on_closing(self):
        self.APP_STATE=self.cmd.test_server_running()
        if self.APP_STATE==0:
            self.deleteme()
        else:
            self.master.destroy()        
    #ask if you want to close the application when server is running    
    def deleteme(self):
        result = messagebox.askquestion("Close Application", "Do you want close of the application?", icon='warning')
        if result == 'yes':
            self.cmd.kill_task()
            self.master.destroy()



