<template>

<md-content>
<md-dialog  v-if="mode == 'tab_serv'" :md-active.sync="active" @md-closed="$emit('close')">
        <md-dialog-title>Agregar Servivicio</md-dialog-title>
        <md-dialog-content>
					<md-field>
						<label>Servicio</label>
						<md-input v-model="data.tab_service" required></md-input>
					</md-field>
		
					<md-field>
						<label>Subservicio</label>
						<md-input v-model="data.tab_subservice" required></md-input>
					</md-field>

					<md-field>
						<label>Solucion</label>
						<md-input v-model="data.tab_solution" required></md-input>
					</md-field>

					<md-field>

					<md-select v-model="data.tab_gestor" placeholder="Gestor de Nube">
						<md-option  value="OpenNebula">OpenNebula</md-option>
						<md-option  value="Proxmox">Proxmox</md-option>
					</md-select>

					</md-field>
					<md-field>
						<label>Hipervisor</label>
						<md-input v-model="data.tab_hipervisor" required></md-input>
					</md-field>
					
		
					<md-field>
						<label>Maquina Virtual</label>
						<md-input v-model="data.tab_vm" required></md-input>
					</md-field>
					
					<md-field>
						<label>Nodo</label>
						<md-input v-model="data.tab_node" required></md-input>
					</md-field>
        </md-dialog-content>

        <md-dialog-actions>
			
            <md-button class="md-accent md-raised" @click="$emit('close')">Cerrar</md-button>
            <md-button class="md-primary md-raised" @click="$emit('create',new_service())" >Crear</md-button>
        </md-dialog-actions>
    </md-dialog>

</md-content>







</template>

<script type="text/javascript">
export default {
    name: "Dialog",
    props: {
        mode: {
            type: String,
            required: true
        },
        active: {
            type: Boolean,
            required: true
        }
    },
    data() {
        return {
            data: {
                tab_service: null,
                tab_subservice: null,
                tab_solution: null,
                tab_gestor: null,
                tab_hipervisor: null,
                tab_vm: null,
                tab_node: null
            },
            check: null
        };
    },
    methods: {
        new_service: function() {
            if (this.mode === "tab_serv") {
                var send_data = {
                    service: this.data.tab_service,
                    subservice: this.data.tab_subservice,
                    solution: this.data.tab_solution,
                    gestor: this.data.tab_gestor,
                    vmachine: this.data.tab_vm,
                    node: this.data.tab_node,
                    hipervisor: this.data.tab_hipervisor
                };
            } else {
                console.log("otro");
            }
            return send_data;
        }
    },
    computed: {},
    created() {}
};
</script>
