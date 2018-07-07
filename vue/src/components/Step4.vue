<template>
    <md-content>
        {{dialog_active}}{{dialog.name}}
        <h3>Escoja cual de las pruebas desea realizar:</h3>
        <md-button class="md-primary md-raised" @click="dialog_active=true,dialog.name='correo'">Correo</md-button>
		<md-button class="md-primary md-raised" @click="dialog_active=true,dialog.name='navegacion'">Navegacion</md-button>
        <Dialog :mode="dialog.name" :active="dialog_active" @close="dialog_active=false"  />
  
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
        }
    })
};
</script>
