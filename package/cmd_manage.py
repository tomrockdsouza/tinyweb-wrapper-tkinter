import os, sys

class CommandManage:
    
    def __init__(self,port):
        self.port=port
    
    def test_server_running(self):
        if self.search_task() and self.check_port():
            return 0 #signifies tiny.web is running on port
        elif self.check_port():
            return 1 #signifies port is busy
        else: 
            return 2 #signifies tiny.web is inactive

    #kills any instances of tiny.exe
    def kill_task(self):
        KILL_TASK = 'taskkill /f /im tiny.exe | find "SUCCESS"'
        process = os.popen(KILL_TASK,'r',1)
        value=len(process.read())>0
        process.close()
        return value

    #searches if any instances of tiny.exe is running
    def search_task(self):
        SEARCH_TASK = 'TASKLIST /FI "IMAGENAME eq tiny.exe" | find "tiny.exe"'
        process = os.popen(SEARCH_TASK,'r',1)
        value=len(process.read())>0
        process.close()
        return value

    #starts server on the given port
    def start_server(self):
        START_SERVER = 'start tiny.exe %cd%\htdocs '+str(self.port)
        os.popen(START_SERVER,'r',1).close()

    #checks if the port is busy listening
    def check_port(self):
        PORT_CHECK = 'netstat -an | find "LISTENING" | find ":'+str(self.port)+'"'
        process = os.popen(PORT_CHECK,'r',1)
        value=len(process.read())>0
        process.close()
        return value
    


    
        