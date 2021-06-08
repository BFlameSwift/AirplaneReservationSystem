<template>
  <div class="register_container" style="height: 1000px; width: 2000px">
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
      <!-- 登录 -->
    </div>
    <a class="title" style="top: 20%; left: 370px; color: rgb(0, 70, 132)"
    >免费注册</a
    >

    <a class="title" style="top: 20%; left: 1170px; color: rgb(0, 70, 132)"
    >*更多信息</a
    >

    <!-- 免费注册 -->
    <div class="register_form">
      <!-- 用户名 -->
      <h4
        style="color: rgb(0, 70, 132); position: absolute; left: 45%; top: 10%"
      >
        用户名
      </h4>
      <input v-model="username" class="info" style="top: 20%"/>
      <!-- 密码 -->
      <h4
        style="color: rgb(0, 70, 132); position: absolute; left: 45%; top: 30%"
      >
        密码
      </h4>
      <input v-model="password" class="info" style="top: 40%"/>
      <!-- 确认密码 -->
      <h4
        style="color: rgb(0, 70, 132); position: absolute; left: 45%; top: 50%"
      >
        确认密码
      </h4>
      <input v-model="conPassword" class="info" style="top: 60%"/>
      <!-- 电子邮箱 -->
      <h4
        style="color: rgb(0, 70, 132); position: absolute; left: 45%; top: 70%"
      >
        电子邮箱
      </h4>
      <input v-model="email" class="info" style="top: 80%"/>
    </div>

    <div class="verticle"></div>

    <!-- 更多信息 -->
    <div class="moreInfo_form">
      <!-- 用户名 -->
      <h4
        style="color: rgb(0, 70, 132); position: absolute; left: 45%; top: 10%"
      >
        真实姓名
      </h4>
      <input v-model="realname" class="info" style="top: 20%"/>
      <!-- 性别 -->
      <h4
        style="color: rgb(0, 70, 132); position: absolute; left: 45%; top: 30%"
      >
        性别
      </h4>

      <!-- 出生日期 -->
      <h4
        style="color: rgb(0, 70, 132); position: absolute; left: 45%; top: 50%"
      >
        手机号
      </h4>
      <input v-model="phoneNum" class="info" style="top: 60%"/>
      <!-- *身份证号 -->
      <h4
        style="color: rgb(0, 70, 132); position: absolute; left: 45%; top: 70%"
      >
        身份证号
      </h4>
      <input v-model="Id" class="info" style="top: 80%"/>
    </div>
    <!-- 注册 -->
    <button
      type="button"
      class="button button--login button--round-s button--text-thick button--inverted button--size"
      style="
        position: absolute;
        left: 350px;
        top: 85%;
        width: 300px;
        height: 60px;
      "
      @click="register"
    >
      注册
    </button>

    <!-- 日期选择 -->
<!--    <div class="date" data-invalid="true">-->

