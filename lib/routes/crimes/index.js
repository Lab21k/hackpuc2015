module.exports = function(server) {
    'use strict';

    const   sequelize   = require('sequelize'),
            db          = require('../../models');

    server.post('/crimes', (req, res, next) => {

        let position = 'SRID=4326;POINT(' + req.body.longitude;
            position += ' ' + req.body.latitude;
            position += ')';

        db.Crime.create({
            name: req.body.name,
            description: req.body.description,
            neighbourhood: req.body.neighbourhood,
            position: position,
            date: req.body.date,
            data: req.body.data
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
