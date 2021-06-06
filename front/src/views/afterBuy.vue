<template>
  <div style="width: 2000px; height: 1000px">
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
          承运方: {{ company }}
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
  methods: {
    toMycenter: function () {
      this.$router.push({ path: "/personal", query: {} });
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
</style>