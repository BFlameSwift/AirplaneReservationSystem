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
    <div style="margin-top: 200px; background: #fff; height: 80%">
      <el-select
        v-model="value"
        style="position:absolute;width: 200px; top: 300px; left: 1350px"
      >
        <el-option
          v-for="it in ellist"
          :key="it.value"
          :value="it.value"
          :label="it.lable"
        ></el-option>
      </el-select>
      <blue-botton
        style="position:absolute;top: 400px; left: 1350px; width: 150px"
        msg="查询"
      />
      <blue-botton
        style="position:absolute;top: 400px; left: 1550px; width: 150px"
        msg="添加航班"
        @click.native="toaddFlight"
      />
      <div style="height: 60px"></div>
      <div
        v-for="(it, index) in flights"
        :key="index"
        style="margin-left: 300px; margin-top: 20px"
      >
        <each-flight-admin></each-flight-admin>
      </div>
    </div>
  </div>
</template>
<script>
import BlueBotton from "../components/BlueBotton.vue";
import EachFlightAdmin from "../components/EachFlightAdmin.vue";
export default {
  name: "admin",
  data() {
    return {
      ellist: [
        {
          value: "0",
          lable: "按航班号查询",
        },
        {
          value: "1",
          lable: "按出发城市查询",
        },
        {
          value: "2",
          lable: "按到达城市查询",
        },
        {
          value: "3",
          lable: "按日期查询",
        },
      ],
      value: "0",
      flights: [{}, {}, {}, {}],
    };
  },
  components: {
    BlueBotton,
    EachFlightAdmin,
  },
  methods: {
    toaddFlight: function () {
      this.$router.push("/addFlight");
      console.log("xxxx");
    },
  },
};
</script>
<style scoped>
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