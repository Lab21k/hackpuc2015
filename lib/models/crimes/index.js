'use strict';

function Crime(sequelize, DataTypes) {
    let Crime = sequelize.define('Crime', {
        name: DataTypes.STRING,
        description: DataTypes.TEXT,
        neighbourhood: DataTypes.STRING,
        position: 'geometry(POINT, 4326)',
        data: DataTypes.JSON,
        date: DataTypes.DATE
    }, {
        tableName: 'Crime',
        force: true
    });

    return Crime;
}

module.exports = Crime;
