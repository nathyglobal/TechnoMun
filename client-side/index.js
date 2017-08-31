//Verification Submit
$( "#verification_submit" ).click(function() {
  $.ajax({
	type: "POST",
	dataType: "json",
	data: {
		req_type: "verify_facs2",
		digits: $('#verif').val()
	},
	url: "https://www.sudo-code.com.au/cgi-bin/TechnoMUN/serve.cgi",
	success: function(data) {
		console.log(data);
	},
  }).fail(function(dunnoWhatThisArgumentDoes, textStatus) {
	   console.log(textStatus);
  });
});


$( "#del" ).click(function() {
  $.ajax({
	type: "POST",
	dataType: "json",
	data: {
		req_type: "",
		
	},
	url: "https://www.sudo-code.com.au/cgi-bin/TechnoMUN/serve.cgi",
	success: function(data) {
		console.log(data);
	},
  }).fail(function(dunnoWhatThisArgumentDoes, textStatus) {
	   console.log(textStatus);
  });
});


$(function(){

    $('body').hover(function(){
        $(this).data('hover',1); //store in that element that the mouse is over it
    },
    function(){
        //alert("keep mouse on screen")
        $(this).data('hover',0); //store in that element that the mouse is no longer over it
    });


    window.isHovering = function (selector) {
        return $(selector).data('hover')?true:false; //check element for hover property
    }
});