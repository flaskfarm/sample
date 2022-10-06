from .setup import *
name = 'ui'

class ModuleUI(PluginModuleBase):

    def __init__(self, P):
        super(ModuleUI, self).__init__(P, name=name, first_menu='input_text')
        

    def process_menu(self, page, req):
        try:
            return render_template(f'{__package__}_{name}_{page}.html', arg={})
        except Exception as e: 
            P.logger.error(f'Exception:{str(e)}')
            P.logger.error(traceback.format_exc())
            return render_template('sample.html', title=f"{__package__}/{name}/{page}")

    def process_command(self, command, arg1, arg2, arg3, req):
        return jsonify('')
            
