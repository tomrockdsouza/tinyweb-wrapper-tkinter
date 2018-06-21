from tkinter import *
from tkinter import ttk
import webbrowser
from tkinter import messagebox
from .cmd_manage import CommandManage


class TkinterApp:
    
    
    def __init__(self,master,port):
        #port NUMBER
        self._port = port
        self._master = master

        #make root non-resizable  frame
        self._master.title('TinkerServerCGI')
        self._master.resizable(
                False,
                False
                )

        #make a main subframe
        self.mainframe = Frame(self._master,
                                padx = 3, 
                                pady = 3
                                ) 
        self.mainframe.pack()
        #Start Stop Server Button
        self.start_stop_button = ttk.Button(
                                    self.mainframe,
                                    text = 'Start Server',
                                    command = self.start_server_button
                                    )                              
        self.start_stop_button.grid(
                row = 0,
                column = 0,
                pady = 3,
                padx = 3
                )
        #Launch Button
        self.launch_button = ttk.Button(
                                    self.mainframe,
                                    text = 'Launch App',
                                    state = DISABLED,
                                    command = self.launch_server_button
                                    )           
        self.launch_button.grid(
                row = 0,
                column = 1,
                pady = 3,
                padx = 3
                )
        #State Label
        self.state_label=Label(
                            self.mainframe,
                            text = '',
                            borderwidth = 2,
                            relief = SUNKEN,
                            background = 'white'
                            )    
        self.state_label.grid(
                    row = 1,
                    columnspan = 2,
                    pady = 3,
                    padx = 3,
                    ipady = 10,
                    sticky = 'wen'
                    )
        #playinitial state
        self.play_app_state()
        self._master.wm_iconbitmap('tkinterApp.ico')
        #assigns a function to define closing the app behaviour
        self._master.protocol(
            'WM_DELETE_WINDOW',
            self.on_closing
            )

            
    #when start or stop server button is pressed
    def start_server_button(self):
        OFF = 0
        ACTIVE = 2
        STATE = self.test_server_running()
        if STATE == ACTIVE:
            CommandManage.start_server(self._port,'%cd%\htdocs')
        elif STATE == OFF:
            CommandManage.kill_task()     
        self.play_app_state()
 

    def  app_template_change(
                self,
                start_server_button_text,
                launch_server_button_text,
                label_text,
                label_color
                ):
        self.start_stop_button.configure(
                    text = start_server_button_text
                    )
        self.launch_button.configure(
                    state = launch_server_button_text
                    )
        self.state_label.configure(
                    text = label_text,
                    foreground = label_color
                    )

                    
    #make changes app buttons and labels as per the current state
    def play_app_state(self):
        OFF = 0
        BUSY = 1
        ACTIVE = 2
        STATE = self.test_server_running()
        
        if STATE == OFF:
            self.app_template_change(
                    'Stop Server',
                    NORMAL,
                    'Application Active ('+str(self._port)+')',
                    'green'
                    )
        elif STATE == BUSY:
            self.app_template_change(
                    'Start Server',
                    DISABLED,
                    'Port ('+str(self._port)+') is busy',
                    'red'
                    )
        elif STATE == ACTIVE:
            self.app_template_change(
                    'Start Server',
                    DISABLED,
                    '',
                    'black'
                    )
        else:
            self.app_template_change(
                    'Stop Server',
                    NORMAL,
                    'Access Denied',
                    'red'
                    )
        

    #starts webpage in browser and minimizes the app
    def launch_server_button(self):
        webbrowser.open(
            'http://localhost:'+str(self._port)+'/',
            new = 2
            )
        self._master.wm_state('iconic')
    
    #when User clicks on close
    def on_closing(self):
        STATE = self.test_server_running()
        if STATE == 0:     # 0 = Server is Not Active
            self.deleteme()
        else:
            self._master.destroy()   
    
    
    #ask if you want to close the application when server is running    
    def deleteme(self):
        result = messagebox.askquestion(
                    'Close Application',
                    'Do you want close of the application?',
                    icon='warning'
                    )
        if result == 'yes':
            CommandManage.kill_task()
            self._master.destroy()
    
    #gets system state using few parameters
    def test_server_running(self):
        if CommandManage.search_task() and CommandManage.check_port(self._port):
            return 0    #signifies tiny.web is running on port
        elif CommandManage.check_port(self._port):
            return 1    #signifies port is busy
        else: 
            return 2    #signifies tiny.web is inactive

