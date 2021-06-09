<template>
  <div class="personal_container">
    <!-- 标签栏 -->
    <div class="head">
      <img
        src="../assets/logox.png"
        alt=""
        style="position: absolute; left: 364px; top: 13px; width: 250px"
      />
      <hr class="hr" color="#e8e8e8" />
      <hr class="hr_bottom" color="#e8e8e8" />
      <a class="line" @click="search" style="left: 18%">查询</a>
      <a class="line" @click="manage" style="left: 27%">管理</a>
      <a class="line" @click="help" style="left: 36%">帮助</a>
      <a class="line" @click="book" style="left: 45%">预定</a>
      <div class="to_login" @click="exit" style="bottom: 0%; right: 6%">
        <p>退出</p>
      </div>
    </div>

    <!-- 个人中心 -->
    <a
      style="
        position: absolute;
        font-size: 50px;
        top: 20%;
        left: 370px;
        color: rgb(0, 70, 132);
      "
      >更新用户信息</a>
       <!-- menu菜单 -->
    <button
      type="button"
      class="button button--login button--round-s button--text-thick button--inverted button--size"
      style="
        position: absolute;
        left: 1400px; top: 360px;
        width: 400px;
        height: 60px;
      "
       @click="toPersonal"
    >
      我的帐户
    </button>
    <button
      type="button"
      class="button button--login button--round-s button--text-thick button--inverted button--size"
      style="
        position: absolute;
        left: 1400px; top: 420px;
        width: 400px;
        height: 60px;
      "
      @click="toFutureFlight"
    >
      未出发的航班
    </button>
    <button
      type="button"
      class="button button--login button--round-s button--text-thick button--inverted button--size"
      style="
        position: absolute;
        left: 1400px; top: 480px;
        width: 400px;
        height: 60px;
      "
      @click="toHistoryFlight"
    >
      以往的航班
    </button>
    <button
      type="button"
      class="button button--login button--round-s button--text-thick button--beforeinverted button--size"
      style="
        position: absolute;
        left: 1400px; top: 540px;
        width: 400px;
        height: 60px;
      "
    >
      更新个人信息
    </button>
    <div>
        <div style="margin-top:350px;margin-left:350px">
               <p class="tit">用户名</p>
              <input v-model="username" style="width:30%;">
              <p class="tit" style="margin-top:50px">手机号</p>
              <input v-model="phoneNumber" style="width:30%;">
              <p class="tit" style="margin-top:50px">性别</p>
              <el-radio v-model="sex" label="male" style="margin-top:10px;margin-bottom:10px" size="medium">男</el-radio>
            <el-radio v-model="sex" label="female">女</el-radio>
            <p class="tit" style="margin-top:50px">出生日期</p>
               <el-date-picker type="date" v-model="birthday" value-format="yyyy-MM-dd" placeholder="选择出生日期" style="margin-top:30px;margin-bottom:30px"></el-date-picker>
         </div>
         <button class="btn" style="margin-left:350px;margin-top:50px" @click="update">确认修改</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      birthday:"",
      sex:"",
      cancer:"学生",
      phoneNumber:""
    };
  },
  created(){
    this.$http.get('/index/').then(result => {
      this.username=result.data.user.name;
      this.birthday=result.data.user.birthday;
      this.sex=result.data.user.sex==='male'?'男':'女';
      this.phoneNumber=result.data.user.phone_number;
    })

    },
  methods: {
    update:function(){
      const formData = new FormData();
      formData.append("username", this.username)
      formData.append("sex", this.sex)
      console.log(this.birthday)
      console.log(this.sex)
      // const a = this.birthday.getFullYear() + '-' + (this.birthday.getMonth() + 1) + '-' + this.birthday.getDate()
      formData.append("birthday", this.birthday)

      formData.append("perfession", this.cancer)
      formData.append("phone_number", this.phoneNumber)
      this.$http.post('api/index/change/', formData)
        .then(result => {
          if (result.data.status === 0) {
            // eslint-disable-next-line no-undef
            this.$message({
              message: '成功！',
              type: 'success'
            });
            // this.$router.push({path:'/personal',query:{list:result.data.concrete_flights_before}})
          } else {
            // eslint-disable-next-line no-undef
            this.$alert(result.data.msg, '更新失败', {
              confirmButtonText: '确定',
            });
          }
        })
    },
    prev: function () {
      this.index--;
      console.log(this.index);
    },
    next: function () {
      this.index++;
      console.log(this.index);
    },
    // mouseover(index){
    //   this.style[index]="color:green;"
    // },
    // mouseleave(index){
    //   this.style[index]=""
    // },

    toLogin: function () {
      this.$router.push("/login");
    },
    toRegister: function () {
      this.$router.push("/register");
    },
    toPersonal:function(){
      this.$router.push("/personal");
    },
     toFutureFlight:function(){
      this.$router.push({path:'/futureFlight',query:{}})
    },
    toHistoryFlight:function(){
      this.$router.push("/historyFlight");
    },
    search(){
      this.$router.push('/main')
    },
    manage(){
      this.$router.push('/personal')
    },
    help(){
      this.$router.push('/personal')
    },
    book(){
      this.$router.push('/personal')
    },
    exit(){
      this.$router.push('/main')
    }
  },
};
</script>

