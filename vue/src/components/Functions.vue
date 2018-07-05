<template>
    <md-content>
    <md-list>
    <md-list-item class="md-inset">
    <h3>Agregar un anuncio offline</h3>

    <md-button class="md-primary md-raised" @click="showDialog=true,message='create'">Agregar</md-button>
    </md-list-item>
    <md-divider></md-divider>
    <md-list-item class="md-inset">
    <h3>Sincronizar anuncios</h3>
    <md-button class="md-primary md-raised" :disabled="disabled" @click="synchronize()">Sincronizar</md-button>
    </md-list-item>
    </md-list>

 <Dialog :mode="message" :active="showDialog" @close="showDialog=false" />
 <Dialog_sync :dialactive="showDialog_sync" :amount="amount" @close="showDialog_sync=false"/>
</md-content>
</template>

<script type="text/javascript">
    import Dialog from './Dialog.vue';
    import Dialog_sync from './Dialog_sync.vue'


    export default {
        name:'Functions',
        props:{
            disabled:{
                type:Boolean,
                required:true,
            },
        },
        data() {
        return {
      message:'',
      amount:0,
      showDialog:false,
      showDialog_sync:false,
      sincerrors:'',
      }
    },
    methods:{
        synchronize() {
            this.showDialog_sync=true
            console.log('synchronizing')
            eel.syncMails()(response => console.log(response))
            setInterval(this.update_bar,4000)

      },

        update_bar() {
            
            eel.mail_data()(result => {console.log(result)});
        },

    },
    components:{
        Dialog,
        Dialog_sync,
    }
    }

</script>
