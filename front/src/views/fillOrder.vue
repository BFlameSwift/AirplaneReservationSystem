<template>
<div style="width:2000px;height:1000px">
    <div>
        <p id='t1'>立即预订，随时变更</p>
        <div style="height:120px;border:0;margin:0;width:40%;float:left">
            <p id='t2'>FLIGHT BOOKING</p>
             <hr style="border:0;background-color:#021B41;height:2px;margin:0"/>
        </div>
        <div style="height:120px;border:0;margin:0;width:2%;float:left">
            <div style="height:60px;">
                <img src="../assets/箭头_左.png" style="width:20px;height20px:;margin-top:50px" @click="todisplayFlight"/>
            </div>
            <hr style="border:0;background-color:#021B41;height:2px;margin-top:60px"/>
        </div>
        <div style="height:120px;border:0;margin:0;width:58%;float:left">
            <p style="height:120px;margin:0;font-size:20px;line-height:120px;color:#021B41;display:inline">返回到航班</p>
             <hr style="border:0;background-color:#021B41;height:2px;margin:0"/>
        </div>
    </div>
    <div style=" height: 100%;width: 60%;margin:0;padding:0;border:0;float:left;">
        <p id='t3'>告诉我们谁在旅行</p>
        <p id='t4' class="point">Required fields</p>
        <p id='t5'>{{surname}} {{givenname}} - 主要乘客</p>
        <i class="point" style="margin-left:250px;margin-right:10px"/>
        <el-select class='elselect1' placeholder="请选择称谓" v-model="title">
            <el-option v-for="it,index in titles" :key="index" :value="it">
            </el-option>
        </el-select>
        <i class="point" style="margin-left:10px;margin-right:0px"/>
        <input class='inputsurname' v-model="surname" placeholder="证件上的姓氏"/>
        <br>
        <i class="point" style="margin-left:250px;margin-right:10px"/>
        <input class="inputgivenname" v-model="givenname" placeholder="证件上的名字"/>
        <div>
            <i class="point" style="margin-left:250px;margin-right:10px"/>
            <el-radio v-model="gender" label="male" style="margin-left:0;margin-top:10px;margin-bottom:10px" size="medium">男</el-radio>
            <el-radio v-model="gender" label="female">女</el-radio>
        </div>
        <div>
            <i class="point" style="margin-left:250px;margin-right:10px"/>
            <el-date-picker type="date" placeholder="选择出生日期" style="margin-left:0px;margin-top:30px;margin-bottom:30px" v-model="birthday"></el-date-picker>
        </div>
        <div>
            <i class="point" style="margin-left:250px;margin-right:10px"/>
            <el-select class="select2" placeholder="国家/地区代码" v-model="areacode">
                <el-option v-for="it,index in areacodes" :key="index" :value="it"></el-option>
            </el-select>
            <i class="point" style="margin-left:10px;margin-right:0px"/>
            <input class="inputPhone" v-model="phonenumber" placeholder="电话号码"/>
            <br>
            <i class="point" style="margin-left:250px;margin-right:10px"/>
            <input v-model="id" placeholder="证件号码" style="margin-left:0px;width:54%"/>
        </div>
        <div>
            <i class="point" style="margin-left:250px;margin-right:10px"/>
            <input v-model="email" placeholder="电子邮件" style="margin-left:0px;width:54%;margin-top:20px;margin-bottom:30px"/>
        </div>
        <div>
            <BlueBotton msg="继续" style="margin-left:250px;margin-top:20px" @click.native="toafterBuy"/>
        </div>
    </div>
    <div style=" height: 100%;width: 40%;margin:0;padding:0;border:0;float: left;">
        <div class="curved_box" style="margin-top:30px;margin-left:0px;margin-right:20px;width:400px;height:700px">
            <p style="font-size:25px;margin-left:20px;font-weight:200;margin-bottom:0">{{departcity}} ({{departairport}}) 至</p>
            <br>
            <p style="font-size:25px;margin-left:20px;font-weight:200;margin-top:0px">{{descity}} ({{desairport}})</p>
            <div>
                <div style="width:48%;float:left;margin-left:0px">
                     <p style="font-size:20px;margin-left:20px;margin-right:0;font-weight:10;margin-top:0px;display:inline">{{departtime}} {{departairport}}</p>
                </div>
                <div style="width:4%;float:left">
                    <hr style="border:0;background-color:#021B41;height:1px;margin-top:10px;width:70%;margin-left:8px;margin-right:0">
                </div>
                <div style="width:48%;float:left">
                    <p style="font-size:20px;margin-left:10px;font-weight:10;margin-top:0px;display:inline">{{destime}} {{desairport}}</p>
                </div>
            </div>
            <br>
            <p style="font-size:15px;margin-left:20px;font-weight:400;margin-top:50px;margin-bottom:50px">{{seatType}}托运行李</p>
            <p style="font-size:18px;margin-left:20px;font-weight:350;margin-top:50px;display:inline">承运方: </p>
            <p style="font-size:18px;margin-left:20px;font-weight:10;margin-top:50px;display:inline;">{{company}}</p>
            <p style="font-size:20px;margin-left:40px;font-weight:10;margin-top:80px;">总计</p>
            <p style="font-size:40px;margin-left:150px;font-weight:300;margin-top:80px;display:inline"> CNY {{price}}</p>
        </div>
    </div>
