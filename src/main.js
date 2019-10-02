// 入口文件

import Vue from "vue"


import VueRouter from "vue-router"

Vue.use(VueRouter)
import "bootstrap/dist/css/bootstrap.css"
// 導入Bootstra
import BootstrapVue from 'bootstrap-vue'
Vue.use(BootstrapVue)

// 註冊Vuex
import Vuex from "vuex"



Vue.use(Vuex)
var store = new Vuex.Store({
    state:{ 
    },
    mutations:{ 
    },
    getters:{ 
    }
})



// 2.1 導入axios
// 2.2 安裝 axios
import axios from 'axios'
Vue.prototype.$ajax = axios


// 按需導入Mint-UI中的組件
import MintUI from 'mint-ui'
Vue.use(MintUI)
import 'mint-ui/lib/style.css'



// 導入App根組件
import "./lib/mui/css/mui.min.css"
import "./lib/mui/css/icons-extra.css"





import router from "./router.js"


import app from "./App.vue"


// 全局設置post時候表單數據格式組織形式
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';





var vue = new Vue({
    el:"#app",
    render: c=>c(app),
    router,  
})