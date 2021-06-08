<template>
  <template>
    <div style="width:1000px;height:160px;background:white">
        <div class="frame">
            <label style="font-size:15px;font-weight:50">航班号:</label>
            <input v-model="flightid" style="width:30%;margin-left:1%">
            <label style="font-size:15px;font-weight:50;margin-left:9%">出发城市:</label>
            <input v-model="departCity" style="width:10%;margin-left:1%">
            <label style="font-size:15px;font-weight:50;margin-left:5%">到达城市:</label>
            <input v-model="desCity" style="width:10%;margin-left:1%">
            <br>
            <label style="font-size:15px;font-weight:50">出发机场:</label>
            <input v-model="departAirport" style="width:10%;margin-left:1%">
            <label style="font-size:15px;font-weight:50;margin-left:5%">到达机场:</label>
            <input v-model="desAirport" style="width:10%;margin-left:1%">
            <label style="font-size:15px;font-weight:50;margin-left:5%">出发时间:</label>
            <input v-model="departTime" style="width:10%;margin-left:1%">
            <label style="font-size:15px;font-weight:50;margin-left:5%">到达时间:</label>
            <input v-model="desTime" style="width:10%;margin-left:1%">
            <br>
            <label style="font-size:15px;font-weight:50">经济舱价格:</label>
            <input v-model="low" style="width:10%;margin-left:1%">
            <label style="font-size:15px;font-weight:50;margin-left:5%">商务舱价格:</label>
            <input v-model="mid" style="width:10%;margin-left:1%">
            <label style="font-size:15px;font-weight:50;margin-left:5%">头等舱价格:</label>
            <input v-model="high" style="width:10%;margin-left:1%">
            <button style="margin-left:145px;width:60px;margin-top:10px" class="blueb">修改</button>
            <button style="margin-left:15px;width:60px;margin-top:10px" class="redb">删除</button>
        </div>
    </div>
</template>
<script>
export default{
    name:'EachFlight',
    props:{
        flightid:String,
        departAirport:String,
        desAirport:String,
        departTime:String,
        desTime:String,
        departCity:String,
        desCity:String,
        low:String,
        mid:String,
        high:String,
        company:String,
        time:String,
    }
}
</script>
<style scoped>
input{
    border-radius: 0;
    margin-left:0;
    border-top:0;
    border-left:0;
    border-right:0;
    border-bottom: 2px solid #dbdbdb;
    height: 40px;
    outline: none;
    font-size: 17px;
}
.frame{
    width:100%;
    height:100%;
    border:2px solid #e2d7d7;
    box-shadow:0px 0px 8px rgb(197, 192, 182);
    margin-top: 20px;
}
.blueb{
    position: relative;
    width: 100px;
    height: 50px;
    border: none;
    background: #2E5C99;
    color: #fff;
    -webkit-transition: background-color 0.3s, color 0.3s;
    transition: background-color 0.3s, color 0.3s;
    -moz-osx-font-smoothing: grayscale;
    font-weight: 300;
    border-radius: 1px;
    font-size: 16px;
    border-radius: 3px;
}
.blueb:hover{
    background-color: #2671D3;
    color: #fcfcfd;
}
.redb{
    position: relative;
    width: 100px;
    height: 50px;
    border: none;
    background: #ff0808;
    color: #fff;
    -webkit-transition: background-color 0.3s, color 0.3s;
    transition: background-color 0.3s, color 0.3s;
    -moz-osx-font-smoothing: grayscale;
    font-weight: 300;
    border-radius: 1px;
    font-size: 16px;
    border-radius: 3px;
}
.redb:hover{
    background-color: #f16666;
    color: #fcfcfd;
}
</style>
