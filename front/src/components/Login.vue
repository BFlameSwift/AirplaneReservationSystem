<template>
  <div class="container">
    <div class="line"></div>
    <!-- 登录 -->
    <div>
      <a class="title" style="top: 26%; left: 388px">您的帐户</a>

      <!-- 忘记密码 -->
      <p href="/register/" class="forget">忘记密码？</p>

      <!-- 关闭 -->
      <img src="../assets/关闭.png" alt=""
      @click="to_main"

      style="cursor: pointer;position:absolute;right:30px;top:50px;width:30px;height:30px"/>

      <!-- 登录按钮 -->
      <button
        type="button"
        class="button button--login button--round-s button--text-thick button--inverted button--size"
        style="position:absolute;left: 372px; top: 55%;width: 300px; height: 60px"
        @click="login"
      >登录
      </button>

      <!-- 加入按钮 -->
      <button
        type="button"
        class="button button--join button--round-s button--text-thick button--inverted button--size"
        style="position:absolute;left: 60%; top: 55%; width: 300px; height: 60px"
        @click="to_register"
      >
        注册
      </button>

      <!-- 介绍 -->
      <h3 class="introduce">注册后即可预定航班，并且可以积累积分并赚取奖励。</h3>

      <!-- 注册 -->
      <a class="title" style="top: 26%; right: 35%">注册</a>

      <!-- 登陆表单 -->
      <form class="form" action="/login/" method="post">
        <!-- 账号框 -->
        <div class="row js-input">
          <div class="input">
            <input type="text" v-model="username" id="username"/>
            <label>帐号</label>
          </div>
        </div>

        <!-- 密码框 -->
        <div class="row js-input">
          <div class="input">
            <input type="text" v-model="pwd" id="pwd"/>
            <label>密码</label>
          </div>
        </div>
      </form>
    </div>
  </div>
  <!-- /container -->
</template>

<script>
export default {
  data() {
    return {
      username:'',
      pwd:'',
      msg:''
    };
  },
  methods:{
    to_main: function () {
      this.$router.push("/main");
    },
    to_register: function () {
      this.$router.push("/register");
    },
    login(){
      const formData = new FormData();
      formData.append("username",this.username)
      formData.append("password",this.pwd)
      this.$http.post('/login/',formData)
      .then(result=>{
        if(result.data.status === 0){
          this.$message.success('登录成功')
          console.log(result.data.msg)
          this.$router.push('/personal')
        }
        console.log(result.data)
        this.msg = result.data.msg
        console.log(result)
        window.sessionStorage.setItem('token',result.data.token);

      })
      .catch(err=>{
        console.log((err))
      })
    }
  }
};
</script>

<style lang="less" scoped>
.introduce{
  position: absolute;
  width:380px;
  left: 1200px;
  top: 340px;
  font-size: 30px;
  font-weight: 100;
}
.container{
  position: absolute;
  width: 2000px;
  height: 1000px;
}
.title {
  position: absolute;
  font-size: 50px;
}
.line {
  position: absolute;
  left: 50%;
  top: 20%;
  height: 55%;
  border-right: 2px solid rgb(235, 226, 226);
}
.form {
  margin: 50px;
  position: absolute;
  left: 17%;
  top: 30%;
}
.row {
  margin-top: 50px;
  height: 26px;
  line-height: 26px;
  border-bottom: 2px solid #e8e8e8;
  width: 500px;
}
.input {
  position: relative;
  width: 500px;
  height: 50px;
}
.input input {
  position: absolute;
  bottom: 34px;
  left: 45px;
  display: block;
  width: 100%;
  height: 26px;
  border: none;
  background: none;
  outline: none;
  font-size: 20px;
}
.input label {
  position: absolute;
  bottom: -20px;
  left: 0;
  height: 80px;
  line-height: 26px;
  color: #999;
  font-size: 20px;
}
.forget {
  position: absolute;
  left: 20%;
  top: 62%;
  color: #0d78ad;
  cursor: pointer;
}

//按钮
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
.button--round-s {
  border-radius: 2px;
}
/* Wapasha */
.button.button--login {
  background: #176c97;
  color: #fff;
  -webkit-transition: background-color 0.3s, color 0.3s;
  transition: background-color 0.3s, color 0.3s;
}
.button.button--join {
  background: #fff;
  color: #196c97;
  -webkit-transition: background-color 0.3s, color 0.3s;
  transition: background-color 0.3s, color 0.3s;
}
.button--login.button--inverted {
  background: #2d44a8;
  color: #fdfeff;
}
.button--login::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  border-radius: inherit;
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
// 加入按钮
.button--join.button--inverted {
  background: #fdfeff;
  border:1px solid #0d78ad;
  color: #2d44a8;
}
.button--join::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  border-radius: inherit;
  opacity: 0;
  -webkit-transform: scale3d(0.6, 0.6, 1);
  transform: scale3d(0.6, 0.6, 1);
  -webkit-transition: -webkit-transform 0.3s, opacity 0.3s;
  transition: transform 0.3s, opacity 0.3s;
  -webkit-transition-timing-function: cubic-bezier(0.75, 0, 0.125, 1);
  transition-timing-function: cubic-bezier(0.75, 0, 0.125, 1);
}
.button--join:hover {
  background-color: #fff;
  color: #3f51b5;
}
.button--join.button--inverted:hover {
  background-color: #0d78ad;
  color: #fcfcfd;
}
</style>
