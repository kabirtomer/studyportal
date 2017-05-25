var $select1 = $( '#select1' ),
		$select2 = $( '#select2' );
    
$select1.on( 'change', function() {
	if( $("#select1 option:selected").text() =='Select a department'){
		$select2.val('');
	}
	else{
	$select2.val($("#select1 option:selected").text());
	}	

/* For the dropdown */
	$('#select2').focus();
    	$('#select2').trigger("click");

	var e = jQuery.Event("keydown");
e.which = 65; // # Some key code value
$("#select2").trigger(e);

} ).trigger( 'change' );


