<template>
    <div>

<md-dialog v-if="mode == 'false'" :md-active.sync="active" :md-click-outside-to-close="false" @md-closed="verify">

        <md-tabs md-dynamic-height class="md-primary" >
            <md-tab md-label="Password" >
                <h3>{{message}}</h3>
                <md-field v-if="show">
                <label>Introduzca su password</label>
                <md-input v-model="password" type="password"></md-input>
            </md-field>


            </md-tab>
    </md-tabs>


        <md-dialog-actions>

            <md-button class="md-primary md-raised" @click="$emit('close')">Cerrar</md-button>
            <md-button v-if="show" class="md-primary md-raised" @click="save_pass(password)">Salvar</md-button>
        </md-dialog-actions>
    </md-dialog>


<md-dialog v-if="mode == 'breach'" :md-active.sync="active" :md-click-outside-to-close="false" @md-closed="delete_password">

        <md-tabs class="md-accent" md-dynamic-height>
            <md-tab md-label="Alerta">
                <h4>Hemos detectado que esta corriendo este software en una maquina no autorizada. Si considera que esto es un error,cambie sus credenciales de usuario.</h4>
                <h5 style="color:red">Al cerrar este dialogo sus credenciales seran eliminadas</h5>
            </md-tab>
        </md-tabs>


        <md-dialog-actions>
            <md-button class="md-accent md-raised" @click="$emit('close')">Proceder</md-button>

        </md-dialog-actions>
    </md-dialog>

<md-dialog  v-if="mode == 'create'" :md-active.sync="active" :md-click-outside-to-close="false" @md-closed="$emit('close')">
        <md-dialog-content>
        <md-tabs md-dynamic-height class="md-primary">
            <md-tab md-label="Crear">
                
                <md-field  md-clearable>
                    <label>Precio</label>
                    <md-input v-model="announce.price" type="number"></md-input>
                </md-field>

                
                <md-field md-clearable>

                    <label>Telefono</label>
                    <md-input v-model="announce.phone" required></md-input>
                </md-field>


                <md-field  md-clearable>
                    <select v-model="announce.category" placeholder="Categoria">
                        <option disabled value="">Categoria</option>
                        <option v-for="value in categories" v-bind:value="value">
                            {{ value }}
                        </option>
                    </select>

                </md-field>

                <md-field  md-clearable>
                    <label>Encabezado</label>
                    <md-input v-model="announce.title" required></md-input>
                </md-field>

                <md-field  md-clearable>
                    <label>Correo</label>
                    <md-input v-model="announce.email" required></md-input>
                </md-field>

                <md-field>
                    <label>Imagenes</label>
                    <md-input v-model="announce.img1" md-label="Imagen 1"></md-input>
                    <md-input v-model="announce.img2" md-label="Imagen 2"></md-input>
                    <md-input v-model="announce.img3" md-label="Imagen 3"></md-input>
                </md-field>

                
                <md-field md-clearable>

                    <label>Descripcion</label>
                    <md-textarea v-model="announce.text"></md-textarea>
                </md-field>

            </md-tab>
        </md-tabs>
        </md-dialog-content>

        <md-dialog-actions>
            <h3>{{alert}}</h3>
            <md-button class="md-accent md-raised" @click="$emit('close')">Cerrar</md-button>
            <md-button class="md-primary md-raised" @click="create_offline(announce)">Crear</md-button>

        </md-dialog-actions>
    </md-dialog>





</div>



</template>

<script type="text/javascript">
    export default {
        name:'Dialog',
        props:{
            mode:{
                type:String,
                required:true
            },
            active:{
                type:Boolean,
                required:true
            }
        },
        data() {
            return {
                    password:'',
                    alert:null,
                    show:true,
                    message:'Es la primera vez que abres este software, es necesario que introduzcas tu password para verificar que eres tu. Solo ocurrira una vez...',
                    categories: [],
                    announce:{
                        'title':null,
                        'text':null,
                        'price':null,
                        'email':null,
                        'phone':null,
                        'date':null,
                        'reposted':0,
                        'img1':'',
                        'img2':'',
                        'img3':'',
                        'category':null,
                    },

            }
        },
        methods:{
            save_pass: function(password){
                eel.save_password(password)(message => this.message = message);
                this.show=false;
                this.password='';
            },
            delete_password: function (){
                eel.delete_password()();
                this.$emit('disable');
                this.$emit('close')

            },
            create_offline: function (data){
                this.alert = null;

                if (data.title === null || data.price ===null || data.category === null ){
                    console.log(data.title);
                    this.alert = 'No puede dejar esos campos en blanco';
                    
                }
                else{
                    console.log(data)
        eel.create_announce(data)(response => console.log(response));
                this.announce = {
                        'title':null,
                        'text':null,
                        'price':null,
                        'email':null,
                        'phone':null,
                        'date':null,
                        'reposted':null,
                        'email':null,
                        'img1':'',
                        'img2':'',
                        'img3':'',
                        'category':null,
                    };
                }

            },
            verify: function(){
                if (this.show == true){
                    this.$emit('disable');
                    this.$emit('close')
                }
                else {
                    this.$emit('close')
                }
            }

        },
        computed:{
            load_categories: function() {
                eel.load_categories()(result => this.categories = result);
            }
        },
        created(){
            this.load_categories;
        }

    }

</script>
