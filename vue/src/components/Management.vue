<template>
  <div>

  	<md-empty-state v-if="adds.length == 0"
      md-label="No tiene anuncios locales"
      md-description="En estos momentos no tiene anuncios almacenados en la base de datos, sincronice con su cuenta o cree un anuncio offline para poblar esta lista.">
     
    </md-empty-state>

    <md-list class="md-double-line" v-for="add in adds" :key=add.id>
      <md-subheader>
        <p><strong>{{add.title}}</strong>   <br>      
        <strong>{{add.images}}</strong>   <span>img1</span></p>
      </md-subheader>
	

      <md-list-item>
        <md-icon class="fa fa-pie-chart"></md-icon>
        <div class="md-list-item-text">
          <span>
            <strong>Ultimo reposteo: </strong>{{add.last_repost}}</span>

        </div>

        <div class="md-list-item-text" v-if="deladd != add.id">
          <span>
            <strong>Veces reposteado:</strong> {{add.reposted}}</span>

        </div>
        <h5 style="color:red" v-if="deladd == add.id">Esta seguro de que desea borrar el anuncio?</h5>
        <md-button v-if="deladd != add.id" class="md-raised md-accent" @click="deladd=add.id">Eliminar</md-button>
        <md-button v-if="deladd == add.id" class="md-raised md-accent" @click="delete_announce(add.id),deladd=-1">Eliminar</md-button>
        <md-button v-if="deladd == add.id" class="md-raised md-accent" @click="deladd=-1">Cancelar</md-button>

      </md-list-item>
      <md-divider></md-divider>

    </md-list>
  </div>
</template>

<script type="text/javascript">
  export default {

    data() {
      return {
        adds: [],
        deladd: -1
      }
    },
    methods: {
      update: function () {
        eel.get_Announces()(adds => {if (this.adds != adds){ this.adds = adds}})
      },
      delete_announce: function (id) {
        eel.delete_announce(id)()
      }
    },
    created() {
      setInterval(this.update, 500);

    }
  }

</script>
