
### DB Migration

로딩시 `PluginModuleBase` `PluginPageBase` class의 `migration` 함수 호출됨.  
필요한 경우 오버라이딩하여 사용하며 버전을 알 수 있는 `db_version` 정도의 값을 `ModelSetting` 에 유지하는게 필요하다.

참고로 [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) 패키지가 자동 migration을 지원하나 FF에 적용하기 어려워 사용하지 않는다.
```python
def migration(self):
    try:
        with F.app.app_context():
            import sqlite3
            db_file = F.app.config['SQLALCHEMY_BINDS'][P.package_name].replace('sqlite:///', '').split('?')[0]
            if P.ModelSetting.get(f'{self.name}_db_version') == '1':
                connection = sqlite3.connect(db_file)
                cursor = connection.cursor()
                query = f'ALTER TABLE {P.package_name}_file ADD uuid VARCHAR'
                cursor.execute(query)
                connection.close()
                P.ModelSetting.set(f'{self.name}_db_version', '2')
                db.session.flush()
                
            if P.ModelSetting.get(f'{self.name}_db_version') == '2':
                connection = sqlite3.connect(db_file)
                cursor = connection.cursor()
                query = f'ALTER TABLE {P.package_name}_job ADD process_command VARCHAR'
                cursor.execute(query)
                connection.close()
                P.ModelSetting.set(f'{self.name}_db_version', '3')
                db.session.flush()      
    except Exception as e: 
        P.logger.error(f'Exception:{str(e)}')
        P.logger.error(traceback.format_exc())
```
