<template>
  <div class="page-container">
    <md-app  md-mode="fixed">
      <md-app-toolbar class="md-large md-dense " :style="alert">

          <div class="md-toolbar-row" >
          <div class="md-toolbar-section-start">

          </div>
          <div class="md-toolbar-section-end">

          </div>
            <h1 ><img src="/static/logo1.png">LiliPad 2.0</h1>
          </div>

          <div class="md-toolbar-row">
            <div class="md-toolbar-section-start">

          </div>
          <div class="md-toolbar-section-end">

          </div>
          <md-tabs class="md-primary" md-aligment="fixed" @md-changed="change" >
            <md-tab id="step_1" md-label="Paso 1"></md-tab>
            <md-tab id="step_2" md-label="Paso 2"></md-tab>
            <md-tab id="step_3" md-label="Paso 3"></md-tab>
            <md-tab id="step_4" md-label="Paso 4"></md-tab>
            <md-tab id="step_5" md-label="Paso 5"></md-tab>
            <md-tab id="step_6" md-label="Paso 6"></md-tab>
            <md-tab id="step_7" md-label="Paso 7"></md-tab>

          </md-tabs>
        </div>
      </md-app-toolbar>






      <md-app-content>

      <div v-if="active =='step_1'">
        
        <Step1/>
      </div>
      <div v-if="active =='step_2'">
        
        <Step2/>
      </div>
      <div v-if="active =='step_3'">
        <Step3/>
      </div>
      <div v-if="active =='step_4'">
        <Step4/>
        </div>
        <div v-if="active =='step_5'">
          <Step5/>
      </div>
      <div v-if="active =='step_6'">
        <Step6/>
      </div>
      <div v-if="active =='step_7'">
        <Step7/>
      </div>
      
      </md-app-content>
    </md-app>
  </div>
</template>

<style lang="css" scoped>
.md-app {
    min-height: 100%;
    border: 1px solid rgba(#000, 0.12);
}
img {
    height: 45px;
    width: 45px;
    margin-right: 10px;
}
h1 {
    margin-top: 30px;
    margin-bottom: 10px;
}
</style>

<script>
import Step1 from "./Step1.vue";
import Step2 from "./Step2.vue";
import Step3 from "./Step3.vue";
import Step4 from "./Step4.vue";
import Step5 from "./Step5.vue";
import Step6 from "./Step6.vue";
import Step7 from "./Step7.vue";
import Tools from "./Tools.vue";

export default {
    name: "Container",
    data: () => ({
        active: "step_1",
        alert: "background-color:black;color:white",
        showSnackBar: false,
        message: ""
    }),
    computed: {},
    methods: {
        change: function(activeTab) {
            this.active = activeTab;
        }
    },
    created() {},
    components: {
        Step1,
        Step2,
        Step3,
        Step4,
        Step5,
        Step6,
        Step7,
        Tools
    }
};
</script>
