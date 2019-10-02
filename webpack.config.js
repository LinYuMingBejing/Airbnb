
const path = require('path');

const htmlWebpackPlugin = require("html-webpack-plugin")

const VueLoaderPlugin = require('vue-loader/lib/plugin')


module.exports = {
    entry: path.join(__dirname,"./src/main.js"), 
    output:{
        path: path.join(__dirname,"./dist"), 
        filename:"bundle.js" 
    },
    plugins:[ 
        new htmlWebpackPlugin({
            template:path.join(__dirname,"./src/index.html"),  
            filename:"index.html", 
            
        }),
        new VueLoaderPlugin()
    ],
    module:{  //配置所有第三方loader 模塊的
        rules:[
            { test:/\.css$/, use:["style-loader", "css-loader"] }, 
            { test:/\.less$/, use:["style-loader","css-loader","less-loader"]}, 
            { test:/\.(jpg|png|gif|bmp|jpeg)$/, use :"url-loader?limit=7631&name=[name].[ext]"}, 
           
            { test:/\.scss$/, use:["style-loader","css-loader","sass-loader"]},
            { test:/\.(ttf|eot|svg|woff|woff2)$/,use:"url-loader"},
            { test:/\.js$/, use :["babel-loader"], exclude:/node_modules/}, 
            { test: /\.vue$/, use: ['vue-loader']}, 
        ]
    },
    resolve: {
        alias: {
            "vue$" : "vue/dist/vue.js"
        }
    }
}

