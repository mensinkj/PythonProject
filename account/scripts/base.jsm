$(function() {
	// update the time every n seconds
	window.setInterval(function() {
		$('.browser-time').text(new Date());
	}, 1000);

	// update button
    $('#server-time-button').click(function() {
      $('.server-time').load('/account/index.gettime');
    });
});

//set active page by id
function getCurrentPath() 
{ 
	$(${ currentPage }).addClass('active');
}