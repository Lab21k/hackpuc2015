module.exports = function(server) {
    'use strict';

    const   sequelize   = require('sequelize'),
            db          = require('../../models');

    server.post('/path', (req, res, next) => {

        let position = req.body.path.map((p) => {
            return p.join(' ');
        }).join(', ');

        let path = 'SRID=4326;LINESTRING(';
            path += position;
            path += ')';

            console.log(path);

        db.Path.create({
            path: path
        })
        .then((data) => {
            res.send(data);
            return next();
        }, (err) => {
            res.send(err);
            return next();
        });

    });
};
