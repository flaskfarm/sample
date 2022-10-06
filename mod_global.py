from .setup import *
name = 'global' 

class ModuleGlobal(PluginModuleBase):

    def __init__(self, P):
        super(ModuleGlobal, self).__init__(P, name=name, first_menu='button')
        

    def process_menu(self, page, req):
        try:
            return render_template(f'{__package__}_{name}_{page}.html', arg={})
        except Exception as e: 
            P.logger.error(f'Exception:{str(e)}')
            P.logger.error(traceback.format_exc())
            return render_template('sample.html', title=f"{__package__}/{name}/{page}")

    def process_command(self, command, arg1, arg2, arg3, req):
        return jsonify('')
            
