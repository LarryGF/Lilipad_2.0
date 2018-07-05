<template>

<md-content>
<h3>Mantenga sus anuncios siempre arriba </h3>
 <md-button class="md-raised md-primary" :disabled="disabled" @click="post()">Repostear ({{postnum}})</md-button>
<Dialog :mode="message" :active="showDialog" @disable="$emit('disabled')" @close="showDialog=false" />

</md-content>
</template>

<script type="text/javascript">
    import Dialog from './Dialog.vue';

    export default {
        name:'Main',
        props:{
            disabled:{
                type:Boolean,
                required:true,
            },
        },
        data() {
        return {
      message:'',
      // disabled:false,
      showDialog:'',
      started:false,
      postnum: 0
  }
    },
    computed:{
        onLoad: function (){
            if (!this.started){
        eel.py_is_saved()(message => {this.message = message.msg;this.showDialog = message.active});
      }
      },

    postnump: function () {
      eel.announce_size()(num => this.postnum = num)
    }

    },

        methods:{
            post: function () {
        eel.open_browser_tabs()(num => this.postnum=num)
      }

  },
        components:{
            Dialog,
        },
  created(){
    this.onLoad;
    setInterval(this.postnump, 1000)
  }

}

</script>

