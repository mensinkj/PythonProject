$(function () {

	$('#search_text').on('change', function() {
		
		$.ajax({
			url: '/catalog/index.search/' + $('#search_text').val() + '/',
			success: function(data) {
			
				$('#products').html(data);
				
			}, //success
			
		}); //ajax
		
	}); //change
	
	
}); //ready