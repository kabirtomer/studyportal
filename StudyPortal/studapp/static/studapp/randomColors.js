$(document).ready(function(){
	 colors = ["rgb(224, 17, 53)","rgb(78, 169, 110)","rgb(131, 8, 239)","rgb(240, 132, 77)",
	     "#FFC107","rgb(196, 154, 253)","rgb(245, 170, 105)",
	     "rgb(34, 140, 252)","rgb(51, 97, 122)","rgb(9, 170, 112)","rgb(20, 173, 161)",
	     "rgb(124, 32, 168)","rgb(49, 108, 162)"," rgb(81, 92, 152)",
	     "rgb(255, 46, 53)","rgb(189, 163, 13)","rgb(79, 216, 73)","rgb(97, 214, 121)","rgb(134, 94, 28)",
	     "rgb(179, 134, 147)","rgb(96, 11, 56)","rgb(191, 18, 1)","rgb(105, 97, 78)",
	     "rgb(18, 70, 100)","rgb(240, 56, 122)","rgb(63, 184, 156)","rgb(78, 42, 225)",
	     "rgb(210, 132, 98)"];

	 var dontTake = 0;
	$(".deal").each(function(index){
		 // var colorR = Math.floor((Math.random() * 256));
	  //    var colorG = Math.floor((Math.random() * 256));
	  //    var colorB = Math.floor((Math.random() * 256));
   //    $(this).css("background", "rgb(" + colorR + "," + colorG + "," + colorB + ")");

   		 var select = Math.floor((Math.random() * colors.length));
   		 while (select == dontTake){
   		 	select = Math.floor((Math.random() * colors.length));
   		 }    
	     $(this).css("background",colors[select]);
	});
})