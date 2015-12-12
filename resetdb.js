const db = require('./lib/models'),
      config = require('./lib/config/config.json').development;

db.sequelize.sync()
    .then((err) => {
        if (err) {
            console.log(err);
        } else {
            done(true);
        }
    });

