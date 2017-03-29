$(function () {
   var $switches = $('#switches');
   $.ajax ({
	type: 'GET',
	url: 'http://172.27.171.130:5000/status',
	success: function(switches) {
	   $.each(switches, function(i, item) {
		$switches.append('<li>Name: ' + item.name +', Status: '+ item.status + '</li>');
           });
        }
   });
});
