<template>
  <div>
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
    <div style="margin-top: 250px; margin-left: 400px">
      <div style="margin-top: 50px">
        <label style="font-size: 15px; font-weight: 50">航班号:</label>
        <input v-model="flightid" style="width: 30%; margin-left: 1%" />
      </div>
      <div style="margin-top: 50px">
        <label style="font-size: 15px; font-weight: 50">出发城市:</label>
        <input v-model="departCity" style="width: 30%; margin-left: 1%" />
      </div>
      <div style="margin-top: 50px">
        <label style="font-size: 15px; font-weight: 50">到达城市:</label>
        <input v-model="desCity" style="width: 30%; margin-left: 1%" />
      </div>
      <div style="margin-top: 50px">
        <label style="font-size: 15px; font-weight: 50">出发机场:</label>
        <input v-model="departAirport" style="width: 30%; margin-left: 1%" />
      </div>
      <div style="margin-top: 50px">
        <label style="font-size: 15px; font-weight: 50">到达机场:</label>
        <input v-model="desAirport" style="width: 30%; margin-left: 1%" />
      </div>
      <div style="margin-top: 50px">
        <label style="font-size: 15px; font-weight: 50">经济舱价格:</label>
        <input v-model="low" style="width: 30%; margin-left: 1%" />
      </div>
      <div style="margin-top: 50px">
        <label style="font-size: 15px; font-weight: 50">商务舱价格:</label>
        <input v-model="mid" style="width: 30%; margin-left: 1%" />
      </div>
      <div style="margin-top: 50px">
        <label style="font-size: 15px; font-weight: 50">头等舱价格:</label>
        <input v-model="high" style="width: 30%; margin-left: 1%" />
      </div>
      <label style="font-size: 15px; font-weight: 50">时间选择:</label>
      <el-date-picker
        v-model="departTime"
        type="datetime"
        placeholder="选择出发日期时间"
        style="margin-top: 50px; margin-left: 20px"
      >
      </el-date-picker>
      <el-date-picker
        v-model="desTime"
        type="datetime"
        placeholder="选择到达时间"
        style="margin-top: 50px; margin-left: 20px"
      >
      </el-date-picker>
      <blue-botton
        style="margin-left: 800px"
        msg="确认并添加"
        @click="confirmAndAdd"
      ></blue-botton>
    </div>
  </div>
</template>
<script>
import BlueBotton from "../components/BlueBotton.vue";
export default {
  name: "addFlight",
  components: {
    BlueBotton,
  },
  data() {
    return {
      flightid: "",
      departAirport: "",
      desAirport: "",
      departTime: "",
      desTime: "",
      departCity: "",
      desCity: "",
      low: "",
      mid: "",
      high: "",
      company: "",
      time: "",
    };
  },
  methods: {
    toadmin: function () {
      this.$router.push("/admin");
    },
    confirmAndADD: function () {
      this.$axios
        .post("", {})
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
<style scoped>
input {
  border-radius: 0;
  margin-left: 0;
  border-top: 0;
  border-left: 0;
  border-right: 0;
  border-bottom: 2px solid #dbdbdb;
  height: 40px;
  outline: none;
  font-size: 17px;
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
</style>