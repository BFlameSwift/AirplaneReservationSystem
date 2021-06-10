<template>
  <div class="login_container">
    <img
      :src="imgArr[index]"
      alt=""
      height="100%"
      width="100%"
      referrerPolicy="no-referrer"
    />
    <!-- 标签栏 -->

    <div class="head">
      <img
        src="../assets/logox.png"
        alt=""
        style="position: absolute; left: 364px; top: 13px; width: 250px"
      />
      <hr class="hr" color="#e8e8e8"/>
      <a class="line" style="left: 18%">查询</a>
      <a class="line" @click="manage" style="left: 27%">管理</a>
      <a class="line" @click="help" style="left: 36%">帮助</a>
      <a class="line" @click="book" style="left: 45%">预定</a>
      <div v-if="isLogin===0">
        <div class="to_login" @click="toRegister" style="bottom: 0%; right: 3%">
          <p>注册</p>
        </div>
        <div class="to_login" @click="toLogin" style="bottom: 0%; right: 6%">
          <p>登录</p>
        </div>
      </div>
      <div v-if="isLogin!==0">
        <div class="to_login" @click="toPersonal" style="bottom: 0%; right: 3%">
          <p>您好，{{ username }}</p>
        </div>
      </div>

    </div>

    <!-- 查询栏 -->
    <div class="login_box">
      <div class="title_on" style="top: 10%; left: 3%">
        <p>查询航班</p>
      </div>
      <div class="search" @click="search">
        <img
          src="../assets/搜索.png"
          alt=""
          style="
          position: absolute;
          height: 40px;
          width: 40px;
          left: 50%;
          top: 50%;
          transform: translate(-50%, -50%);
          <!-- border: 0.5px solid #adadad; -->
        "
        />
      </div>
      <!-- 舱位选择 -->
      <div class="dropdown" style="top: 68%;">
        <button class="dropbtn" v-text="seat"></button>
        <div class="dropdown-content">
          <a @click="seat='大于30kg'">大于30kg</a>
          <a @click="seat='小于30kg'">小于30kg</a>
        </div>
      </div>
      <!-- 人数选择 -->
      <div class="dropdown" style="top: 42%;">
        <button class="dropbtn" v-text="passen">下拉菜单</button>
        <div class="dropdown-content">
          <a @click="passen='成人'">成人 18岁以上</a>
          <a @click="passen='未成年人'">未成年人 12-18</a>
          <a @click="passen='儿童'">儿童 2-11</a>
          <a @click="passen='婴儿'">婴儿 0-2</a>
        </div>
      </div>

      <img src="../assets/箭头.png" alt=""
           style="position:absolute;width: 20px;left:180px;top:162px">
      <!-- 日期 -->
      <div class="date">
        <date-picker style="position:absolute;height: 100%;width: 100%;color: transparent;" v-model=date type="date"
                     :min="min" :max="max" :hide-icon="true"/>
        <h3 class="month">{{ match[(new Date(date)).getMonth()] }}</h3>
        <font size="7" color="#ce0000" class="day">{{ (new Date(date)).getDate() }}</font>
      </div>

      <!-- 登陆表单区域 -->
      <div label-width="10px" class="login_form">
        <!-- 标签 -->
        <!-- 出发地 -->

        <input
          v-model="departure"
          style="
            height: 50px;
            width: 360px;
            margin-left: 10px;
            border: 0.5px solid #adadad;
            border-radius: 3px;
            font-size: 15px;
          "
          placeholder="出发地"
          clearable
        />
        <!-- 目的地 -->
        <input
          v-model="destination"
          style="
            height: 50px;
            width: 360px;
            margin-left: 10px;
            margin-top: 22px;
            border: 0.5px solid #adadad;
            border-radius: 3px;
            font-size: 15px;
          "
          placeholder="目的地"
          clearable
        />
      </div>
    </div>
  </div>
</template>

<script>
import DatePicker from '@hyjiacan/vue-datepicker'
import '@hyjiacan/vue-datepicker/dist/datepicker.css'

