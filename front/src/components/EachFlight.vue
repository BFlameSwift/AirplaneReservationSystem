<template>
<div style="width:1000px;height:160px;background:white">
        <div class="frame">
            <div style="width:22%;float:left;height:100%">
                <div style="float:left;width:45%;height:50%">
                    <p style="width:100%;height:100%;font-size:15px;">{{departTime}} {{departAirport}}</p>
                </div>
                <div style="float:left;width:10%;height:50%">
                    <hr style="border:0;background-color:#021B41;height:1px;margin-top:25px;width:70%;margin-left:0"/>
                </div>
                <div style="float:left;width:45%;height:50%">
                    <p style="width:100%;height:100%;font-size:15px;">{{desTime}} {{desAirport}}</p>
                </div>
                <div style="width:100%;height:50%">
                    <p style="width:100%;height:100%;font-size:17px;text-indent:10px">航班号:{{company}}</p>
                    <p style="width:100%;height:100%;font-size:17px;text-indent:10px;">时长:{{time.slice(0,2)}}时{{time.slice(3,5)}}分</p>
                </div>
            </div>
            <div style="width:3%;float:left;height:100%">
            </div>
            <div style="width:25%;float:left;height:100%">
                <button class="ppp" @click="tofillOrder(1)">经济舱￥{{low}}</button>
            </div>
            <div style="width:25%;float:left;height:100%">
                <button class="ppp" @click="tofillOrder(2)">商务舱￥{{mid}}</button>
            </div>
            <div style="width:25%;float:left;height:100%">
                <button class="ppp" @click="tofillOrder(3)">头等舱￥{{high}}</button>
            </div>
        </div>
</div>
</template>
<script>

export default{
    name:'EachFlight',
    props:{
        departCity:String,
        desCity:String,
        departAirport:String,
        desAirport:String,
        departTime:String,
        desTime:String,
        low:String,
        lowp:String,
        mid:String,
        high:String,
        company:String,
        time:String,
        date:String
    },
    methods:{
        tofillOrder:function(type){
            let price;
            let seatType;
            if(type==1)
            {
                price=this.low;
                seatType="经济舱";
            }
            else if(type==2)
            {
            price=this.mid;
            seatType="商务舱";
            }
            else if(type==3)
            {
            price=this.high;
            seatType="头等舱";
            }
            this.$router.push(
                {path:'/fillOrder',query:{date:this.date,time:this.time,departCity:this.departCity,desCity:this.desCity,departAirport:this.departAirport,desAirport:this.desAirport,departTime:this.departTime,desTime:this.desTime,seat:seatType,price:price,company:this.company}}
            )
        }
    }
}
</script>
<style scoped>
.ppp{
    width:85%;
    height:80px;
    margin-left:5%;
    margin-right:5%;
    margin-top:40px;
    color:white;
    background-color: #2E5C99;
    line-height: 80px;
    text-indent: 25px;
    font-size: 20px;
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
