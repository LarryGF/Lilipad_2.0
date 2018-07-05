<template>

  <div id="app" >
    <Container/>
  
    
  </div>
</template>



<script>

import Container from './components/Container.vue';

export default {
  name: 'App',
  data() {
      return {  
          
          

          }
    },
  components: {
    Container
  }
}
</script>



<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  min-height: 100%;

  
}

img {
  width: 80px;

}
html, body {
    height: 100%;
}
</style>
