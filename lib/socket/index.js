const sio   = require('socket.io');

var io;

function register(server) {
    io = sio.listen(server.server);
}

function emit(channel, message) {
    io.emit(channel, message);
}

module.exports = {
    register: register,
    emit: emit,
    io: io
};
