<template>
<b-container class="bv-example-row" style="">
    <b-navbar toggleable="md" type="dark" variant="info">

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
          <b-container fluid>
              <b-row class="my-1">
                <b-col sm="12">
                <b-form-input id="input-large" size="lg" type="text" placeholder="Enter your name"></b-form-input>
                </b-col>
              </b-row>
          </b-container>

            <div>
              <b-form-textarea id="textarea1"
                              v-model="text"
                              placeholder="Enter something"
                              :rows="27"
                              :max-rows="27">
              </b-form-textarea>
            
            </div>
        </b-col>
        
        <b-col sm="3">
          <b-form-textarea id="textarea3" plaintext 
          :value="text" :rows="20"></b-form-textarea>
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

.bg-info {
  margin-right: -15px;
  margin-left: -15px;
}

.form-control:focus {
  box-shadow:none;
  border-color:none;
}

.row {
  background-color:#d1d8e0;
}

</style>
