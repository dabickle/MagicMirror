const path = require('path');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');

module.exports = {
    entry : "./WeatherApp/WeatherForcastApp.js",
    output : {
        filename:'../../../home/static/home/dist/WeatherForcastApp.js',
    },
    mode : "development",
    optimization: {
        minimizer: [new UglifyJsPlugin()],
    },
    module:  {
        rules: [
            {
                exclude : [
                    path.resolve(__dirname, "/Framework/"),
                    path.resolve(__dirname, "/Common/")
                ]
            }
        ]
    }
};