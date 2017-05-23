

/*
$("#select1").change(function() {
  if ($(this).data('options') === undefined) {
    Taking an array of all options-2 and kind of embedding it on the select1
    $(this).data('options', $('#select2 option').clone());
  }
  var id = $(this).val();
  var options = $(this).data('options').filter('[value=' + id + ']');
  $('#select2').html(options);
});*/

var $select1 = $( '#select1' ),
		$select2 = $( '#select2' ),
    $options = $select2.find( 'option' );
    
$select1.on( 'change', function() {
	$select2.html( $options.filter( '[value="' + this.value + '"]' ) );
} ).trigger( 'change' );
