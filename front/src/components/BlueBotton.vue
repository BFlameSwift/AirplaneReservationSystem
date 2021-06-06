<template>
<button>{{msg}}</button>
</template>
<script>
export default{
    name:'BlueButton',
    props:{
        msg:String,
    }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
button{
    position: relative;
    width: 100px; 
    height: 50px;
    border: none;
    background: #2E5C99;
    color: #fff;
    -webkit-transition: background-color 0.3s, color 0.3s;
    transition: background-color 0.3s, color 0.3s;
    -moz-osx-font-smoothing: grayscale;
    font-weight: 300;
    border-radius: 1px;
    font-size: 16px;
}
button:hover{
    background-color: #2671D3;
    color: #fcfcfd;
}
</style>
