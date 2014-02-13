$(document).ready(function(){
	$('.module').hide({height: 100}, 1000);
	$('#blog').before('<ul class="tabings"></ul>');
	$('.module').each(function(){
		$('.tabings').append('<li class="lists"><h2>' + $(this).attr('id') + '</h2></li>');
	});
	$('.lists').click(function(){
		if($(this).find('h2').html()=='lists active'){
			$(this).removeClass('active')
		}
		else{
			$(this).addClass('active');
			if($(this).find('h2').html()=='blog'){
				$('#blog').show();
				$('#specials').hide();
			}
			
			else if($(this).find('h2').html()=='specials'){
				$('#specials').show();
				$('#blog').hide();
			}
		}
	});
});