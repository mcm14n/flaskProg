// JQuery functions

function requestServerDataJQuery(URL, method, data, callbacks)
{
	$.ajax({
		url: URL,
		type: method,
		data: JSON.stringify(data),
		dataType: json,
	})
	.done(callbacks['done']['function'](callbacks['done']['arguments']))
	.fail(callbacks['fail']['function'](callbacks['fail']['arguments']))
	.complete(callbacks['complete']['function'](callbacks['complete']['arguments']))
}