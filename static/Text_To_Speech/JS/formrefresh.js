$(document).on('submit','#speech_form',function(e){

	e.preventDefault();

	$.ajax({

		type:'POST',
		url:'/Speech-app/Speech/',
		data:{

			name:$('#message').val(),
			csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),

		},

		success:function(){
		
			alert("Speech Completed")
		}

	});



});