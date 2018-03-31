<template>
<b-container class="bv-example-row">
    <b-navbar toggleable="md" type="light" variant="light">

  <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

  <b-navbar-brand href="#">NavBar</b-navbar-brand>

  <b-collapse is-nav id="nav_collapse">

    <b-navbar-nav>
      <b-nav-item href="#">Link</b-nav-item>
      <b-nav-item href="#" disabled>Disabled</b-nav-item>
    </b-navbar-nav>

    <!-- Right aligned nav items -->
    <b-navbar-nav class="ml-auto">

      <b-nav-form>
        <b-form-input size="sm" class="mr-sm-2" type="text" placeholder="Search"/>
        <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
      </b-nav-form>

      <b-nav-item-dropdown text="Lang" right>
        <b-dropdown-item href="#">EN</b-dropdown-item>
        <b-dropdown-item href="#">ES</b-dropdown-item>
        <b-dropdown-item href="#">RU</b-dropdown-item>
        <b-dropdown-item href="#">FA</b-dropdown-item>
      </b-nav-item-dropdown>

      <b-nav-item-dropdown right>
        <!-- Using button-content slot -->
        <template slot="button-content">
          <em>User</em>
        </template>
        <b-dropdown-item href="#">Profile</b-dropdown-item>
        <b-dropdown-item href="#">Signout</b-dropdown-item>
      </b-nav-item-dropdown>
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

                <b-form inline>
                  <label class="sr-only" for="inlineFormInputName2">Name</label>
                  <b-input class="mb-2 mr-sm-2 mb-sm-0" id="inlineFormInputName1" placeholder="Jane Doe" />

                  <label class="sr-only" for="inlineFormInputName2">Name</label>
                  <b-input class="mb-2 mr-sm-2 mb-sm-0" id="inlineFormInputName2" placeholder="Jane Doe" />

                  <label class="sr-only" for="inlineFormInputName2">Name</label>
                  <b-input class="mb-2 mr-sm-2 mb-sm-0" id="inlineFormInputName3" placeholder="Jane Doe" />

                  <label class="sr-only" for="inlineFormInputName2">Name</label>
                  <b-input class="mb-2 mr-sm-2 mb-sm-0" id="inlineFormInputName4" placeholder="Jane Doe" />
                </b-form>
                
                </b-col>
              </b-row>
          </b-container>

            <div>
              <b-form-textarea id="textarea1"
                              v-model="text"
                              placeholder="Enter something"
                              :rows="25"
                              :max-rows="25">
              </b-form-textarea>
            </div>
          </form>
        </b-col>
        
        <b-col sm="3">
          <b-form-textarea id="textarea3" plaintext 
          :value="text" :rows="25"></b-form-textarea>
        </b-col>
    </b-row>
</b-container> 
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
   data () {
    return {
      text: 'This is some text.\nIt is read only and doesn\'t look like an input.'
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
  margin-left: 5px;
}

.col-sm-3 {
  margin-left: -10px;
  height:100%;
}

.bg-light {
  margin-right: -15px;
  margin-left: -15px;
  height: 45px;
  background-color:#f7b731 !important;
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
  margin-bottom: 30px;
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
}



</style>