<!--      <div class="select">-->
<!--        <select-->
<!--          aria-required="true"-->
<!--          id="birthday"-->
<!--          name="birthday"-->
<!--          class="input-primary"-->
<!--          aria-invalid="true"-->
<!--          v-model="day"-->
<!--        >-->
<!--          <option value="">日</option>-->
<!--          <option value="01">01</option>-->
<!--          <option value="02">02</option>-->
<!--          <option value="03">03</option>-->
<!--          <option value="04">04</option>-->
<!--          <option value="05">05</option>-->
<!--          <option value="06">06</option>-->
<!--          <option value="07">07</option>-->
<!--          <option value="08">08</option>-->
<!--          <option value="09">09</option>-->
<!--          <option value="10">10</option>-->
<!--          <option value="11">11</option>-->
<!--          <option value="12">12</option>-->
<!--          <option value="13">13</option>-->
<!--          <option value="14">14</option>-->
<!--          <option value="15">15</option>-->
<!--          <option value="16">16</option>-->
<!--          <option value="17">17</option>-->
<!--          <option value="18">18</option>-->
<!--          <option value="19">19</option>-->
<!--          <option value="20">20</option>-->
<!--          <option value="21">21</option>-->
<!--          <option value="22">22</option>-->
<!--          <option value="23">23</option>-->
<!--          <option value="24">24</option>-->
<!--          <option value="25">25</option>-->
<!--          <option value="26">26</option>-->
<!--          <option value="27">27</option>-->
<!--          <option value="28">28</option>-->
<!--          <option value="29">29</option>-->
<!--          <option value="30">30</option>-->
<!--          <option value="31">31</option>-->
<!--        </select>-->
<!--      </div>-->
<!--    </div>-->
<!--    &lt;!&ndash; 月 &ndash;&gt;-->
<!--    <div class="month">-->
<!--      <div class="select">-->
<!--        <select-->
<!--          aria-required="true"-->
<!--          id="birthmonth"-->
<!--          name="birthmonth"-->
<!--          class="input-primary"-->
<!--          v-model="month"-->
<!--        >-->
<!--          <option value="">月</option>-->
<!--          <option value="01">January</option>-->
<!--          <option value="02">February</option>-->
<!--          <option value="03">March</option>-->
<!--          <option value="04">April</option>-->
<!--          <option value="05">May</option>-->
<!--          <option value="06">June</option>-->
<!--          <option value="07">July</option>-->
<!--          <option value="08">August</option>-->
<!--          <option value="09">September</option>-->
<!--          <option value="10">October</option>-->
<!--          <option value="11">November</option>-->
<!--          <option value="12">December</option>-->
<!--        </select>-->
<!--      </div>-->
<!--    </div>-->
<!--    &lt;!&ndash; 年 &ndash;&gt;-->
<!--    <div class="year">-->
<!--      <div class="select">-->
<!--        <select-->
<!--          aria-required="true"-->
<!--          id="birthyear"-->
<!--          name="birthyear"-->
<!--          class="input-primary"-->
<!--          v-model="year"-->
<!--        >-->
<!--          <option value="">年</option>-->
<!--          <option value="2021">2021</option>-->
<!--          <option value="2020">2020</option>-->
<!--          <option value="2019">2019</option>-->
<!--          <option value="2018">2018</option>-->
<!--          <option value="2017">2017</option>-->
<!--          <option value="2016">2016</option>-->
<!--          <option value="2015">2015</option>-->
<!--          <option value="2014">2014</option>-->
<!--          <option value="2013">2013</option>-->
<!--          <option value="2012">2012</option>-->
<!--          <option value="2011">2011</option>-->
<!--          <option value="2010">2010</option>-->
<!--          <option value="2009">2009</option>-->
<!--          <option value="2008">2008</option>-->
<!--          <option value="2007">2007</option>-->
<!--          <option value="2006">2006</option>-->
<!--          <option value="2005">2005</option>-->
<!--          <option value="2004">2004</option>-->
<!--          <option value="2003">2003</option>-->
<!--          <option value="2002">2002</option>-->
<!--          <option value="2001">2001</option>-->
<!--          <option value="2000">2000</option>-->
<!--          <option value="1999">1999</option>-->
<!--          <option value="1998">1998</option>-->
<!--          <option value="1997">1997</option>-->
<!--          <option value="1996">1996</option>-->
<!--          <option value="1995">1995</option>-->
<!--          <option value="1994">1994</option>-->
<!--          <option value="1993">1993</option>-->
<!--          <option value="1992">1992</option>-->
<!--          <option value="1991">1991</option>-->
<!--          <option value="1990">1990</option>-->
<!--          <option value="1989">1989</option>-->
<!--          <option value="1988">1988</option>-->
<!--          <option value="1987">1987</option>-->
<!--          <option value="1986">1986</option>-->
<!--          <option value="1985">1985</option>-->
<!--          <option value="1984">1984</option>-->
<!--          <option value="1983">1983</option>-->
<!--          <option value="1982">1982</option>-->
<!--          <option value="1981">1981</option>-->
<!--          <option value="1980">1980</option>-->
<!--          <option value="1979">1979</option>-->
<!--          <option value="1978">1978</option>-->
<!--          <option value="1977">1977</option>-->
<!--          <option value="1976">1976</option>-->
<!--          <option value="1975">1975</option>-->
<!--          <option value="1974">1974</option>-->
<!--          <option value="1973">1973</option>-->
<!--          <option value="1972">1972</option>-->
<!--          <option value="1971">1971</option>-->
<!--          <option value="1970">1970</option>-->
<!--          <option value="1969">1969</option>-->
<!--          <option value="1968">1968</option>-->
<!--          <option value="1967">1967</option>-->
<!--          <option value="1966">1966</option>-->
<!--          <option value="1965">1965</option>-->
<!--          <option value="1964">1964</option>-->
<!--          <option value="1963">1963</option>-->
<!--          <option value="1962">1962</option>-->
<!--          <option value="1961">1961</option>-->
<!--          <option value="1960">1960</option>-->
<!--          <option value="1959">1959</option>-->
<!--          <option value="1958">1958</option>-->
<!--          <option value="1957">1957</option>-->
<!--          <option value="1956">1956</option>-->
<!--          <option value="1955">1955</option>-->
<!--          <option value="1954">1954</option>-->
<!--          <option value="1953">1953</option>-->
<!--          <option value="1952">1952</option>-->
<!--          <option value="1951">1951</option>-->
<!--          <option value="1950">1950</option>-->
<!--          <option value="1949">1949</option>-->
<!--          <option value="1948">1948</option>-->
<!--          <option value="1947">1947</option>-->
<!--          <option value="1946">1946</option>-->
<!--          <option value="1945">1945</option>-->
<!--          <option value="1944">1944</option>-->
<!--          <option value="1943">1943</option>-->
<!--          <option value="1942">1942</option>-->
<!--          <option value="1941">1941</option>-->
<!--          <option value="1940">1940</option>-->
<!--          <option value="1939">1939</option>-->
<!--          <option value="1938">1938</option>-->
<!--          <option value="1937">1937</option>-->
<!--          <option value="1936">1936</option>-->
<!--          <option value="1935">1935</option>-->
<!--          <option value="1934">1934</option>-->
<!--          <option value="1933">1933</option>-->
<!--          <option value="1932">1932</option>-->
<!--          <option value="1931">1931</option>-->
<!--          <option value="1930">1930</option>-->
<!--          <option value="1929">1929</option>-->
<!--          <option value="1928">1928</option>-->
<!--          <option value="1927">1927</option>-->
<!--          <option value="1926">1926</option>-->
<!--          <option value="1925">1925</option>-->
<!--          <option value="1924">1924</option>-->
<!--          <option value="1923">1923</option>-->
<!--          <option value="1922">1922</option>-->
<!--        </select>-->
<!--      </div>-->
<!--    </div>-->


    <!-- 性别选项 -->
    <div class="radio">
      <label class="gender-male-lbl" for="male">
        <input
          class="primary"
          value="Male"
          name="gender"
          id="male"
          type="radio"
          @click="sex='male'"
        />
        <span variant="Variant1">男性</span>
      </label>

      <label class="gender-female-lbl" for="Female"
      ><input
        class="primary"
        value="Female"
        name="gender"
        id="Female"
        type="radio"
        @click="sex='female'"
      /><span>女性</span></label
      >
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      screenWidth: '',
      screenHeight: '',
      month: '',
      day: '',
      year: '',
      sex: '',
      username: '',
      password: '',
      conPassword: '',
      email: '',
      Id: '',
      realname: '',
      phoneNum: '',
      date: '2021-4-8'
    };
  },
  mounted() {
    this.screenWidth = document.body.clientWidth;
    this.screenHeight = document.body.clientHeight;
    window.onresize = () => {
      return (() => {

        this.screenWidth = document.body.clientWidth;
        this.screenHeight = document.body.clientHeight;
      })();
    };
  },
  methods: {
    // mouseover(index){
    //   this.style[index]="color:green;"
    // },
    // mouseleave(index){
    //   this.style[index]=""
    // },
    register() {
      const formData = new FormData();
      formData.append("real_name", this.realname)
      formData.append("sex", this.sex)
      formData.append("username", this.username)
      formData.append("password1", this.password)
      formData.append("password2", this.conPassword)
      formData.append("email", this.email)
      formData.append("Id_number", this.Id)
      formData.append("phone_number", this.phoneNum)
      formData.append("birthday", this.date)
      console.log(this.username)
      console.log(this.password)
      console.log(this.Id)
      console.log(this.conPassword)
      console.log(this.email)
      console.log(this.phoneNum)
      console.log(this.realname)
      console.log(this.sex)
      this.$http.post('/api/register/', formData)
        .then(result => {
          if (result.data.status === 0) {
            // eslint-disable-next-line no-undef
            this.$alert('请等待确认邮件', '提示', {
              confirmButtonText: '确定',
            });
            console.log(result.data)
            this.$router.push('login')
          } else {
            // eslint-disable-next-line no-undef
            this.$alert(result.data.msg, '注册失败', {
              confirmButtonText: '确定',
            });
          }
          console.log(result.data)
          this.msg = result.data.msg
          console.log(result)


        })
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
    }
  },
};
</script>

