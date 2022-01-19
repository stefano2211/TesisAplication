<template>
  <div id="app-wrapper">
    <div class="app">
     <Navbar/>
    </div>
  </div>
  <router-view/>
</template>

<script>
import Navbar from './components/Navbar.vue'

export default {
	name: 'app',
	component: {
		Navbar
	}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
