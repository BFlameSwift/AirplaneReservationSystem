<template>
  <div style="width: 2000px; height: 1000px">
     <button
        type="button"
        class="button button--join button--round-s button--text-thick button--inverted button--size"
        style="position:absolute;left: 60%; top: 55%; width: 300px; height: 60px"
        @click="to_pay"
      >
        确认购买
      </button>
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
      <!-- 登录 -->
    </div>
    <div style="height: 120px; border: 0; margin: 0; width: 58%; float: left">
      <p
        style="
          height: 120px;
          margin: 0;
          font-size: 20px;
          line-height: 120px;
          color: #021b41;
          display: inline;
        "
      >
        返回到个人界面
      </p>
      <hr
        style="border: 0; background-color: #021b41; height: 2px; margin: 0"
      />
    </div>
    <div style="width: 1000px; margin: 0">
      <p
        style="
          height: 200px;
          line-height: 200px;
          margin-left: 250px;
          font-size: 30px;
          font-weight: 50;
        "
      >
        查看您的航班
      </p>
      <hr
        style="
          border: 1px solid #d6dad9;
          width: 1000px;
          margin-left: 250px;
          margin-top: 60px;
        "
      />
      <p
        style="
          margin-top: 80px;
          margin-left: 250px;
          font-size: 25px;
          font-weight: 50;
        "
      >
        {{ departCity }} ({{ departAirport }}) 到 {{ desCity }} ({{
          desAirport
        }})
      </p>
      <p style="margin-left: 250px; font-size: 15px; font-weight: 50">
        全程{{ time }}
      </p>
      <div style="height: 60px; width: 100%; margin-left: 250px">
        <div style="height: 100%; width: 20%; float: left">
          <p style="font-size: 20px; font-weight: 50">
            {{ departTime }} {{ departAirport }}
          </p>
          <p style="font-size: 15px; font-weight: 50">{{ departDate }}</p>
        </div>
        <!--中间横线-->
        <div style="height: 100%; width: 12%; float: left">
          <hr
            style="
              border: 0;
              background-color: #021b41;
              height: 1px;
              margin-top: 35px;
              width: 70%;
              margin-left: 0;
            "
          />
        </div>
        <div style="height: 100%; width: 20%; float: left">
          <p style="font-size: 20px; font-weight: 50">
            {{ desTime }} {{ desAirport }}
          </p>
          <p style="font-size: 15px; font-weight: 50">{{ desDate }}</p>
        </div>
      </div>
      <div>
        <p
          style="
            margin-left: 250px;
            margin-top: 80px;
            font-size: 20px;
            font-weight: 50;
          "
        >
          航班号: {{ company }}
        </p>
      </div>
      <hr
        style="
          border: 1px solid #d6dad9;
          width: 1000px;
          margin-left: 250px;
          margin-top: 50px;
        "
      />
      <p
        style="
          text-align: right;
          margin-left: 250px;
          width: 1000px;
          font-size: 18px;
        "
      >
        总计:
      </p>
      <p
        style="
          text-align: right;
          margin-left: 250px;
          width: 1000px;
          font-size: 40px;
          font-weight: 100;
          margin-top: 0;
        "
      >
        ￥{{ price }}
      </p>
    </div>
  </div>
</template>
<script>
import BlueBotton from "../components/BlueBotton.vue";

export default {
  name: "afterBuy",
  components: {
    BlueBotton,
  },
  data() {
    return {
      departCity: "重庆",
      desCity: "北京",
      departAirport: "江北国际机场",
      desAirport: "大兴国际机场",
      time: "3h",
      departTime: "18:00",
      desTime: "21:00",
      departDate: "2021-5-22",
      desDate: "2021-5-22",
      price: "1000.00",
      company: "南方航空",
    };
  },
  created: function () {
    this.departCity = this.$route.query.departCity;
    this.desCity = this.$route.query.desCity;
    this.departAirport = this.$route.query.departAirport;
    this.desAirport = this.$route.query.desAirport;
    this.departTime = this.$route.query.departTime;
    this.desTime = this.$route.query.desTime;
    this.price = this.$route.query.price;
    this.time = this.$route.query.time;
    this.company = this.$route.query.flight_number;
    console.log(this.departAirport)
    console.log(this.departAirport)
  },
  methods: {
    toMycenter: function () {
      this.$router.push({path: "/personal", query: {}});
    },
    search() {
      this.$router.push('/main')
    },
    manage() {
      this.$router.push('/personal')
    },
    help() {
      this.$router.push('/personal')
    },
    book() {
      this.$router.push('/personal')
    },
    to_pay(){
      const formDatapay = new FormData();
      formDatapay.append("money", this.price)
      this.$http.post('api/pay/', formDatapay)
    }
  },
};
</script>
<style scoped>
#t1 {
  height: 40px;
  margin: 0px;
  color: white;
  background: #021b41;
  text-align: center;
  font-size: 15px;
  line-height: 40px;
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

.button--join.button--inverted {
  background: #fdfeff;
  border: 1px solid #0d78ad;
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
