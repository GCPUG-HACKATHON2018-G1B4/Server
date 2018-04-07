<template>
<b-container class="bv-example-row">
    <b-navbar toggleable="md" type="light" variant="light">

  <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

  <b-navbar-brand href="#">코카인</b-navbar-brand>

  <b-collapse is-nav id="nav_collapse">

    <!-- Right aligned nav items -->
    <b-navbar-nav class="ml-auto">

    <i class="far fa-smile"></i>
    </b-navbar-nav>

  </b-collapse>
</b-navbar>

<!-- navbar-1.vue -->

    <b-row>
        <b-col sm="9">
          <form>
          <b-container fluid>
              <b-row class="my-1">
                <b-col sm="12">

                <b-nav id="nav3">
                  <b-nav-item>Keyword</b-nav-item>
                </b-nav>

                <b-form inline>
                  <label class="sr-only" for="inlineFormInputName2">Name</label>
                  <input class="mb-2 mr-sm-2 mb-sm-0" id="inlineFormInputName1" placeholder="Name" name="hash" v-model="hash.tag1" size="lg" type="text" v-on:keyup.enter="passHash1"/>

                  <label class="sr-only" for="inlineFormInputName2">Name</label>
                  <input class="mb-2 mr-sm-2 mb-sm-0" id="inlineFormInputName2" placeholder="Framework" name="hash" v-model="hash.tag2" size="lg" type="text" v-on:keyup.enter="passHash2"/>

                  <label class="sr-only" for="inlineFormInputName2">Name</label>
                  <input class="mb-2 mr-sm-2 mb-sm-0" id="inlineFormInputName3" placeholder="Feature1" name="hash" v-model="hash.tag3" size="lg" type="text" v-on:keyup.enter="passHash3"/>

                  <label class="sr-only" for="inlineFormInputName2">Name</label>
                  <input class="mb-2 mr-sm-2 mb-sm-0" id="inlineFormInputName4" placeholder="Feature2" name="hash" v-model="hash.tag4" size="lg" type="text" v-on:keyup.enter="getHash"/>
                </b-form>
                
                </b-col>
              </b-row>
          </b-container>

            <div>
              <b-nav id="nav2">
                <b-nav-item>Code_Editor</b-nav-item>
              </b-nav>

              <b-form-textarea id="textarea1"
                              v-model="text"
                              placeholder="Enter Your Code"
                              :rows="23"
                              :max-rows="23">
              </b-form-textarea>

              <b-nav id="nav4">
                <b-nav-item>line 1, Column 12</b-nav-item>
              </b-nav>
            </div>
          </form>
        </b-col>
        

        <b-col sm="3">
          <b-nav id="nav1">
            <b-nav-item>Code-Guide</b-nav-item>
          </b-nav>

          <div class="box-container">
            <div class="box" v-for="data in datalist">
                <b-card title> {{data.title}} 
                
                <p class="card-text mt-2"> 
                  {{data.body}}
                </p>
                
                </b-card>              
            </div>
          </div>
        </b-col>
    </b-row>
</b-container> 
</template>
<script defer src="https://use.fontawesome.com/releases/v5.0.9/js/all.js" integrity="sha384-8iPTk2s/jMVj81dnzb/iFR2sdA7u06vHJyyLlAd4snFpCl/SnyUjRrbdJsw1pGIl" crossorigin="anonymous"></script>
<script>

export default {
  data:   function data() {    
    return   {
          hash: [
            {tag1: ''},
            {tag2: ''},
            {tag3: ''},
            {tag4: ''}
          ],
          datalist: [],
          text:''
        } 
    },
    methods: {
    

    getHash () {
    
     console.log(this.hash.tag1, this.hash.tag2, this.hash.tag3, this.hash.tag4);
     
     this.$http.get(`http://35.189.132.166:5000/setting?tag=java&tag=android&tag=camera&tag=save`) 
    //  this.$http.get(`http://35.189.132.166:5000/setting?tag= #{this.hash.tag1} &tag= #{this.hash.tag2} &tag= #{this.hash.tag3} &tag= #{this.hash.tag4} `) 
     //  this.$http.get('http://35.189.132.166:5000/setting?tag='+this.hash.tag1+'&tag='+this.hash.tag2+'&tag='+this.hash.tag3+'&tag='+this.hash.tag4 )
     .then(function(response) {
       console.log(response)
        return response.json();        
     })
     .then(data => {
       this.datalist = Object.values(data);
       console.log( Object.values(data))
     })
     
     .catch(function(error){
      console.log(error)
     })

        

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
  max-width:100%;
}
.col-sm-12 {
  padding: 0;
}

.col-sm-9 {
  margin-left: 0px;
  padding-left: 0px;
  margin-top:1px;
}

.col-sm-3 {
  margin-right: -8px;
  height:100%;
  padding-right: 0px;
}

.bg-light {
  margin-right: -15px;
  margin-left: -15px;
  height: 45px;
  background-color:#2364AA !important;
}

.navbar-brand {
  margin-left: 45%;
  color: #FEC601;
  font-weight:600;
}

.navbar-brand:active,
.navbar-brand:hover {
  color:#fbc531;
}

.nav {
  background-color: #3DA5D9;
  line-height: 0.5rem;
  margin-bottom: -8px;
  margin-top: 10px;

}

.form-control {
  border-radius: 0px;
}

.form-control:focus {
  box-shadow:none;
  border-color:none;
}

.row {
  background-color:white;
  flex-wrap: nowrap;
}

#textarea1 {
  margin-top: 8px;
  margin-bottom: 15px;
  border-radius: 0px;
  height: 526px;
  width: 1014px;
  margin-left: 8px;
  padding-right: 0px;
}

.box-container {
  background-color: #d2dae2;
  height: 600px;
}

.form-control-lg {
  margin-top: 6px;
}

#input-large {
  margin-top: 4px;
  width: 100%;
  display: block;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  line-height:1.5;
  color:#495057;
  background-clip:padding-box;
  border: 1px solid #cde4da;
  border-radius: 0.25rem;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

#input-large:focus {
  border-color: none;
}

#inlineFormInputName1,
#inlineFormInputName2,
#inlineFormInputName3,
#inlineFormInputName4 {
  width: 23.5%;
  margin-left: 7px;
}

a {
  color: white;
}

#nav1 {
  margin-bottom: 0px;
  margin-top: 0px;
  background-color:#EA7317;
  font-weight: 500;
}

#nav2 {
  background-color: #73BFB8;
  font-weight: 500;
}


#nav3 {
  margin-bottom: -8px;
  margin-top: -5px !important;
  font-weight: 500;
}

#nav4 {
  margin-top: -15px;
  width: 1014px;
  font-weight: 200;
  font-size: 0.8rem;
  background-color: #2c3e50;
  margin-left: 8px;
}

.form-inline {
  margin-top: 12px;
}



.card {
  border-radius: 0px;
  height: 100%;
}

.card-body {
  padding: 0.5rem;
}

p {
  font-size: 0.8rem;
}

h4 {
  font-size: 1.2rem;
}

.box {
    width: 20em; height: 20%;
    border: solid 1px #ccc;
    position: relative;
    background: white;
}
.box:before, .box:after {
    min-height: 45%; width: 65%;
    border-radius: .2em;
    box-shadow: 0 0 .625em rgba(204,204,204,.4);
    position: absolute;
    z-index: -1;
    background: rgba(204,204,204,.4);
    content: '';
}
.box:before {
    bottom: 0; left: .3em;
    transform: rotate(-5deg);
}
.box:after {
    right: .3em; bottom: 0; 
    transform: rotate(5deg);
}

</style>


