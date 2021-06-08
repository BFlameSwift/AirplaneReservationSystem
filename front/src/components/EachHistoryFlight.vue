<template>
    <div style="width:1000px;height:160px;background:white">
        <div class="frame">
            <div style="width:80%;float:left;height:100%">
                <div style="float:left;width:40%;height:30%;margin-right:0">
                    <p style="width:100%;height:100%;font-size:20px;margin-left:20px">{{departCity}} ({{departAirport}}) {{departTime}}</p>
                </div>
                <div style="float:left;width:10%;height:30%">
                    <hr style="border:0;background-color:#021B41;height:1px;margin-top:30px;width:80%;margin-right:80px"/>
                </div>
                <div style="float:left;width:45%;height:30%">
                    <p style="width:100%;height:100%;font-size:20px;margin-left:20px">{{desCity}} ({{desAirport}}) {{desTime}}</p>
                </div>
                <div style="margin-top:60px;height:20%;margin-left:10px;">
                    <div style="float:left;width:50%">
                        <p style="font-size:18px;text-indent:10px;">航班号: {{flight}}</p>
                    </div>
                    <div style="float:left;width:50%">
                        <p v-if="seat==='3'" style="margin-left:20px;font-size:18px;">商务舱</p>
                        <p v-else-if="seat==='1'" style="margin-left:20px;font-size:18px;">头等舱</p>
                        <p v-else-if="seat==='2'" style="margin-left:20px;font-size:18px;">高端经济舱</p>
                        <p v-else style="margin-left:20px;font-size:18px;">经济舱</p>
                    </div>
                </div>
                <div style="margin-top:20px">
                    <p style="font-size:18px;margin-left:20px">{{date}}</p>
                </div>
            </div>
            <div style="width:20%;float:left;height:100%">
                <p style="font-size:30px;margin-left:50px;margin-top:80px">￥{{price}}</p>
            </div>
        </div>
</div>
</template>
<script>
export default{
    name:'EachFutureFlight',
    props:{
        departCity:String,
        desCity:String,
        departAirport:String,
        desAirport:String,
        departTime:String,
        desTime:String,
        price:String,
        date:String,
        flight:String,
        time:String,
        seat:String,
    },
    methods:{
        refund:function(){

        }
    }
}
</script>
<style scoped>
.ppp{
    width:80px;
    height:50px;
    margin-left:50px;
    margin-right:5%;
    margin-top:0;
    color:white;
    background-color: #2E5C99;
    line-height: 50px;
    font-size: 15px;
    font-weight: 100;
    font-family: Arial, Helvetica, sans-serif;
}
.frame{
    width:100%;
    height:100%;
    border:2px solid #e2d7d7;
    box-shadow:0px 0px 8px rgb(197, 192, 182);
}
button:hover{
    background-color: #2671D3;
    color: #fcfcfd;
}
</style>
