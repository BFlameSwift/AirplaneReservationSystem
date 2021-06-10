<template>
  <div>
    <div>
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
    </div>
    <div style="margin-top: 250px; margin-left: 400px">
      <div style="margin-top: 50px">
        <label style="font-size: 15px; font-weight: 50">航班号:</label>
        <input v-model="flightid" style="width: 30%; margin-left: 1%"/>
      </div>
      <div style="margin-top: 50px">
        <label style="font-size: 15px; font-weight: 50">飞机类型:</label>
        <input v-model="plane_type" style="width: 30%; margin-left: 1%"/>
      </div>
      <div style="margin-top: 50px">
        <label style="font-size: 15px; font-weight: 50">出发城市:</label>
        <input v-model="departCity" style="width: 30%; margin-left: 1%"/>
      </div>
      <div style="margin-top: 50px">
        <label style="font-size: 15px; font-weight: 50">到达城市:</label>
        <input v-model="desCity" style="width: 30%; margin-left: 1%"/>
      </div>
      <div style="margin-top: 50px">
        <label style="font-size: 15px; font-weight: 50">出发机场:</label>
        <input v-model="departAirport" style="width: 30%; margin-left: 1%"/>
      </div>
      <div style="margin-top: 50px">
        <label style="font-size: 15px; font-weight: 50">到达机场:</label>
        <input v-model="desAirport" style="width: 30%; margin-left: 1%"/>
      </div>
      <div style="margin-top: 50px">
        <label style="font-size: 15px; font-weight: 50">经济舱价格:</label>
        <input v-model="low" style="width: 30%; margin-left: 1%"/>
      </div>
      <div style="margin-top: 50px">
        <label style="font-size: 15px; font-weight: 50">商务舱价格:</label>
        <input v-model="mid" style="width: 30%; margin-left: 1%"/>
      </div>
      <div style="margin-top: 50px">
        <label style="font-size: 15px; font-weight: 50">头等舱价格:</label>
        <input v-model="high" style="width: 30%; margin-left: 1%"/>
      </div>
      <div style="position:absolute;left:1400px;top:500px;">
        <label style="font-size: 15px; font-weight: 50">出发时间:</label>
        <input v-model="departTime" style="width: 100%; margin-left: 1%"/>
      </div>
      <div style="position:absolute;left:1400px;top:600px;">
        <label style="font-size: 15px; font-weight: 50">到达时间:</label>
        <input v-model="desTime" style="width: 100%; margin-left: 1%"/>
      </div>
      <label style="position:absolute;left:1400px;top:310px;font-size: 15px; font-weight: 50">出发日期:</label>
      <label style="position:absolute;left:1400px;top:400px;font-size: 15px; font-weight: 50">到达日期:</label>
      <div style="position:absolute;left:1500px;top:300px;">
        <el-date-picker
          v-model="start_date"
          type="date"
          value-format="yyyy-MM-dd">
          placeholder="选择出发日期"
          >
        </el-date-picker>
      </div>
      <div style="position:absolute;left:1500px;top:390px;">
        <el-date-picker
          v-model="ending_date"
          type="date"
          value-format="yyyy-MM-dd">
          placeholder="选择到达日期"
          >
        </el-date-picker>
      </div>
      <button
        type="button"
        class="button button--login button--round-s button--text-thick button--inverted button--size"
        style="position:absolute;left:1400px;top:800px;width: 300px; height: 60px"
        @click="confirmed"
      >
        确认并添加
      </button>
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
      start_date: '',
      ending_date: '',
      plane_type: ""
    };
  },
  methods: {
    toadmin: function () {
      this.$router.push("/admin");
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
    confirmed(){
      const formData = new FormData();
      formData.append("flight_number", this.flightid)
      formData.append("origination", this.departCity)
      formData.append("destination", this.desCity)
      formData.append("starting_time", this.departTime)
      formData.append("arrival_time", this.desTime)
      formData.append("first_class_price", this.high)
      formData.append("business_class_price", this.mid)
      formData.append("economy_class_price", this.low)
      formData.append("departure_airport", this.departAirport)
      formData.append("landing_airport", this.desAirport)
      formData.append("starting_date", this.start_date)
      formData.append("ending_date", this.ending_date)
      formData.append("plane_type", this.plane_type)
      console.log(this.start_date)
      console.log(this.ending_date)
      console.log(this.start_date)
      console.log(this.desTime)
      console.log(this.departTime)
      console.log(this.departCity)

      this.$http.post('api/background/entry_flight/', formData)
        .then(result => {
          console.log("hhh")
          if (result.data.status === 0) {
            this.$message({
              message: '成功！',
              type: 'success'
            });
            this.$router.go(-1);
          } else {
            this.$alert(result.data.msg, '添加失败', {
              confirmButtonText: '确定',
            });
          }
        })
    }
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
</style>
