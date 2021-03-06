const path=require('path')

module.exports = {
    entry : "./WeatherApp/WeatherApp.js",
    output : {
        filename:'../../../home/static/home/dist/WeatherApp.js',
    },
    mode : "development",
    
    module:  {
        rules: [
            {
                exclude : [
                    path.resolve(__dirname, "Framework/*"),
                    path.resolve(__dirname, "Common/*"),
                ]
            }
        ]
    }
};