$(document).ready(function() {
	$('.promos').hide();
	$('.promos').fadeIn(1000);
	
	/*$('.sidebar').css('width','0%');
	$('.sidebar').animate({width:'29%'},1000);*/

	$('.sidebar').hide();
	$('.sidebar').slideDown(1000);

	$('.navbar').hide();
	$('.navbar').slideDown(1000);
	$('.nav').hide();
	$('.nav').slideDown(1000);

	
	/*$('.navbar').css('right','100%');	
	$('.navbar').css('left','');	
	$('.navbar').animate({right:'',left:'29%'},1000);*/
});
