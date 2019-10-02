<template>
<div>
    <navbar></navbar>
    <div class="hotel-container">
        <div class="subtitle">
            <div>300多間房源</div>
        </div>
        <div class="info-container">
            <div class="hotel-inner-container">
                <div class="img-block">
                    <carousel class="img"></carousel>
                    <!-- <img src="https://a0.muscache.com/im/pictures/55113277/8e202e00_original.jpg?aki_policy=large" alt=""> -->
                </div>
                <div class="hotel-info" >
                    <div class="title-score">
                        <div class="title">喜來登大飯店
                            <a href="/hotel/info">查看詳情</a>
                        </div>
                        
                        <div class="score">4.55 <span class="comment_count">(374)</span></div>
                    </div>
                    <div class="additional-info">
                        <div class="room-type">海景雙人床、豪華雙人床</div>
                        <div class="service">免費停車...........</div>
                    </div>
                </div>
            </div>
             <div class="hotel-inner-container">
                <div class="img-block">
                    <carousel class="img"></carousel>
                    <!-- <img src="https://a0.muscache.com/im/pictures/55113277/8e202e00_original.jpg?aki_policy=large" alt=""> -->
                </div>
                <div class="hotel-info">
                    <div class="title-score">
                        <div class="title">喜來登大飯店</div>
                        <div class="score"><span class="oi oi-star">4.55 (374)</span></div>
                    </div>
                    <div class="additional-info">
                        <div class="room-type">海景雙人床、豪華雙人床</div>
                        <div class="service">免費停車...........</div>
                    </div>
                </div>
            </div>
            <div class="hotel-inner-container">
                <div class="img-block">
                    <carousel class="img"></carousel>
                    <!-- <img src="https://a0.muscache.com/im/pictures/55113277/8e202e00_original.jpg?aki_policy=large" alt=""> -->
                </div>
                <div class="hotel-info">
                    <div class="title-score">
                        <div class="title">喜來登大飯店</div>
                        <div class="score"><span class="oi oi-star">4.55 (374)</span></div>
                    </div>
                    <div class="additional-info">
                        <div class="room-type">海景雙人床、豪華雙人床</div>
                        <div class="service">免費停車...........</div>
                    </div>
                </div>
            </div>
            <div class="hotel-inner-container">
                <div class="img-block">
                    <carousel class="img"></carousel>
                    <!-- <img src="https://a0.muscache.com/im/pictures/55113277/8e202e00_original.jpg?aki_policy=large" alt=""> -->
                </div>
                <div class="hotel-info">
                    <div class="title-score">
                        <div class="title">喜來登大飯店</div>
                        <div class="score"><span class="oi oi-star">4.55 (374)</span></div>
                    </div>
                    <div class="additional-info">
                        <div class="room-type">海景雙人床、豪華雙人床</div>
                        <div class="service">免費停車...........</div>
                    </div>
                </div>
            </div>
              <div class="hotel-inner-container">
                <div class="img-block">
                    <carousel class="img"></carousel>
                    <!-- <img src="https://a0.muscache.com/im/pictures/55113277/8e202e00_original.jpg?aki_policy=large" alt=""> -->
                </div>
                <div class="hotel-info">
                    <div class="title-score">
                        <div class="title">喜來登大飯店</div>
                        <div class="score"><span class="oi oi-star">4.55 (374)</span></div>
                    </div>
                    <div class="additional-info">
                        <div class="room-type">海景雙人床、豪華雙人床</div>
                        <div class="service">免費停車...........</div>
                    </div>
                </div>
            </div>
              <div class="hotel-inner-container">
                <div class="img-block">
                    <carousel class="img"></carousel>
                    <!-- <img src="https://a0.muscache.com/im/pictures/55113277/8e202e00_original.jpg?aki_policy=large" alt=""> -->
                </div>
                <div class="hotel-info">
                    <div class="title-score">
                        <div class="title">喜來登大飯店</div>
                        <div class="score"><span class="oi oi-star">4.55 (374)</span></div>
                    </div>
                    <div class="additional-info">
                        <div class="room-type">海景雙人床、豪華雙人床</div>
                        <div class="service">免費停車...........</div>
                    </div>
                </div>
            </div>
        </div>
        <pagination></pagination>
    </div>
    
</div>
</template>


<script>
import navbar from "../subcomponent/navbar.vue"
import carousel from "../subcomponent/carousel.vue"
import pagination from "../subcomponent/page.vue"
export default {
    components:{
        navbar,
        carousel,
        pagination
    }
}
</script>



<style lang="scss" scoped>
    .box{
        width:960px;
        border: 6px solid #f00;
        display:flex;
        justify-content:flex-end;
        flex-wrap:wrap;
        flex-direction: row;
        align-items:stretch;
        align-content: center;
        
    }
    .hotel-container{
        background-color: #fff;
        font-family:"Microsoft JhengHei";
        display:flex;
        flex-direction: column;
        justify-content:flex-start;
        .subtitle{
            font-size:30px;
            font-weight: bold;
            margin: 1% 5%;
            display:flex;
            justify-content:flex-start;
        }
        .mt-3{
            margin: 1% 5%;
            display:flex;
            justify-content:flex-end;
        }
        
        .info-container{
            display:flex;
            flex-wrap:wrap;
            justify-content:space-around;
            width:90%;
            margin: 0 auto;
            .hotel-inner-container{
                width:520px;
                display:flex;
                flex-wrap:wrap;
                justify-content:space-around;
                flex-grow:1;
                padding:5px;
                .img-block{
                    width:100%;
                    .img{
                        width:100%;
                        height:100%;
                    }
                }
                .hotel-info{
                    flex-grow:1;
                    padding:1%;
                    .title-score{
                        display: flex;
                        justify-content:space-between;
                        .title{
                            font-size: 30px;
                            max-height:24px;
                            font-weight: bold;
                            letter-spacing: 3%;
                        }
                        .comment_count{
                            color:#222222;
                        }
                    }
                    .additional-info{
                        display: flex;
                        flex-direction: column;
                        padding-top:10px;
                        .room-type{
                            flex-grow:1;
                        }
                        .service{
                            flex-grow:2;
                        }
                    }
                    
                }
            }
        }
    }
    
</style>