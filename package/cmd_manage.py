import os, sys

class CommandManage:
    
            
    #kills any instances of tiny.exe
    @staticmethod
    def kill_task():
        KILL_TASK = 'taskkill /f /im tiny.exe | find "SUCCESS"'
        process = os.popen(KILL_TASK,'r',1)
        value=len(process.read())>0
        process.close()
        return value

        
    #searches if any instances of tiny.exe is running
    @staticmethod
    def search_task():
        SEARCH_TASK = 'TASKLIST /FI "IMAGENAME eq tiny.exe" | find "tiny.exe"'
        process = os.popen(SEARCH_TASK,'r',1)
        value=len(process.read())>0
        process.close()
        return value

        
    #starts server on the given port
    @staticmethod
    def start_server(port,path):
        START_SERVER = 'start tiny.exe '+path+' '+str(port)
        os.popen(START_SERVER,'r',1).close()

        
    #checks if the port is busy listening
    @staticmethod
    def check_port(port):
        PORT_CHECK = 'netstat -an | find "LISTENING" | find ":'+str(port)+'"'
        process = os.popen(PORT_CHECK,'r',1)
        value=len(process.read())>0
        process.close()
        return value
    


    
        