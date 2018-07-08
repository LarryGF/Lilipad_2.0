<template>
    <md-content>
       <md-field>
					<label>Nombre del Servicio</label>
					<md-input v-model="step5_srvname" required></md-input>
				</md-field>

				<md-field>
					<label>Usuario de la base de datos</label>
					<md-input v-model="step5_usr" required></md-input>
				</md-field>

				<md-field>
					<label>Password de la base de datos</label>
					<md-input v-model="step5_pass" required></md-input>
				</md-field>
				<md-field>
					<label>Hostname (IP) de la base de datos</label>
					<md-input v-model="step5_ip" required></md-input>
				</md-field>

				<md-field>
						<label>Fecha inicial</label>
						<md-input v-model="step5_start" required></md-input>
					</md-field>

				<md-field>
						<label>Fecha final</label>
						<md-input v-model="step5_end" required></md-input>
					</md-field>

				<md-button class="md-primary md-raised"  >Enviar</md-button>
  
    </md-content>
</template>

<script>
import Dialog from "./Dialog.vue";
export default {
    name: "Step4",
    data: () => ({
        dialog_active: false,
        dialog: {
            name: ""
        },
        result: null
    }),
    components: {
        Dialog
    },
    methods: {
        tool: function(data) {
            eel.tools(data)(result => (this.result = result));
        }
    }
};
</script>
