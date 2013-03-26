var http = require('http');
var fs = require('fs');

function heading() {
    return '<h1>Github tags</h1>';
}

/**
  * Creates a html link from the tag. Opens a new tab
  */
function create_link(url) {
    return '<a target="_blank" href="' + url + '">' + url + '</a>';
}

/**
  * Just output a nice table format for the tags and url
  */
function create_html_table(data) {
    var output_data = '<table><tr><th>Tag</th><th>Url</th></tr>';
    var tag_data = JSON.parse(data)
    for (var tag in tag_data) {
        output_data += '<tr><td>';
        output_data += tag;
        output_data += '</td><td>';
        output_data += create_link(tag_data[tag]);
        output_data += '</td></tr>'
    }
    output_data += '</table>'
    return output_data;
}

/**
  * The main loopback mechanism. Starts a http server and listens on port 8000.
  */
var server = http.createServer(function(req, res) {
    res.writeHead(200);
    fs.readFile('tags.json', function (err, data) {
        if (err) throw err;
        var output_data = heading();
        output_data += create_html_table(data);
        res.end(output_data);
    });
});
server.listen(8000)
