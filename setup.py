__menu = {
    'uri': __package__,
    'name': '샘플 플러그인',
    'list': [
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
            'uri': 'manual',
            'name': '매뉴얼',
            'list': [
                {
                    'uri': 'README.md',
                    'name': 'README'
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
    'home_module': 'ui',
    'menu': __menu,
    'setting_menu': None,
    'default_route': 'normal',
}

from plugin import *
P = create_plugin_instance(setting)

from .mod_ui import ModuleUI
from .mod_global import ModuleGlobal
from .mod_pages import ModulePages
P.set_module_list([ModuleUI, ModuleGlobal, ModulePages])

