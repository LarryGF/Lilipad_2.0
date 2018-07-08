<template>
   <md-content>
           
                <md-field>
                    <label>Usuarios actuales</label>
                    <md-input v-model="users.act" type="number"></md-input>
                </md-field>

                <md-field>
                    <label>Usuarios nuevos</label>
                    <md-input v-model="users.new" type="number"></md-input>
                </md-field>

                <md-field>
                    <label>Usuarios futuros</label>
                    <md-input v-model="users.fut" type="number"></md-input>
                </md-field>

                <md-button class="md-raised md-primary" @click="save('step_1',[{'usrfutr':users.fut,'usract':users.act,'usrnew':users.new}])">Guardar</md-button>
            
    </md-content>
</template> 

<script type="text/javascript">
export default {
    name: "Step1",
    props: {
        disabled: {
            type: Boolean,
            required: false
        }
    },
    data() {
        return {
            users: {
                act: null,
                new: null,
                fut: null
            }
        };
    },
    methods: {
        save: function(table, list) {
            eel.save(table, list)();
        },
        load: function(activeTab, list) {
            eel.load(["step_1"])(result => {
                this.users.act = result[0][0]["usract"];
                this.users.new = result[0][0]["usrnew"];
                this.users.fut = result[0][0]["usrfutr"];
            });
        }
    },
    created() {
        this.load();
    }
};
</script> 
