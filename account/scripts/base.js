$(function () {
	$('#show_login_dialog').on('click', function() {
		$.loadmodal('/account/login.loginform/');
	});
}); //ready

$(function () {
	$('#loginform').ajaxForm(function(data) {
		$('#jquery-loadmodal-js-body').html(data);
	});

}); //ready