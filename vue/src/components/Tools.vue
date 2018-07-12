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
            <md-input v-model="data.one.one_user" required></md-input>
        </md-field>
      
       <md-field>
            <label>Password de Opennebula</label>
            <md-input v-model="data.one.one_pass" required></md-input>
        </md-field>

         <md-field>
            <label>Hostname(IP) de Opennebula</label>
            <md-input v-model="data.one.one_ip" required></md-input>
        </md-field>
      
      
    </md-list-item> 
    <md-list-item>
        
        <md-field>
            <label>Usuario de Proxmox</label>
            <md-input v-model="data.prox.prox_user" required></md-input>
        </md-field>
      
       <md-field>
            <label>Password de Proxmox</label>
            <md-input v-model="data.prox.prox_pass" required></md-input>
        </md-field>

         <md-field>
            <label>Hostname(IP) de Proxmox</label>
            <md-input v-model="data.prox.prox_ip" required></md-input>
        </md-field>
        
    </md-list-item>     
    <md-list-item>
        
        <md-field>
            <label>Usuario de Zabbix</label>
            <md-input v-model="data.zabbix.zabbix_user" required></md-input>
        </md-field>
      
       <md-field>
            <label>Password de Zabbix</label>
            <md-input v-model="data.zabbix.zabbix_pass" required></md-input>
        </md-field>

         <md-field>
            <label>Hostname(IP) de Zabbix</label>
            <md-input v-model="data.zabbix.zabbix_ip" required></md-input>
        </md-field>
        <md-field>
            <label>Nombre de la base de datos de Zabbix</label>
            <md-input v-model="data.zabbix.zabbix_db" required></md-input>
        </md-field>
        
    </md-list-item>      
    <md-list-item>
        <span>Enviar los datos para ser procesados</span>
        <md-button class="md-primary md-raised" @click="map(data)">Enviar</md-button>
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
        result: null,
        amount: null,
        data: {
            one: {
                one_user: null,
                one_pass: null,
                one_ip: null
            },
            prox: {
                prox_user: null,
                prox_pass: null,
                prox_ip: null
            },
            zabbix: {
                zabbix_user: null,
                zabbix_pass: null,
                zabbix_ip: null,
                zabbix_db: null
            }
        }
    }),
    components: {},
    methods: {
        map: function(data) {
            eel.map(data)(result => (this.result = result));
        }
    }
};
</script>
