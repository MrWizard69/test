$.validator.setDefaults({
	submitHandler: function() {$( "#progressbar" ).show().progressbar({ value: 100}); alert("Submitted!!! :D"); }
});

$().ready(function() {
	// validate the comment form when it is submitted
	$("#commentForm").validate();

	// validate signup form on keyup and submit
	$("#signupForm").validate({
		rules: {
			firstname: "required",
			lastname: "required",
			username: {
				required: true,
				minlength: 2
			}
			
		}
		
	});
});

$( "#progressbar" ).hide();

function create( template, vars, opts ){
	return $container.notify("create", template, vars, opts);
}

$(function(){
	// initialize widget on a container, passing in all the defaults.
	// the defaults will apply to any notification created within this
	// container, but can be overwritten on notification-by-notification
	// basis.
	$container = $("#container").notify();

	create("default", { title:'A Form', text:'Type stuff and be merry!'});
	});

