$(document).ready(function(){
	var textsaver = $('label').text();
	$('.input_text').attr('value', $('label').text());
	$('.input_text').addClass('hint');
	$('label').remove();
	$('.input_text').focusin(function(){
		$(this).val('');
	});
	$('.input_text').focusout(function(){
		if($(this).val()==""){;
			$(this).val(textsaver);
		}
	});
});