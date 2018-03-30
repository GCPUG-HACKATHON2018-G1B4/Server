<template>

  
<b-container class="bv-example-row" style="">
    <b-row>
        <b-col sm="8" style="background-color:red">
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
        
        <b-col sm="4" style="background-color:blue">
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
</style>
