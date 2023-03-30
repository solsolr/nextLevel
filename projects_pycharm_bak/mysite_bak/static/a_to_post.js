function goPage(page = 1) {

          var f = document.paging;


          f.page.value = page;


          f.action = "{% url 'login:auth' %}"

          f.method = "post"
          f.submit();
        };