</div>
</template>
<script>
import BlueBotton from '../components/BlueBotton.vue'
export default{
    name:'fillOrder',
    components:{
        BlueBotton
    },
    data(){
        return{
            surname:'',
            givenname:'',
            phonenumber:'',
            email:'',
            birthday:'',
            gender:'',
            id:'',
            descity:'北京',
            departcity:'重庆',
            desairport:'大兴国际机场',
            departairport:'江北国际机场',
            departtime:'18:00',
            destime:'21:00',
            price:'1000.00',
            company:'南方航空',
            seatType:'经济舱',
            title:'',
            areacode:'',
            titles:[
                'Mr',
                'Mrs',
                'Miss',
                'Mstr',
                'Capt',
                'Prof',
                'Dr',
                'Dame',
                'Lady',
                'Lord',
                'The Rt Hon',
                'Rabbi',
                'Rev',
                'Sir',
                'Baroness',
                'Viscount',
                'Viscountness'
            ],
            areacodes:[
                '+1',
                '+86',
                '+213',
                '+93',
            ]
        }
    },
    created:function(){
        this.departcity=this.$route.query.departCity;
        this.descity=this.$route.query.desCity;
        this.departairport=this.$route.query.departAirport;
        this.desairport=this.$route.query.desAirport;
        this.departtime=this.$route.query.departTime;
        this.destime=this.$route.query.desTime;
        this.price=this.$route.query.price;
        this.seatType=this.$route.query.seat;
        this.company=this.$route.query.company;
    },
    methods:{
        todisplayFlight:function(){
            this.$router.push("/displayFlight");
        },
        checkAllFilled:function(){
            console.log("xxx");
             if(this.title==''){
                alert("请选择称谓");
                return false;
            }
            if(this.surname==''){
                alert("请输入姓氏");
                return false;
            }
            if(this.givenname==''){
                alert("请输入名字");
                return false;
            }
            if(this.gender==''){
                alert("请选择性别");
                return false;
            }
            if(this.birthday==''){
                alert("请输入出生日期");
                return false;
            }
            if(this.areacode==''){
                alert("请选择国家/地区代码");
                return false;
            }
            if(this.phonenumber==''){
                alert("请输入电话号码");
                return false;
            }
            if(this.id==''){
                alert("请输入证件号码");
                return false;
            }
            if(this.email==''){
                alert("请输入电子邮件");
                return false;
            }
            return true;
        },
        toafterBuy:function(){
          let tag=this.checkAllFilled();
          if(tag==true)
          {
              this.$router.push(
              {path:"/afterBuy",query:{}}
          )
          }  
        }
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
#t1{
    height: 40px;
    margin: 0px;
    color: white;
    background: #021B41;
    text-align: center;
    font-size: 15px;
    line-height: 40px;
}
#t2{
    height: 120px;
    margin: 0;
    background: white;
    color:#2E5C99;
    line-height: 120px;
    font-size: 35px;
    font-family:serif;
    padding-left: 60px;
    font-weight: 700;

}
.hr {
  position: relative;
  margin-top: 110px;
}
.line {
  position: absolute;
  top: 70%;
  font-size: 20px;
  /* color: black; */
  color: #54545e;
  cursor: pointer;
}
.hr_bottom {
  position: relative;
  margin-top: 50px;
}
#t3{
    height:80px;
    margin-top: 20px;
    margin-bottom: 0;
    background: white;
    color:#1A3B66;
    line-height: 80px;
    font-size: 35px;
    font-weight: 100;
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    padding-left: 250px;
}
#t4{
    height: 60px;
    line-height: 60px;
    margin-top:0px;
    margin-bottom: 0px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-size: 15px;
    padding-left: 250px;
    color: #2671D3;
}
.point::before{
    content: '';
    width: 10px;
    height: 10px;
    background-color:#2671D3;
    border-radius: 50%; 
    display: inline-block;
    margin-right: 10px;
}
#t5{
    height: 60px;
    line-height: 60px;
    padding-left: 250px;
    margin-top:0;
    margin-bottom: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-size: 25px;
    font-weight: 100;
    background: white;
    color:#1A3B66;
}
.elselect1{
    margin-left: 0;
    width: 20%;
    margin-top:30px;
    margin-bottom: 50px;
}
.inputsurname{
    width: 30%;
}
.inputgivenname{
    margin-left:0px;
    margin-bottom: 40px;
    width: 53.5%;
}
.inputPhone{
    margin-left:0;
    width: 35.5%;
}
.select2{
    width: 15%;
    margin-top:20px;
    margin-bottom: 50px;
}
.curved_box{
    border:1px solid #dbdbdb;
    box-shadow:0px 0px 10px rgb(197, 192, 182);
}
</style>