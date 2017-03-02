// cookie csrf function
function getCookie(name) {
   var cookieValue = null;
   if (document.cookie && document.cookie !== '') {
       var cookies = document.cookie.split(';');
       for (var i = 0; i < cookies.length; i++) {
           var cookie = jQuery.trim(cookies[i]);
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
   return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$('#submitForm').click(submitForm)

function submitForm(){
    user = $("#userId").val()
    name = $("#firstName").val() +' ' + $("#lastName").val()
    fmd = 1
    farm_condition = $("#conditions").val()
    bgp_requirements = $("#requirements").val()
    corrective_action = $("#correctiveActions").val()
    observed = $("#dateTime").val()
    var postdata = {'user':user, 'name':name, 'fmd':fmd, 'fmd':fmd,
                    'farm_condition':farm_condition, 'bgp_requirements':bgp_requirements,
                    'corrective_action':corrective_action,
                     'observed':observed}
    console.log(postdata)
    $.ajax({url:'/api/fmddata/', data:postdata, type:'POST'}).done(function(){
        location = location
    })
}
