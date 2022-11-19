from .setup import *

name = 'global' 

class ModuleGlobal(PluginModuleBase):

    def __init__(self, P):
        super(ModuleGlobal, self).__init__(P, name=name, first_menu='button')
        

    def process_menu(self, page, req):
        try:
            arg = {}
            arg['globalOpenBtn_md'] = '''
* **javascript 코드**  
  ```javascript
    $("body").on('click', '#globalOpenBtn', function(e) {
        e.preventDefault();
        url = $(this).data('url')
        window.open(url, "_blank");
    });
  ```

* **사용 : macro** 
  ```javascript
  macros.info_text_and_buttons('version', '버전', [
    ['globalOpenBtn', '업데이트 내역', [('url','https://sjva.me/wiki/public/changelog')]], 
    ['recent_version_btn', '최신버전 확인']
  ])
  ```

* **사용 : javascript**
  ```javascript
  tmp += j_button('globalOpenBtn', 'GIT', {'url':current_data[i].info.local_info.home});
  ```
'''
            return render_template(f'{__package__}_{name}_{page}.html', arg=arg)
        except Exception as e: 
            P.logger.error(f'Exception:{str(e)}')
            P.logger.error(traceback.format_exc())
            return render_template('sample.html', title=f"{__package__}/{name}/{page}")

    def process_command(self, command, arg1, arg2, arg3, req):
        return jsonify('')
            
