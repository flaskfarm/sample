from .setup import *

name = 'pages'  

class ModulePages(PluginModuleBase):

    def __init__(self, P):
        super(ModulePages, self).__init__(P, name=name, first_menu='page1')
        self.set_page_list([Page1])

    def process_command(self, command, arg1, arg2, arg3, req):
        return jsonify('')
            



class Page1(PluginPageBase):
    def __init__(self, P, parent):
        super(Page1, self).__init__(P, parent, name='page1', scheduler_desc="페이지 스케쥴링")

        self.db_default = {
            f'{self.parent.name}_{self.name}_db_version' : '1',
            f'{self.parent.name}_{self.name}_auto_start' : 'True',
            f'{self.parent.name}_{self.name}_interval' : '10',
        }
        default_route_socketio_page(self)

    def process_menu(self, req):
        title = "Page1 : 페이지 단위에서 스케쥴러, socketio 사용"
        return render_template('sample.html', title=title)


    def process_ajax(self, sub, req):
        pass

    def scheduler_function(self):
        data = {'type':'info', 'msg' : "Page1 scheduler_function 함수에서 전달하는 알림입니다."}
        F.socketio.emit("notify", data, namespace='/framework', broadcast=True)
         
    
    def plugin_load(self):
        def func():
            data = {'type':'info', 'msg' : "Page1 plugin_load 함수에서 전달하는 알림입니다."}
            F.socketio.emit("notify", data, namespace='/framework', broadcast=True)

        threading.Timer(10,func).start()

    def plugin_unload(self):
        data = {'type':'info', 'msg' : "Page1 plugin_unload 함수에서 전달하는 알림입니다."}
        F.socketio.emit("notify", data, namespace='/framework', broadcast=True)
        #time.sleep(10)
