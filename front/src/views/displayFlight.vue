<template>
  <div style="width: 2000px; height: 1000px">
    <div>
      <div class="head">
        <img
          src="../assets/logox.png"
          alt=""
          style="position: absolute; left: 364px; top: 13px; width: 250px"
        />
        <hr class="hr" color="#e8e8e8"/>
        <hr class="hr_bottom" color="#e8e8e8"/>
        <a class="line" @click="toMain" style="left: 18%">查询</a>
        <a class="line" @click="manage" style="left: 27%">管理</a>
        <a class="line" @click="help" style="left: 36%">帮助</a>
        <a class="line" @click="book" style="left: 45%">预定</a>
        <div v-if="isLogin===0">
          <div class="to_login" @click="toRegister" style="bottom: 6%; right: 3%">
            <p>注册</p>
          </div>
          <div class="to_login" @click="toLogin" style="bottom: 6%; right: 6%">
            <p>登录</p>
          </div>
        </div>
        <div v-if="isLogin!==0">
          <div class="to_login" @click="toPersonal" style="bottom: 4%; right: 3%">
            <p>您好，{{ username }}</p>
          </div>
        </div>
      </div>
    </div>
    <!-- <div style="height: 120px; border: 0; margin: 0; width: 58%; float: left">
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
        返回到航班查询
      </p>
      <hr
        style="border: 0; background-color: #021b41; height: 2px; margin: 0"
      />
    </div> -->
    <div style="margin-top: 220px">
      <p
        style="font-size: 30px; text-indent: 300px; font-weight: 100; margin: 0"
      >
        {{ departCity }}到{{ desCity }}
      </p>
      <p style="font-size: 20px; text-indent: 300px; font-weight: 100">
        {{ date }}
      </p>
    </div>
    <div style="margin-top: 0; background: #fff; height: 100%">
      <div style="height: 60px"></div>
      <div
        v-for="it in mylist"
        :key="index"
        style="margin-top: 20px; margin-left: 300px"
      >
        <each-flight
          :desCity="it.origination"
          :departCity="it.destination"
          :departAirport="it.departure_airport"
          :desAirport="it.landing_airport"
          :departTime="it.starting_time"
          :desTime="it.arrival_time"
          :company="it.flight_number"
          :time="it.flight_time"
          :low="it.business_class_price"
          :mid="it.economy_class_price"
          :high="it.first_class_price"
          :date="it.date"
        ></each-flight>
      </div>
    </div>
  </div>
</template>
<script>
import BlueBotton from "../components/BlueBotton.vue";
import EachFlight from "../components/EachFlight.vue";

export default {
  name: "displayFlight",
  components: {
    BlueBotton,
    EachFlight,
  },

  data() {
    return {
      username: '',
      departCity: "北京",
      desCity: "上海",
      date: "2021-5-22",
      mylist: [],
    }
  },
  created: function () {
    console.log(this.$route.query.mylist)
    this.mylist = JSON.parse(this.$route.query.mylist);
    console.log(this.$route.query.mylist)
    console.log(this.mylist)
    const Str = window.sessionStorage.getItem('token')
    if (Str) this.isLogin = 1;
    else this.isLogin = 0;
    if (this.isLogin === 1) {
      this.$http.get('/index/').then(result => {
        this.username = result.data.user.name;
      })
    }
    console.log(this.mylist)
    console.log(this.mylist[0])
  },
  methods: {
    toMain: function () {
      this.$router.push("/");
    },
    toLogin: function () {
      this.$router.push("/login");
    },
    toRegister: function () {
      this.$router.push("/register");
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
    toPersonal: function () {
      this.$router.push("/personal");
    },
  },
};
</script>
<style scoped>

.head {
  position: absolute;
  background-color: #ffffff;
  color: black;
  top: 0%;
  height: 16%;
  min-height: 165px;
  width: 100%;
}

.to_login {
  position: absolute;
  font-size: 15px;
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

.line {
  position: absolute;
  bottom: 16%;
  font-size: 20px;
  /* color: black; */
  color: #54545e;
  cursor: pointer;
}

.hr_bottom {
  position: relative;
  margin-top: 50px;
}
</style>
