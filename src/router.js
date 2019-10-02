import VueRouter from "vue-router"

// 導入路由對應的路由組件
import CityContainer from "./components/main/CityContainer.vue" 
import HotelInfo from "./components/main/HotelInfo.vue"


//3. 創建路由對象
var router = new VueRouter({
    routes:[ //配置路由規則
        // {path:"/" , redirect:"/hotel"},
        {path: "/hotel" ,component:CityContainer},
        {path: "/hotel/info" ,component:HotelInfo},
        ],

    linkActiveClass:"mui-active" //覆蓋默認的路由高亮的類，默認的類叫做router-link-active
})

export default router // 把路由對象暴露出去