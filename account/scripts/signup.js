$(function () {
	/****************************************
	 * Check if username is available
	 ***************************************/
	$('#id_username').on('change', function() {
		
		var username = $('#id_username').val();
		
		$.ajax({
			url: '/homepage/index.check_username/',
			
			data: {
				user: username
			},
			
			type: "POST",
			
			success: function(resp) {
				if (resp == "0") {
					$('#id_username_message').text('This username is available!');
					$('#id_username_message').css('color', 'green');
				} else {
					$('#id_username_message').text('This username is already taken. Please choose a different one!');
					$('#id_username_message').css('color', 'red');
				}//if
				
			}, //success
			
		}); //ajax
	
	}); //change
	
}); //ready

/****************************************
 * Check if passwords match
 ***************************************/

$(function () {
	$('#id_passwordConfirm').on('change',function() {
		var password = $('#id_password').val();
		var passwordConfirm = $('#id_passwordConfirm').val();
		console.log(password);
		console.log(passwordConfirm);
		if (password != passwordConfirm) {
			$('#id_password_message').text("Passwords don't match!");
			$('#id_password_message').css('color', 'red');
		}
		
	}); // change

});

/****************************************
 * AJAX form
 ***************************************/
$(function () {
	$('#createUserForm').ajaxForm(function (data) {
		($('#createUserForm_container')).html(data)
	}) //ajaxForm
}); 