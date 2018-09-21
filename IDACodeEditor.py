
# threading
import threading

# socket
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket


# idaapi
from idaapi import *
from idc import *

PORT = 8000

def WriteFileScript(code):
    
    try:
        # ida dir
        path_ida = idaapi.idadir("plugins\\IDACodeEditor")

        # Write file folder 
        file = open(path_ida + "\\code.py", "w")
        file.write(code)    # write
        file.close()        # close

        # Execute Script
        ExecuteFileScript()
    except:
        print "[ERROR] Error Write File"


def ExecuteFileScript():
    
    g = globals()

    try:
    
        # ida dir
        path_ida = idaapi.idadir("plugins\\IDACodeEditor")

        # Execute
        IDAPython_ExecScript(path_ida + "\\code.py", g)

    except:
        print "[ERROR] Error Execute Script"

class WSHandler(tornado.websocket.WebSocketHandler):
    
    def on_message(self, message):
        print "Done!"
        WriteFileScript(message)

    def check_origin(self, origin):
        return True
 
application = tornado.web.Application([
    (r'/ws', WSHandler),
])

def StartServer():
    
    print "IDA Code Editor | Dev Bym24v"

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(PORT)

    #myIP = socket.gethostbyname(socket.gethostname())
    print ".:: Server Started ::.\n"

    tornado.ioloop.IOLoop.instance().start()


class IDACodeEditor(idaapi.plugin_t):
    
    # settings plugin
    flags = idaapi.PLUGIN_UNL
    comment = "IDA Code Editor"
    help = "IDA Code Editor"
    wanted_name = "IDA Code Editor"
    wanted_hotkey = 'Ctrl-z'

    # init
    def init(self):
        return idaapi.PLUGIN_OK

    # Run new Thread
    def run(self, arg):
        t = threading.Thread(target=StartServer)
        t.daemon = True
        t.start()

    def term(self):
        pass

def PLUGIN_ENTRY():
    return IDACodeEditor()

if __name__ == "__main__":
    PLUGIN_ENTRY()