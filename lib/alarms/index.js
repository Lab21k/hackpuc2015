'use strict';

module.exports = {
    verifyAlarms: verifyAlarms
};

const db    = require('../models'),
      sio    = require('../socket');

function verifyAlarms(crime) {
    let query = `
        WITH buffered_area AS (
            SELECT ST_Buffer(CAST(path AS geography), 200)::geometry as geom, * FROM "Path"
        )
        SELECT * FROM buffered_area
        WHERE ST_Disjoint(
                (SELECT position FROM "Crime" WHERE id = ${crime.id}),
                geom
            ) IS false;
    `;

    db.sequelize.query(query).spread(function(results, metadata) {
        if (results.length > 0) {
            sio.emit('alarm:incident_on_route', {
                crime: crime.toJSON()
            });
        }
    });
}
