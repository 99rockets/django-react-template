var path = require("path");
var webpack = require('webpack');

module.exports = {
    context: __dirname,
    entry: {
        App: './assets/js/index',
        vendors: ['react']
    },
    output: {
        path: path.resolve('./assets/bundles/local/'),
        filename: "[name]-[hash].js",
    },
    externals: [
    // add all vendor libs here
    ],
    plugins: [
        new webpack.optimize.CommonsChunkPlugin('vendors', 'vendors.js'),
        // add all common plugins here
    ],
    module: {
        loaders: [
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                loaders: ['babel']
            }
        ]
    },
    resolve: {
        modulesDirectories: ['node_modules', 'bower_components'],
        extensions: ['', '.js', '.jsx']
    }
};
