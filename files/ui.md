
### 가끔 필요하지만 다시 찾기 힘든 것들


  - **모달창 닫기 방지**  
    {backdrop: 'static', keyboard: false} 을 넣어서 show

    ```javascript
        $("#command_modal").modal({backdrop: 'static', keyboard: false}, 'show');  
    ```
    

  - **formdata 를 dict로 변환**  
    ```python
    def arg_to_dict(self, arg):  
        return self.P.logic.arg_to_dict(arg)
    ```

    - 체크박스 UI
        ```javascript
        $('input[id^="use_checkbox|"]').bootstrapToggle();
        ```

        $("#job_schedule_auto_start").val('on');
        $('#job_schedule_auto_start').bootstrapToggle('on')

{{ macros.setting_global_scheduler_button(arg['is_include'], arg['is_running']) }}


$("#job_schedule_auto_start").val('off');
  $('#job_schedule_auto_start').bootstrapToggle('off')


function set_schedule_mode(mode) {
  $('input:radio[name="job_schedule_mode"][value="'+mode+'"]').attr('checked',true);

  if ( mode == 'none' || mode == 'startup') {
    $("#job_schedule_interval").attr('disabled', true);
    $("#job_schedule_auto_start").attr('disabled', true);
  } else {
    $("#job_schedule_interval").attr('disabled', false);
    $("#job_schedule_auto_start").attr('disabled', false);
  }
}


    - **현재 페이지 새로고침**  
    `location.reload();`


    - radio 버튼 javascript에서 값 변경
    ```
    $('input:radio[name="job_schedule_mode"][value="'+mode+'"]').attr('checked', true);
    $('input:radio[name="mount_finish_mode"][value="all"]').attr('checked',true);
    ```