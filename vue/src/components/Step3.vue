<template>
<md-content>
    
   <Table v-for="table in tables" :key="table.name" :columns="table.columns" :data="table.table" :table="table"  @new="dialog_active=true, dialog.name = $event" @save="save($event)" @delete="del_item($event)"/>
   <Dialog :mode="dialog.name" :active="dialog_active" @close="dialog_active=false" @create="create_service($event)" />
   
</md-content>
</template>

<script>
import Table from "./Table.vue";
import Dialog from "./Dialog.vue";
export default {
    name: "Step3",
    data: () => ({
        dialog_active: false,
        dialog: {
            name: ""
        },
        tables: {
            iaas: {
                name: "iaas",
                title: "Recursos asignados a IaaS",
                table: [],
                columns: [
                    { label: "Subentidad", sort: "subentity" },
                    { label: "CPU [%]", sort: "cpu" },
                    { label: "RAM [MB]", sort: "ram" },
                    { label: "Almacenamiento [GB]", sort: "cap_alm" },
                    { label: "Throughput [Mbps]", sort: "thru_alm" },
                    { label: "TX [Mbps]", sort: "trans_net" },
                    { label: "RX [Mbps]", sort: "rec_net" },
                    { label: "Nucleos [%]", sort: "core_gpu" },
                    { label: "Memoria [%]", sort: "mem_gpu" }
                ]
            },
            dsaas: {
                name: "dsaas",
                title: "Recursos asignados a DSaaS",
                table: [],
                columns: [
                    { label: "Subentidad", sort: "subentity" },
                    { label: "Almacenamiento", sort: "storage" },
                    { label: "Salvas", sort: "saves" }
                ]
            }
        }
    }),
    computed: {
        load: function() {
            eel.load(["iaas", "dsaas"])(result => {
                console.log(result);
                this.tables.iaas.table = result[0];
                this.tables.dsaas.table = result[1];
            });
        }
    },
    methods: {
        create_service: function(data) {
            this.tables[this.dialog.name].table.push(data);
        },
        save: function(table) {
            eel.save(table, this.tables[table].table)();
        },
        del_item: function(table) {
            eel.delete(this.tables[table.name].table, table.selection)(
                result => (this.tables[table.name].table = result)
            );
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

