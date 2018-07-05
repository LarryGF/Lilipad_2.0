<template>
        <div>   
            <h3>Actualizar credenciales</h3>
                
            <md-field>
                <label>Introduzca su password</label>
                <md-input v-model="password" type="password"></md-input>
            </md-field>
            <md-button  class="md-primary md-raised" @click="save_pass(password)">Actualizar</md-button>

        </div>
</template> 

<script type="text/javascript">
    export default {
        name:'Options',
        data() {
            return {  
                    password:'',
                    }
        },
        methods:{
            save_pass: function(password){
                eel.save_password(password)(message => this.message = message);
                this.show=false;
                this.password='';
            },
            

        }
        
    }

</script> 
