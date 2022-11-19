### 설정 관련

- **function getFormdata(form_id)**   

    form id 값에 해당하는 element를 serialize 한다.  
    disabled true인 경우 값에 포함되지 않음.  
    python 에서는 arg_to_dict 함수로 dict로 변환하여 사용. 
    
    * html 코드  

        ```html
        <form id='job_setting'>
            {{ macros.setting_select('job_command', 'Command', [['move', 'Move'],['copy', 'Copy'],['sync', 'Sync']], col='6', desc=None)}}
            {{ macros.setting_input_text('job_name', 'Name', desc=['목록 검색에서 사용할 이름. 없을시 ID']) }}
        </form>
        ```
    
    * python에 전달  

        ```javascript
        $("body").on('click', '#job_save_btn', function(e) {
            var formData = getFormdata('#job_setting');
            globalSendCommandPage("job_save", formData);
        });
        ```

- **function showModal(data='EMPTY', title='JSON', json=true)**   
  **모달창 띄우기**





