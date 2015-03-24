$(function () {
	/********************
	* Quantity
	********************/
	
	$('#id_quantity').on('change', function() {
		
		var originPrice = parseFloat($('#orig_price').text());
		var quantity = parseFloat($('#id_quantity').val());
		
		var total = originPrice*quantity;
		
		var s;
		
		if (quantity > 1) {
			s = total.toFixed(2) + " (" + quantity + " x $" + originPrice + ")";
		} else {
			s = originPrice;
		}
		
		$('#price').text(s);
		
	}); //change
	
	
	/********************
	* Add to cart and  Shopping car modal
	********************/
	
	$('#buy_now_btn').on('click', function () {
		
		var quantity = parseFloat($('#id_quantity').val());
		var itemID = $('#item_id').text();
		
		console.log(itemID);
		
		console.log("Buy button pressed");
		
		setTimeout(1000);
		
//		$.ajax({
//			url: '/catalog/cart.add/' + itemID + '/' + quantity + '/',
//			success: $.loadmodal({
//				url: '/catalog/cart/',
//				title: 'Shopping cart:',
//				width: '80%',
//			}),
//		}); //ajax
        
        
        $.loadmodal({
            url: '/catalog/cart.add/' + itemID + '/' + quantity + '/',
            
        });
		
	});//click
	
	
}); //ready

