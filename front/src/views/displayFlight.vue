<template>
  <div style="width: 2000px; height: 1000px">
    <div>
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
        <!-- 登录 -->
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
    <div style="margin-top: 140px">
      <p
        style="font-size: 30px; text-indent: 300px; font-weight: 100; margin: 0"
      >
        {{ departCity }}到{{ desCity }}
      </p>
      <p style="font-size: 20px; text-indent: 300px; font-weight: 100">
        {{ date }}
      </p>
    </div>
    <div style="margin-top: 0px; background: #fff; height: 100%">
      <div style="height: 60px"></div>
      <div
        v-for="(it, index) in mylist"
        :key="index"
        style="margin-top: 20px; margin-left: 300px"
      >
        <each-flight
          :desCity="it.desCity"
          :departCity="it.departCity"
          :departAirport="it.departAirport"
          :desAirport="it.desAirport"
          :departTime="it.departTime"
          :desTime="it.desTime"
          :company="it.company"
          :time="it.time"
          :low="it.low"
          :mid="it.mid"
          :high="it.high"
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
      departCity: "重庆",
      desCity: "北京",
      date: "2021-5-22",
      mylist: [
        {
          departCity: "重庆",
          desCity: "北京",
          departAirport: "江北国际机场",
          desAirport: "大兴国际机场",
          departTime: "18:00",
          desTime: "21:00",
          time: "3h",
          low: "1000",
          mid: "2000",
          high: "3000",
          company: "南方航空",
        },
        {
          departCity: "重庆",
          desCity: "北京",
          departAirport: "江北国际机场",
          desAirport: "首都国际机场",
          departTime: "17:00",
          desTime: "20:00",
          time: "3h",
          low: "1500",
          mid: "2000",
          high: "3000",
          company: "四川航空",
        },
        {
          departCity: "重庆",
          desCity: "北京",
          departAirport: "江北国际机场",
          desAirport: "大兴国际机场",
          departTime: "14:00",
          desTime: "17:00",
          time: "3h",
          low: "1000",
          mid: "2500",
          high: "3500",
          company: "东方航空",
        },
      ],
    };
  },
  methods: {
    toMain: function () {
      this.$router.push("/");
    },
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
#t2 {
  height: 120px;
  margin: 0;
  background: white;
  color: #2e5c99;
  line-height: 120px;
  font-size: 35px;
  font-family: serif;
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
</style>