<style lang="less" scoped>
.input-primary {
  text-decoration: none;
  font: inherit;
  font-size: 1.2rem;
  background-color: #FFFFFF;
  color: #666666;
  padding: 0.8rem;
  -webkit-appearance: none;
  position: absolute;
  width: 120px;
}

.primary {
  width: 30px;
  height: 20px;
}

.radio {
  position: absolute;
  left: 59%;
  top: 50%;
  font-family: Helvetica, Arial, sans-serif;
  font-size: 32.5%;
  -webkit-text-size-adjust: 100%;
  box-sizing: border-box;
  border: none;
  font-weight: normal;
  font-style: normal;
  color: inherit;
  text-decoration: none;
  outline: 0;
}

.gender-male-lbl {
  -webkit-text-size-adjust: 100%;
  box-sizing: border-box;
  font-style: normal;
  text-decoration: none;
  outline: 0;
  font-family: Helvetica, Arial, sans-serif;
  font-size: 20px;
  line-height: 2.4rem;
  position: relative;
  cursor: pointer;
  color: #666666;
  display: inline-block;
}

.gender-female-lbl {
  -webkit-text-size-adjust: 100%;
  box-sizing: border-box;
  font-style: normal;
  text-decoration: none;
  font-family: Helvetica, Arial, sans-serif;
  font-size: 20px;
  line-height: 2.4rem;
  position: relative;
  cursor: pointer;
  color: #666666;
  display: inline-block;
  margin-left: 6rem;
}

