const restify = require('restify');
const server = restify.createServer({
    name: 'batmap',
    version: '0.0.1'
});

server.use(restify.acceptParser(server.acceptable));
server.use(restify.queryParser());
server.use(restify.bodyParser());

// Registering Routes
require('./lib/routes/crimes')(server);
require('./lib/routes/path')(server);

const io = require('./lib/socket');
io.register(server);

server.listen(3001, () => {
    console.log('%s listening at %s', server.name, server.url);
});
