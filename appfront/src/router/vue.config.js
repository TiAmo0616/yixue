// vue.config.js
module.exports = {
    devServer: {
      https: {
        key: require('fs').readFileSync('./src/server.key'),
        cert: require('fs').readFileSync('./src/server.crt'),
      },
      open:true,
    },
  };