<style lang="less" scoped>
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
.tit {
  font-size: 20px;
  font-weight: bold;
  color: #80808f;
}
.personal_container {
  background-color: white;
  position: absolute;
  width: 2000px;
  height: 1000px;
}
.personaldata {
  font-size: 15px;
}
.table_basic {
  position: absolute;
  left: 370px;
  top: 390px;
}
.table_info {
  position: absolute;
  left: 370px;
  top: 820px;
}
.table_margin {
  position: absolute;
  left: 370px;
  top: 1320px;
}
.tit {
  font-size: 20px;
  font-weight: bold;
  color: #80808f;
}
.line {
  position: absolute;
  bottom: 7%;
  font-size: 20px;
  /* color: black; */
  color: #54545e;
  cursor: pointer;
}
.hr {
  position: relative;
  margin-top: 110px;
}
.hr_bottom {
  position: relative;
  margin-top: 50px;
}
.head {
  position: absolute;
  background-color: #ffffff;
  color: black;
  top: 0%;
  height: 16%;
  width: 100%;
}
.to_login {
  position: absolute;
  font-size: 15px;
  /* color: black; */
  color: #54545e;
  cursor: pointer;
}
.button {
  float: left;
  min-width: 150px;
  max-width: 500px;
  display: block;
  margin: 1em;
  padding: 1em 2em;
  border: none;
  background: none;
  color: inherit;
  position: relative;
  z-index: 1;
  -moz-osx-font-smoothing: grayscale;
}
.button:focus {
  outline: none;
}
.button > span {
  vertical-align: middle;
}
/* Sizes */
.button--size {
  font-size: 18px;
}
/* Typography and Roundedness */
.button--text-thick {
  font-weight: 300;
}
/* Wapasha */
.button.button--login {
  background: #176c97;
  color: #fff;
  -webkit-transition: background-color 0.3s, color 0.3s;
  transition: background-color 0.3s, color 0.3s;
}
.button--login.button--inverted {
  border: transparent;
  background: #dcdde6;
  color: #37699b;
}
.button--login.button--beforeinverted {
  border: transparent;
  background: #ebebee;
  color: #37699b;
}
.button--login::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  opacity: 0;
  -webkit-transform: scale3d(0.6, 0.6, 1);
  transform: scale3d(0.6, 0.6, 1);
  -webkit-transition: -webkit-transform 0.3s, opacity 0.3s;
  transition: transform 0.3s, opacity 0.3s;
  -webkit-transition-timing-function: cubic-bezier(0.75, 0, 0.125, 1);
  transition-timing-function: cubic-bezier(0.75, 0, 0.125, 1);
}
.button--login:hover {
  background-color: #fff;
  color: #3f51b5;
}
.button--login.button--inverted:hover {
  background-color: #0d78ad;
  color: #fcfcfd;
}
.button--login.button--beforeinverted:hover {
  border: transparent;
  background: #ebebee;
  color: #37699b;
}
.btn{
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
}
.btn:hover{
   background-color: #2671D3;
    color: #fcfcfd;
}
</style>
