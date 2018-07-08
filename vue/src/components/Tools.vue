<template>
    <md-content>
        {{prox}}
      
    <md-dialog-prompt
      :md-active.sync="dialog_active"
      v-model="amount"
      md-title="Proxmox"
      md-input-maxlength="2"
      md-input-placeholder="Cantidad de instancias de Proxmox en su CD"
      md-confirm-text="Hecho" />

      <md-list>
          <md-list-item>
              <span>Mapear los componentes de su CD</span>
              <md-button class="md-primary md-raised" @click="dialog_active=true">Mapear</md-button>
          </md-list-item>
          <md-divider></md-divider>
      <md-list-item v-if="amount">
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
    <md-list-item v-for="i in Number(amount)" :key="i">
        
        <md-field>
            <label>Usuario de Proxmox</label>
            <md-input v-model="prox.i.prox_user" required></md-input>
        </md-field>
      
       <md-field>
            <label>Password de Proxmox</label>
            <md-input v-model="prox.i.prox_pass" required></md-input>
        </md-field>

         <md-field>
            <label>Hostname(IP) de Proxmox</label>
            <md-input v-model="prox.i.prox_ip" required></md-input>
        </md-field>
        
    </md-list-item>      
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
        },
        transform: function() {
            this.amount = Number(this.amount);
            console.log(this.amount);
        }
    }
};
</script>
