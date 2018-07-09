<template>
<md-content>
   <Table v-for="table in tables" :key="table.name" :columns="table.columns" :data="tab_serv_fut" :table="table"  @new="dialog_active=true, dialog.name = $event" @save="save($event)" @delete="del_item($event)"/>  
</md-content>
</template>

<script>
import Table from "./Table.vue";

export default {
    name: "Step7",
    data: () => ({
        tab_serv_fut: [],
        tables: {
            inminente: {
                name: "inminente",
                title: "Capacidad de recursos inminente",
                table: [],
                columns: [
                    { label: "Servicio", sort: "service" },
                    { label: "vCPU", sort: "cpu2" },
                    { label: "RAM [MB]", sort: "ram2" },
                    { label: "Almacenamiento [MB]", sort: "disk_usage2" },
                    { label: "Lectura en disco [B/s]", sort: "read2" },
                    { label: "Escritura en dsico [B/s]", sort: "write2" },
                    { label: "IOPS a soportar", sort: "iops2" },
                    { label: "Red (in) [MB/s]", sort: "in2" },
                    { label: "Red (out) [MB/s]", sort: "out2" }
                ]
            },
            futuro: {
                name: "futuro",
                title: "Capacidad de recursos futuros",
                table: [],
                columns: [
                    { label: "Servicio", sort: "service" },
                    { label: "vCPU", sort: "cpu" },
                    { label: "RAM [MB]", sort: "ram" },
                    { label: "Almacenamiento [MB]", sort: "disk_usage" },
                    { label: "Lectura en disco [B/s]", sort: "read" },
                    { label: "Escritura en dsico [B/s]", sort: "write" },
                    { label: "IOPS a soportar", sort: "iops" },
                    { label: "Red (in) [MB/s]", sort: "in" },
                    { label: "Red (out) [MB/s]", sort: "out" }
                ]
            }
        }
    }),
    computed: {
        load: function() {
            eel.load(["step_7"])(result => {
                this.tab_serv_fut = result[0];
            });
        }
    },
    methods: {},
    created() {
        this.load;
    },
    components: {
        Table
    }
};
</script>

