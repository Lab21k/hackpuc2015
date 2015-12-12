'use strict';

const _ = require('lodash')._,
    db = {},
    fs = require('fs'),
    path = require('path'),
    Sequelize = require('sequelize'),
    env = process.env.NODE_ENV || 'development',
    config = require(__dirname + '/../config/config.json')[env],
    sequelize = new Sequelize(
        config.database,
        config.username,
        config.password,
        _.extend(config, {
            logging: function(log) {

                if (config.logging) {
                    console.log(log);
                }
            }
        })
    );


fs
    .readdirSync(__dirname)
    .filter((file) => {
        return (file.indexOf('.') !== 0) && (file !== 'index.js');
    })
    .forEach((file) => {
        var model = sequelize['import'](path.join(__dirname, file));
        db[model.name] = model;
    });

Object.keys(db).forEach((modelName) => {
    if ('associate' in db[modelName]) {
        db[modelName].associate(db);
    }
});

db.sequelize = sequelize;
db.Sequelize = Sequelize;

module.exports = db;
