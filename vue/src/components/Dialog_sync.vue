<template>
  <md-dialog :md-active.sync="dialactive" :md-click-outside-to-close="false">
    <md-steppers :md-active-step.sync="active" md-linear>
      <md-step id="first" md-label="Sincronizando" :md-error="firstStepError" :md-editable="false" :md-done.sync="first">
        
        <h4 v-if="!firstStepError" style="text-align: center;">Sincronizando sus anuncios. Sea paciente, puede demorar un poco... {{amount}}</h4>
            
        <h4 v-if="firstStepError" style="text-align: center">{{sincerror}}</h4>
        
        <md-buton v-if="amount==100" class="md-primary md-raised" @click="setDone('first','second')">Ok</md-buton>

        <md-progress-bar md-mode="determinate" :md-value="amount"></md-progress-bar>
        
    


       </md-step>

      
      <md-step id="second" md-label="Listo" :md-done.sync="third" :md-editable="false">
        
        <md-button class="md-raised md-primary" @click="$emit('close')">Done</md-button>
      </md-step>
    </md-steppers>
  </md-dialog>
</template>

<script>
export default {
    name: "Dialog_sync",
    props: {
        dialactive: {
            type: Boolean,
            required: true
        },
        amount: {
            type: Number
        }
    },

    data: () => ({
        active: "first",
        first: false,
        second: false,
        third: false,
        firstStepError: null,

        sincerror: null
    }),

    methods: {
        setDone(id, index) {
            this[id] = true;

            this.firstStepError = null;

            if (index) {
                this.active = index;
            }
        },
        setError() {
            this.firstStepError = "This is an error!";
        }
    }
};
</script>

<style lang="css" scoped>
</style>