from ctypes import *
from my_debugger_defines import *

class Debugger :

    def __init__(self):
	    self.handle = -1
            self.kernel32 = windll.kernel32
            self.pid = -1
		 
    def start_process(self,path_to_exe):
     
	    startupinf = STARTUPINFO()
	    startupinf.dwFlags = 0x1
	    startupinf.wShowWindow = 0x0
	    startupinf.cb = sizeof(startupinf)
		
	    processinf = PROCESS_INFORMATION()
		
	    creation_flags = DEBUG_PROCESS
		
	   
	    if (self.kernel32.CreateProcessA(path_to_exe,None,None,None,None,creation_flags,None,None,byref(startupinf),byref(processinf))):
		    print "[*] Process launched successfully !"
		    print "[*] PID : %d" % processinf.dwProcessId
                    self.pid = processinf.dwProcessId
	    else:
		    print "[*] Error while launching process : ox%08x." % kernel32.GetLastError()
        
            process_handle = self.kernel32.OpenProcess(PROCESS_ALL_ACCESS,False,self.pid)
        
            if process_handle: 
                print "[*] Handle on the process retrieved %d " % process_handle
                self.handle = process_handle
            else:
                print "[*] Failed to retrieve the handle for the process %d" % processing.dwProcessId


    def attach_process(self):
        if self.kernel32.DebugActiveProcess(self.pid):
            print "[*] Process successfully attached"
        else :
            print "[*] Failed to attach process ox%08x." % self.kernel32.GetLastError()

    def debug_process(self):
        debug_event = DEBUG_EVENT()
        if self.kernel32.WaitForDebugEvent(debug_event,INFINITE):
            print "[*] Debugging started"
        else :
            print "[*] Debugging failed ox%08x." % self.kernel32.GetLastError()

    

        
                