.info {
  height: 50px;
  width: 560px;
  position: absolute;
  left: 45%;
  border: 0.5px solid #adadad;
  border-radius: 1px;
  font-size: 22px;
}

.color {
  color: rgb(40, 40, 116);
}

.register_container {
  background-color: white;
  position: absolute;
}

.title {
  position: absolute;
  font-size: 50px;
}

.line {
  position: absolute;
  bottom: 7%;
  font-size: 20px;
  /* color: black; */
  color: #54545e;
  cursor: pointer;
}

.register_form {
  position: absolute;
  top: 25%;
  width: 40%;
  height: 60%;
  padding: 0 10px;
}

.moreInfo_form {
  position: absolute;
  top: 25%;
  left: 40%;
  width: 40%;
  height: 60%;
  padding: 0 10px;
}

.verticle {
  position: absolute;
  left: 53%;
  top: 30%;
  height: 55%;
  border-right: 2px solid rgb(235, 226, 226);
}

.head {
  position: absolute;
  background-color: #ffffff;
  color: black;
  top: 0%;
  height: 16%;
  width: 100%;
}

.hr {
  position: relative;
  margin-top: 110px;
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
  color: rgb(0, 70, 132);
}

.button--login.button--inverted:hover {
  background-color: #1992ce;
  color: #fcfcfd;
}

.month {
  position: absolute;
  left: 69%;
  top: 62%;
  color: inherit;
  width: 120px;
  height: 70px;
}

.date {
  position: absolute;
  left: 73%;
  top: 62%;
  border: none;
  color: inherit;
}

.year {
  position: absolute;
  left: 59%;
  top: 62%;
  font-weight: normal;
  font-style: normal;
  color: inherit;
}
</style>
