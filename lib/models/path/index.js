'use strict';

function Path(sequelize, DataTypes) {
    let Path = sequelize.define('Path', {
        path: 'geometry(LINESTRING, 4326)',
    }, {
        tableName: 'Path',
        force: true
    });

    return Path;
}

module.exports = Path;
