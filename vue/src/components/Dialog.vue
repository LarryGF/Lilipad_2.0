<template>

<div>

<md-dialog  v-if="mode == 'tab_serv'" :md-active.sync="active" :md-click-outside-to-close="false">
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

    <md-dialog  v-if="mode == 'existentes' || mode == 'nuevos' || mode == 'futuros'" :md-active.sync="active" :md-click-outside-to-close="false">
        <md-dialog-title>Agregar servicios {{mode}}</md-dialog-title>
        <md-dialog-content>
					<md-field>
						<label>Nombre</label>
						<md-input v-model="data_mix.name" required></md-input>
					</md-field>
				
					<md-field>
						<label>Tipo</label>
						<md-input v-model="data_mix.type" required></md-input>
					</md-field>
					
					<md-field>
						<label>Clasificacion</label>
						<md-input v-model="data_mix.class" required></md-input>
					</md-field>

					<md-field>
						<label>Estructura</label>
						<md-input v-model="data_mix.structure" required></md-input>
					</md-field>

					<md-field>
						<label>Criticidad</label>
						<md-input v-model="data_mix.criticity" required></md-input>
					</md-field>
				
					<md-field>
						<label>Comentarios</label>
						<md-input v-model="data_mix.comments" required></md-input>
					</md-field>
								
        </md-dialog-content>

        <md-dialog-actions>
			
            <md-button class="md-accent md-raised" @click="$emit('close')">Cerrar</md-button>
            <md-button class="md-primary md-raised" @click="$emit('create',new_service())" >Crear</md-button>
        </md-dialog-actions>
    </md-dialog>
    

</div>







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
            data_mix: {
                name: null,
                type: null,
                class: null,
                structure: null,
                criticity: null,
                comments: null
            }
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
                this.data = {
                    tab_service: null,
                    tab_subservice: null,
                    tab_solution: null,
                    tab_gestor: null,
                    tab_hipervisor: null,
                    tab_vm: null,
                    tab_node: null
                };
            } else if (
                this.mode == "existentes" ||
                this.mode == "nuevos" ||
                this.mode == "futuros"
            ) {
                var send_data = this.data_mix;
                this.data_mix = {
                    name: null,
                    type: null,
                    class: null,
                    structure: null,
                    criticity: null,
                    comments: null
                };
            }
            return send_data;
        }
    },
    computed: {},
    created() {}
};
</script>
