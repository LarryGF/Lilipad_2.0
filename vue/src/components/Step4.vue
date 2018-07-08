<template>
    <md-content>
        {{result}}
        <h3>Escoja cual de las pruebas desea realizar:</h3>
        <md-button class="md-primary md-raised" @click="dialog_active=true,dialog.name='correo'">Correo</md-button>
		<md-button class="md-primary md-raised" @click="dialog_active=true,dialog.name='navegacion'">Navegacion</md-button>
        <Dialog :mode="dialog.name" :active="dialog_active" @close="dialog_active=false" @create="tool($event)" />
  
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
