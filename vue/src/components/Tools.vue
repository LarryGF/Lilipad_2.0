<template>
    <md-content>

      <md-list>
          <md-list-item>
              <h4>Agregar al programa los elementos de su Centro de Datos a evaluar</h4>
              <!-- <md-button class="md-primary md-raised" @click="dialog_active=true">Mapear</md-button> -->
          </md-list-item>
          <md-divider></md-divider>
      <md-list-item>
        <md-field>
            <label>Usuario de Opennebula</label>
            <md-input v-model="one_user" required></md-input>
        </md-field>
      
       <md-field>
            <label>Password de Opennebula</label>
            <md-input v-model="one_pass" required></md-input>
        </md-field>

         <md-field>
            <label>Hostname(IP) de Opennebula</label>
            <md-input v-model="one_ip" required></md-input>
        </md-field>
      
      
    </md-list-item> 
    <md-list-item>
        
        <md-field>
            <label>Usuario de Proxmox</label>
            <md-input v-model="prox.prox_user" required></md-input>
        </md-field>
      
       <md-field>
            <label>Password de Proxmox</label>
            <md-input v-model="prox.prox_pass" required></md-input>
        </md-field>

         <md-field>
            <label>Hostname(IP) de Proxmox</label>
            <md-input v-model="prox.prox_ip" required></md-input>
        </md-field>
        
    </md-list-item>      
    <md-list-item>
        <span>Enviar los datos para ser procesados</span>
        <md-button class="md-primary md-raised">Enviar</md-button>
    </md-list-item>
    <md-divider></md-divider>
      </md-list>

    
                
    </md-content>
</template>

<script>
export default {
    name: "Tools",
    data: () => ({
        dialog_active: false,
        one_user: null,
        one_pass: null,
        one_ip: null,
        result: null,
        amount: null,
        prox: {}
    }),
    components: {},
    methods: {
        tool: function(data) {
            eel.tools(data)(result => (this.result = result));
        }
    }
};
</script>
