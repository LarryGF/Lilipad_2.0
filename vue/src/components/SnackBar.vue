<template>
        <md-snackbar :md-position="position"  :md-active.sync="showSnackbar" :md-duration="isInfinity ? Infinity : duration" md-persistent>
      <span>{{mensaje}}</span>
      <!-- <md-button class="md-primary" @click="showSnackbar = false">Traba</md-button> -->
    </md-snackbar>
</template> 

<script type="text/javascript">
    export default {
        name:'Options',
        props:{
            showSnackbar:{
                type:Boolean,
                required:true
            },
            mensaje:{
                type:String,
                required:false
            }


        },
        data() {
            return {  
                    position:'left',
                    isInfinity:true,
                    duration:4000
                    

                    }
        },
        methods:{
            
            

        }
        
    }

</script> 
 
