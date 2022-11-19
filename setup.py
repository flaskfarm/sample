__menu = {
    'uri': __package__,
    'name': '샘플 플러그인',
    'list': [
        {
            'uri': 'manual',
            'name': '매뉴얼',
            'list': [
                {
                    'uri': 'README.md',
                    'name': 'README'
                },
                {
                    'uri': 'files/ff_plugin.md',
                    'name': 'FF 플러그인'
                },
                {
                    'uri': 'files/ui_etc.md',
                    'name': 'UI 관련'
                },
                {
                    'uri': 'files/ui.md',
                    'name': 'UI'
                },
                {
                    'uri': 'files/global_function.md',
                    'name': 'JavaScript - Global Function'
                }
            ]
        },
        

        {
            'uri': 'ui',
            'name': 'UI',
            'list': [
                {
                    'uri': 'input_text',
                    'name': '설정 - 텍스트',
                }
            ]
        },
        {
            'uri': 'global',
            'name': 'UI - Global',
            'list': [
                {
                    'uri': 'button',
                    'name': 'global_____Btn',
                },
                {
                    'uri': 'manual/manual/ui.md',
                    'name': '매뉴얼'
                }
            ]
        },
        {
            'uri': 'pages',
            'name': 'PluginPageBase 사용',
            'list': [
                {
                    'uri': 'page1',
                    'name': '테스트 페이지1',
                },
                {
                    'uri': 'page2',
                    'name': '테스트 페이지2',
                }

            ]
        },
        
        {
            'uri': 'log',
            'name': '로그',
        },
    ]
}


setting = {
    'filepath' : __file__,
    'use_db': True,
    'use_default_setting': True,
    'home_module': None,
    'menu': __menu,
    'setting_menu': None,
    'default_route': 'normal',
}

from plugin import *

P = create_plugin_instance(setting)

from .mod_global import ModuleGlobal
from .mod_pages import ModulePages
from .mod_ui import ModuleUI

P.set_module_list([ModuleUI, ModuleGlobal, ModulePages])

