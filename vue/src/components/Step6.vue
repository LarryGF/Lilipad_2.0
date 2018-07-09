<template>
<md-content>
   <Table v-for="table in tables" :key="table.name" :columns="table.columns" :data="tab_ut_serv" :table="table" :hide="true" @new="dialog_active=true, dialog.name = $event" @save="save($event)" @delete="del_item($event)"/>  
</md-content>
</template>

<script>
import Table from "./Table.vue";

export default {
    name: "Step6",
    data: () => ({
        tab_ut_serv: [],
        tables: {
            util_serv: {
                name: "util_serv",
                title: "Utilizacion de Servicios",
                table: [],
                columns: [
                    { label: "Maquina Virtual", sort: "mv" },
                    { label: "Servicio", sort: "service" },
                    { label: "Subservicio", sort: "subservice" },
                    { label: "Asignado [vCPU]", sort: "cpu_asigned" },
                    { label: "UProm (CPU)", sort: "cpu_uprom" },
                    { label: "UMax (CPU)", sort: "cpu_umax" },
                    { label: "Asignado (RAM)", sort: "ram_asigned" },
                    { label: "UProm (RAM)", sort: "ram_uprom" },
                    { label: "UMax (RAM)", sort: "ram_umax" }
                ]
            },
            cap_alm: {
                name: "cap_alm",
                title: "Almacenamiento:Capacidad [MB]",
                table: [],
                columns: [
                    { label: "Maquina Virtual", sort: "mv" },
                    { label: "Servicio", sort: "service" },
                    { label: "Subservicio", sort: "subservice" },
                    { label: "Asignado ", sort: "asigned" },
                    { label: "Uso", sort: "use" }
                ]
            },
            thru_alm_iops: {
                name: "thru_alm_iops",
                title: "Almacenamiento:Throughput (IOPS)",
                table: [],
                columns: [
                    { label: "Maquina Virtual", sort: "mv" },
                    { label: "Servicio", sort: "service" },
                    { label: "Subservicio", sort: "subservice" },
                    { label: "Asignado ", sort: "thru_asigned" },
                    { label: "UProm", sort: "thru_uprom" },
                    { label: "UMax", sort: "thru_umax" }
                ]
            },
            thru_alm: {
                name: "thru_alm",
                title: "Throughput [B/s]",
                table: [],
                columns: [
                    { label: "Maquina Virtual", sort: "mv" },
                    { label: "Servicio", sort: "service" },
                    { label: "Subservicio", sort: "subservice" },
                    { label: "Lectura (UProm) ", sort: "uprom_r" },
                    { label: "Escritura (UProm)", sort: "uprom_w" },
                    { label: "Lectura (UMax)", sort: "umax_r" },
                    { label: "Escritura (UMax)", sort: "umax_w" }
                ]
            },
            gpu: {
                name: "gpu",
                title: "GPU",
                table: [],
                columns: [
                    { label: "Maquina Virtual", sort: "mv" },
                    { label: "Servicio", sort: "service" },
                    { label: "Subservicio", sort: "subservice" },
                    { label: "Asignados (Nucleos) ", sort: "gpu_core_asigned" },
                    { label: "UProm (Nucleos)", sort: "gpu_core_uprom" },
                    { label: "Umax (Nucleos)", sort: "gpu_core_umax" },
                    { label: "Asignado (VRAM)", sort: "gpu_ram_asigned" },
                    { label: "UProm (VRAM)", sort: "gpu_ram_uprom" },
                    { label: "UMax (VRAM)", sort: "gpu_ram_umax" }
                ]
            },
            net: {
                name: "net",
                title: "Red [MB/s]",
                table: [],
                columns: [
                    { label: "Maquina Virtual", sort: "mv" },
                    { label: "Servicio", sort: "service" },
                    { label: "Subservicio", sort: "subservice" },
                    { label: "Asignado (Tx) ", sort: "tx_asigned" },
                    { label: "UProm (Tx)", sort: "tx_uprom" },
                    { label: "Umax (Tx)", sort: "tx_umax" },
                    { label: "Asignado (Rx)", sort: "rx_asigned" },
                    { label: "UProm (Rx)", sort: "rx_uprom" },
                    { label: "UMax (Rx)", sort: "rx_umax" }
                ]
            }
        }
    }),
    computed: {
        load: function() {
            eel.load(["tab_ut_serv"])(result => {
                this.tab_ut_serv = result[0];
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

