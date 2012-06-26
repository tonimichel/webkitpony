function send(url, data, callback) {
    $(document).unbind('webkit_response')
    $(document).bind('webkit_response', function(e, response) {
        callback(response)
    })
    document.title = "null";
    document.title = JSON.stringify({
        '__url__': url,
        '__data__': data
    });
} 
