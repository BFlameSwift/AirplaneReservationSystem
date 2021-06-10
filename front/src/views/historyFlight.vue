<template>
  <div class="personal_container">
    <!-- 标签栏 -->
    <div class="head">
      <img
        src="../assets/logox.png"
        alt=""
        style="position: absolute; left: 364px; top: 13px; width: 250px"
      />
      <hr class="hr" color="#e8e8e8"/>
      <hr class="hr_bottom" color="#e8e8e8"/>
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
    >您好 {{ username }}，欢迎访问</a>
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
      class="button button--login button--round-s button--text-thick button--beforeinverted button--size"
      style="
        position: absolute;
        left: 1400px; top: 480px;
        width: 400px;
        height: 60px;
      "
    >
      以往的航班
    </button>
    <button
      type="button"
      class="button button--login button--round-s button--text-thick button--inverted button--size"
      style="
        position: absolute;
        left: 1400px; top: 540px;
        width: 400px;
        height: 60px;
      "
      @click="toUpdate"
    >
      更新个人信息
    </button>
    <div style="margin-top:350px;margin-left:300px">
      <div v-for="it in Flights" style="margin-top:20px">
        <each-history-flight :desCity=it.origination :departCity=it.destination :departAirport=it.departure_airport
                             :desAirport=it.landing_airport :departTime=it.starting_time :desTime=it.arrival_time :flight=it.flight_number
                             :time=it.flight_time :price='it.price' :date=it.date :seat=it.flight_type></each-history-flight>
      </div>
    </div>
  </div>
</template>

<script>
import EachHistoryFlight from "../components/EachHistoryFlight.vue"

export default {
  components: {EachHistoryFlight},
  data() {
    return {
      username: '',
      Flights: [
      ]
    };
  },
  created() {
    this.$http.get('/index/').then(result => {
      this.username = result.data.user.name
      this.Flights = JSON.parse(result.data.show_order_before);
      console.log(this.Flights)
    })
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
    toPersonal: function () {
      this.$router.push("/personal");
    },
    toFutureFlight: function () {
      this.$router.push({path: '/futureFlight', query: {}})
    },
    toUpdate: function () {
      this.$router.push({path: '/update', query: {}})
    },
    search() {
      this.$router.push('/main')
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
    exit() {
      this.$router.push('/main')
    }
  },
};
</script>

<style lang="less" scoped>
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
</style>
