$(document).ready(function() {
  $(document.body).on('click', '.add', function() {
    $('div :input').each(function(){
      if(!$(this).val() && $(this).attr('required')) {
        $(this).addClass('warning');
      }
    });
    checkErrorMess(function(flag) {
      if (flag) {
        var idcity = $('select[name="city"]').val();
        if (idcity == '0') {
          $('label[for="fname"]').before('<h3 id="errormess" class="text-center error-mes">Выберите город</>');
        }
        else {
          $.ajax({
            type: 'POST',
            url: '/addcomment/',
            dataType: 'json',
            data: {
              'firstname': $('#fname').val(),
              'lastname': $('#lname').val(),
              'secondname': $('#sname').val(),
              'region': $('select[name="region"]').val(),
              'city': $('select[name="city"]').val(),
              'phone': $('#phone').val(),
              'email': $('#email').val(),
              'comment': $('#comment').val()
            },
            success: function(res) {
              $('div :input').each(function(){
                $(this).val("");
              });
              $('select[name="region"] option[value="0"]').prop('selected', true);
              $('select[name="city"] option[value="0"]').prop('selected', true);
              $('label[for="fname"]').before('<h3 id="success" class="text-center success">Данные сохранены</>');
            }
          });
        }
      }
    });
  });

  $(document.body).on('click', '.clickable-row', function() {
      window.document.location = $(this).data("href");
  });

  $(document.body).on('click', '.denger', function() {
    var id = $(this).attr('id');
    var row = $(this).closest('tr');
    $.ajax({
      type: 'POST',
      url: '/delcomment/',
      dataType: 'json',
      data: { 'id': id},
      success: function(res) {
        row.remove();
      }
    });
  });

  $(document.body).on('change', 'input', function() {
    var success = $('#success');
    if (success) {
      success.remove();
    }
    if($(this).val() && $(this).attr('required')) {
      $(this).removeClass('warning');
    }
    if(!$(this).val() && $(this).attr('required')) {
      $(this).addClass('warning');
    }
    checkErrorMess(function(flag) {
    });
  });

  $(document.body).on('change', 'select[name="region"]', function() {
    var success = $('#success');
    if (success) {
      success.remove();
    }
    var id = $(this).val();
    $.ajax({
      type: 'POST',
      url: '/selectregion/',
      dataType: 'json',
      data: { 'id': id},
      success: function(res) {
        $('select[name="city"]').replaceWith(res['template']);
      }
    });
  });

  $(document.body).on('change', 'select[name="city"]', function() {
    var success = $('#success');
    if (success) {
      success.remove();
    }
    var id = $(this).val();
    $.ajax({
      type: 'POST',
      url: '/selectorcity/',
      dataType: 'json',
      data: { 'id': id},
      success: function(selectid) {
        $('select[name="region"] option[value="' + selectid + '"]').prop('selected', true);
      }
    });
  });

  function checkErrorMess(call) {
    var errormess = $('#errormess');
    var input = $('input[class="warning"]');
    if (input.length && !errormess.length) {
      $('label[for="fname"]').before('<h3 id="errormess" class="text-center error-mes">Заполните обязательные поля</>');
      call(false);
    }
    else if (!input.length && errormess.length) {
      errormess.remove();
      call(true);
    }
    else {
      call(true);
    }
  }

  // standart functions, use for usage ajax
  // CSRF code
  function getCookie(name) {
      var cookieValue = null;
      var i = 0;
      if (document.cookie && document.cookie !== '') {
          var cookies = document.cookie.split(';');
          for (i; i < cookies.length; i++) {
              var cookie = jQuery.trim(cookies[i]);
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }

  var csrftoken = getCookie('csrftoken');

  function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  $.ajaxSetup({
      crossDomain: false, // obviates need for sameOrigin test
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type)) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });
});
