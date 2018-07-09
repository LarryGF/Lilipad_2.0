<template>
    <md-content>
		
       <md-field>
					<label>Nombre del Servicio</label>
					<md-input v-model="data.service" required></md-input>
				</md-field>

				<md-field>
					<label>Usuario de la base de datos</label>
					<md-input v-model="data.user" required></md-input>
				</md-field>

				<md-field>
					<label>Password de la base de datos</label>
					<md-input v-model="data.password" required></md-input>
				</md-field>
				<md-field>
					<label>Hostname (IP) de la base de datos</label>
					<md-input v-model="data.ip" required></md-input>
				</md-field>

				<md-field>
						<label>Fecha inicial</label>
						<md-input v-model="data.date_start" required></md-input>
					</md-field>

				<md-field>
						<label>Fecha final</label>
						<md-input v-model="data.date_end" required></md-input>
					</md-field>

				<md-button class="md-primary md-raised" @click="tool" >Enviar</md-button>
  
    </md-content>
</template>

<script>
import Dialog from "./Dialog.vue";
export default {
    name: "Step4",
    data: () => ({
        data: {
            service: null,
            user: null,
            password: null,
            ip: null,
            date_start: null,
            date_end: null
        }
    }),
    components: {
        Dialog
    },
    methods: {
        tool: function(data) {
            eel.usage(this.data)(result => (this.result = result));
        }
    }
};
</script>
