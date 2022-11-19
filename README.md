# 테스트


## 테스트

### 테스트

### 테스트



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