export default {
  components: {DatePicker},
  data() {
    return {
      date: new Date(),
      min: '2020-6-8',
      max: '2022-12-12',
      destination: '',
      departure: '',
      month: "May",
      day: 19,
      isLogin: 0,
      imgArr: [
        require("../assets/1.jpg"),
        require("../assets/2.jpg"),
        require("../assets/3.jpg"),
        require("../assets/4.jpg"),
        require("../assets/5.jpg"),
        require("../assets/6.jpg"),
        require("../assets/7.jpg"),
      ],
      match: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"],
      index: 1,
      // style: ['','','','','',''],
      value1: '',
      value2: '',
      passen: "乘客类型",
      seat: "行李重量",
      username: ''
    };
  },
  created: function () {
    let d = new Date();
    const Str = window.sessionStorage.getItem('token')
    if (Str) this.isLogin = 1;
    else this.isLogin = 0;
    if (this.isLogin === 1) {
      this.$http.get('/index/').then(result => {
        this.username = result.data.user.name;
      })
    }

  },
  mounted: function () {
    this.fun();
  },
  methods: {
    search() {
      const formData = new FormData();
      formData.append("origination", this.departure)
      formData.append("destination", this.destination)
      const d = new Date(this.date)
      const a = d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate()
      formData.append("date", a)
      console.log(formData)
      console.log(a)
      console.log(this.departure)
      console.log(this.destination)
      this.$http.post('/api/query_flight/', formData)
        .then(result => {
          if (result.data.status === 0) {
            if (this.departure !== '') {
              if (this.destination !== '') {
                console.log(JSON.parse(result.data.flight_list))
                this.$router.push({path: '/displayFlight', query: {mylist: result.data.flight_list}})
              }
            } else {
              console.log(this.destination.length)
              console.log(this.departure.length)
              this.$alert('请填写完整', '查询失败', {
                confirmButtonText: '确定',
              });
            }

          } else {
            // eslint-disable-next-line no-undef
            this.$alert(result.data.msg, '查询失败', {
              confirmButtonText: '确定',
            });
          }
          console.log(result.data)
          this.msg = result.data.msg

        })
    },
    fun: function () {
      //setInterval(函数体,时间)
      setInterval(this.play, 3000)
    },
    play: function () {
      this.index++;
      this.index %= 7;
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
    toPersonal: function () {
      this.$router.push("/personal");
    },
    manage() {
      this.$router.push('/historyFlight')
    },
    help() {
      this.$router.push('/HelloWorld')
    },
    book() {
      this.$router.push('/futureFlight')
    },
    //   todisplayFlight:function(){
    //     console.log("xxx")
    //     this.$router.push(
    //       {
    //         path:'/displayFlight',query:{}
    //       }
    //     )
    //   }
    // },
  }
}
</script>

<style lang="less" scoped>
body {
  height: 100%;
  width: 100%;
}

input {
  border-radius: 5px;
}

img {
  border-radius: 5px;
}

.to_login {
  position: absolute;
  font-size: 15px;
  /* color: black; */
  color: #54545e;
  cursor: pointer;
}

.line {
  position: absolute;
  bottom: 9%;
  font-size: 20px;
  /* color: black; */
  color: #54545e;
  cursor: pointer;
}

.head {
  position: absolute;
  background-color: #ffffff;
  color: black;
  top: 0%;
  height: 16%;
  min-height: 165px;
  width: 100%;
}

.input-with-select .el-input-group__prepend {
  background-color: #fff;
}

.login_container {
  background-color: #fff;
  height: 100%;

}

.search {
  position: absolute;
  height: 47%;
  width: 14%;
  right: 2%;
  top: 40%;
  background-color: #ffc0cb;
  border: 1px solid #eee;
  border-radius: 10px;
}

.login_box {
  width: 900px;
  height: 270px;
  background-color: #fff;
  border-radius: 3px;
  position: absolute;
  left: 50%;
  top: 50%;
  border-radius: 15px;
  box-shadow: 2px 2px 5px #000;
  transform: translate(-50%, -50%);
}

.avator_box {
  height: 130px;
  width: 130px;
  border: 1px solid #eee;
  border-radius: 50%;
  padding: 10px;
  box-shadow: 0 0 10px #ddd;
  position: absolute;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
}

.login_form {
  position: absolute;
  bottom: 40%;
  width: 40%;
  height: 20%;
  padding: 0 10px;
}

.date {
  position: absolute;
  top: 40%;
  left: 47%;
  height: 47%;
  width: 17%;
  border-radius: 5px;
  border: 0.3px solid #adadad;
}

.day {
  position: absolute;
  writing-mode: lr-tb;
  left: 50%;
  bottom: 10%;
  transform: translate(-50%);
  padding: 0px 10px;
}

.month {
  position: absolute;
  writing-mode: lr-tb;
  left: 50%;
  bottom: 50%;
  transform: translate(-50%);
  padding: 0px 10px;
}

.icon-search {
  width: 12px;
  height: 12px;
  border-radius: 100%;
  border: 2px solid currentcolor;
  position: relative;
  margin: 30px auto;
}

.icon-search:after {
  content: "";
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  transform: rotate(45deg);
  width: 8px;
  height: 2px;
  position: absolute;
  top: 13px;
  left: 11px;
  background-color: currentcolor;
}

.title_on {
  position: absolute;
  font-size: 20px;
  font-family: 黑体;
  font-weight: bold;
  background: linear-gradient(#3399ff, #3399ff) no-repeat;
  background-size: 100% 1px;
  background-position: 0 2.5em;
  text-shadow: 0.05em 0 #fff, -0.05em 0 #fff;
  color: #3399ff;
  cursor: pointer;
}

.title_off {
  position: absolute;
  font-size: 20px;
  font-family: 黑体;
  font-weight: bold;
  text-shadow: 0.05em 0 #fff, -0.05em 0 #fff;
  color: black;
  cursor: pointer;
}

.left {
  position: absolute;
  top: 50%;
  left: 4%;
}

.right {
  position: absolute;
  top: 50%;
  right: 4%;
}

.hr {
  position: relative;
  margin-top: 110px;
}

/* 下拉按钮样式 */
.dropbtn {
  background-color: #ffffff;
  color: black;
  font-weight: 200;
  height: 100%;
  width: 100%;
  border: none;
  cursor: pointer;
}

/* 容器 <div> - 需要定位下拉内容 */
.dropdown {
  position: absolute;
  left: 67%;
  width: 15%;
  height: 45px;
  border: 0.3px solid #adadad;
  display: inline-block;
}

/* 下拉内容 (默认隐藏) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
}

/* 下拉菜单的链接 */
.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

/* 鼠标移上去后修改下拉菜单链接颜色 */
.dropdown-content a:hover {
  background-color: #f1f1f1;
}

/* 在鼠标移上去后显示下拉菜单 */
.dropdown:hover .dropdown-content {
  display: block;
}

/* 当下拉内容显示后修改下拉按钮的背景颜色 */
.dropdown:hover .dropbtn {
  background-color: #d2d3d2;
}
</style>
