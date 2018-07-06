<template>
<md-content>
   <Table v-for="table in tables" :key="table.name" :columns="table.columns" :data="table.table" :table="table"  @new="dialog_active=true, dialog.name = $event"/>
   <Dialog :mode="dialog.name" :active="dialog_active" @close="dialog_active=false" @create="create_service($event)"/>
   
</md-content>
</template>

<script>
import Table from "./Table.vue";
import Dialog from "./Dialog.vue";
export default {
    name: "Step2",
    data: () => ({
        dialog_active: false,
        dialog: {
            name: ""
        },
        tables: {
            tab_serv: {
                name: "tab_serv",
                title: "Servicios",
                table: [],
                columns: [
                    { label: "Servicio", sort: "service" },
                    { label: "Subservicio", sort: "subservice" },
                    { label: "Solucion", sort: "solution" },
                    { label: "Gestor", sort: "gestor" },
                    { label: "Máquina Virtual", sort: "vmachine" },
                    { label: "Nodo", sort: "node" },
                    { label: "Hipervisor", sort: "hipervisor" }
                ]
            },
            existentes: {
                name: "existentes",
                title: "Servicios Existentes",
                table: [],
                columns: [
                    { label: "Nombre", sort: "name" },
                    { label: "Tipo", sort: "type" },
                    { label: "Clasificación", sort: "class" },
                    { label: "Estructura", sort: "structure" },
                    { label: "Criticidad", sort: "criticity" },
                    { label: "Comentarios", sort: "comments" }
                ]
            },
            nuevos: {
                name: "nuevos",
                title: "Servicios Nuevos",
                table: [],
                columns: [
                    { label: "Nombre", sort: "name" },
                    { label: "Tipo", sort: "type" },
                    { label: "Clasificación", sort: "class" },
                    { label: "Estructura", sort: "structure" },
                    { label: "Criticidad", sort: "criticity" },
                    { label: "Comentarios", sort: "comments" }
                ]
            },
            futuros: {
                name: "futuros",
                title: "Servicios Futuros",
                table: [],
                columns: [
                    { label: "Nombre", sort: "name" },
                    { label: "Tipo", sort: "type" },
                    { label: "Clasificación", sort: "class" },
                    { label: "Estructura", sort: "structure" },
                    { label: "Criticidad", sort: "criticity" },
                    { label: "Comentarios", sort: "comments" }
                ]
            }
        }
    }),
    computed: {
        load: function() {
            eel.load(["tab_serv", "existentes", "nuevos", "futuros"])(
                result => {
                    this.tables.tab_serv.table = result[0];
                    this.tables.existentes.table = result[1];
                    this.tables.nuevos.table = result[2];
                    this.tables.futuros.table = result[3];
                }
            );
        }
    },
    methods: {
        create_service: function(data) {
            this.tables[this.dialog.name].table.push(data);
        }
    },
    created() {
        this.load;
    },
    components: {
        Table,
        Dialog
    }
};
</script>
