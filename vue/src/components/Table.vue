<template>
  <div>
    

<md-table @md-selected="onSelect" v-model="data" md-sort="name" md-sort-order="asc" md-card md-fixed-header>
    <md-table-toolbar>
        <h1 class="md-title">{{table.title}}</h1>
        <md-button class="md-raised md-accent" @click="del_item(table.name)">Borrar</md-button>
        <md-button class="md-raised md-primary" @click="save(table.name,data)">Guardar</md-button>

        <md-button class="md-raised md-primary" @click="change(table.name)">Nuevo</md-button>
    </md-table-toolbar>

    <md-table-row md-selectable="multiple" md-auto-select slot="md-table-row" slot-scope="{ item }">
        <md-table-cell v-for="column in columns" :key="column.label" :md-label="column.label" :md-sort-by="column.sort" md-numeric>{{ item[column.sort] }}</md-table-cell>
    
    </md-table-row>
    <md-table-empty-state
        md-label="No hay servicios"
        :md-description="`No hay servicios agregados a la tabla en estos momentos.`">
        <md-button class="md-primary md-raised" >Nuevo</md-button>
      </md-table-empty-state>
</md-table>

      

  </div>
</template> 

<script type="text/javascript">
export default {
    name: "Table",
    props: {
        table: {
            type: Object,
            required: true
        },
        data: {
            type: Array,
            required: false
        },
        columns: {
            type: Array,
            required: true
        }
    },
    data() {
        return {
            selected: []
        };
    },
    methods: {
        onSelect: function() {}
    }
};
</script> 
 
