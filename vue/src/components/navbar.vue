<template>
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
          <h1 class="title">Docker Deploy</h1>
          <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" @click="showNav = !showNav" :class="{ 'is-active': showNav }">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu" :class="{ 'is-active': showNav }">
          <div class="navbar-start">
            <router-link to="/" class="navbar-item">Home</router-link>
            
          </div>

          <div class="navbar-end">
            <div class="navbar-item">
              <router-link to="/login/" class="navbar-item" v-if="!loggedIn">Login</router-link>
              <p v-if="loggedIn">Welcome, {{userDetails.name}} (@{{userDetails.login}})</p>
            </div>
          </div>
      </div>
    </nav>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Navbar",
  computed: {
    ...mapGetters([
      "loggedIn", "userDetails"
    ])
  },
  data() {
    return {
      showNav: false,
    }
  },
};
</script>

<style scoped>
</style>