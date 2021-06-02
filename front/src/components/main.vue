<template>
  <div class="login_container">
    <img
      :src="imgArr[index]"
      alt=""
      height="100%"
      width="100%"
      referrerPolicy="no-referrer"
    />
    <img
      :src="imgArr[index]"
      alt=""
      height="100%"
      width="100%"
      referrerPolicy="no-referrer"
    />
    <!-- 左箭头 -->
    <a href="javascript:void(0)" v-show="index != 0" @click="prev" class="left">
      <img src="../assets/prev.png" alt="" />
    </a>
    <!-- 右箭头 -->
    <a
      href="javascript:void(0)"
      v-show="index < imgArr.length - 1"
      @click="next"
      class="right"
    >
      <img src="../assets/next.png" alt="" />
    </a>
    <!-- 标签栏 -->

    <div class="head">
      <img
        src="../assets/logox.png"
        alt=""
        style="position: absolute; left: 364px; top: 13px; width: 250px"
      />
      <hr class="hr" color="#e8e8e8" />
      <a class="line" style="left: 18%">查询</a>
      <a class="line" @click="manage" style="left: 27%">管理</a>
      <a class="line" @click="help" style="left: 36%">帮助</a>
      <a class="line" @click="book" style="left: 45%">预定</a>
      <!-- 登录 -->

      <div class="to_login" @click="toRegister" style="bottom: 0%; right: 3%">
        <p>注册</p>
      </div>
      <div class="to_login" @click="toLogin" style="bottom: 0%; right: 6%">
        <p>登录</p>
      </div>
    </div>

    <!-- 查询栏 -->
    <div class="login_box">
      <div class="title_on" style="top: 10%; left: 3%">
        <p>航班</p>
      </div>
      <div class="title_off" style="top: 10%; left: 10%">
        <p>航班+酒店</p>
      </div>
      <div class="search">
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
          <a @click="seat='头等舱'">头等舱</a>
          <a @click="seat='经济舱'">经济舱</a>
          <a @click="seat='商务舱'">商务舱</a>
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
        <h3 class="month">{{ month }}</h3>
        <font size="7" color="#ce0000" class="day">{{ date }}</font>
      </div>

      <!-- 登陆表单区域 -->
      <div label-width="10px" class="login_form" >
        <!-- 标签 -->
        <!-- 出发地 -->

        <input
          v-model="location"
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
export default {
  data() {
    return {
      destination: "",
      location: "",
      month: "May",
      date: 19,
      imgArr: [
        require("../assets/1.jpg"),
        require("../assets/2.jpg"),
        require("../assets/3.jpg"),
        require("../assets/4.jpg"),
        require("../assets/5.jpg"),
        require("../assets/6.jpg"),
        require("../assets/7.jpg"),
      ],
      index: 1,
      // style: ['','','','','',''],
      value1: "",
      value2: "",
      passen:"乘客类型",
      seat:"座位类型"
    };
  },
  methods: {
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
    manage(){
      this.$router.push('/personal')
    },
    help(){
      this.$router.push('/personal')
    },
    book(){
      this.$router.push('/personal')
    }
  },
};
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
  bottom: 7%;
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
  width: 100%;
}
.input-with-select .el-input-group__prepend {
  background-color: #fff;
}

.login_container {
  background-color: #2b4b6b;
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
  left: 45%;
  height: 47%;
  width: 20%;
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
