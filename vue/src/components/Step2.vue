<template>
<md-content>
   <Table v-for="table in tables" :key="table.name" :columns="table.columns" :data="table.table" :table="table"/>
   
</md-content>
</template>

<script>
import Table from "./Table.vue";
export default {
    name: "Step2",
    data: () => ({
        active: "step1",
        alert: "background-color:black;color:white",
        showSnackBar: false,
        message: "",
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
                    { label: "Criticidad", sort: "int" },
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
                    { label: "Criticidad", sort: "int" },
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
                    { label: "Criticidad", sort: "int" },
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
    methods: {},
    created() {
        this.load();
    },
    components: {
        Table
    }
};
</script>
