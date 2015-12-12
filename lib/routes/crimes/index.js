module.exports = function(server) {
    'use strict';

    const   sequelize   = require('sequelize'),
            db          = require('../../models');

    server.post('/crimes', (req, res, next) => {

        console.log(req.body);

        let position = 'SRID=4326;POINT(' + req.body.longitude;
            position += ' ' + req.body.latitude;
            position += ')';

        console.log(position);

        db.Crime.create({
            name: req.body.name,
            description: req.body.description,
            position: position,
            data: req.body.data
        })
        .then((data) => {
            console.log('Foi');
            res.send(data);
            return next();
        }, (err) => {
            console.log('erro');
            res.send(err);
            return next();
        });

    });
};
