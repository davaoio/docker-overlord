<template>
  <div id="app">
    <NavBar />
    <router-view />
  </div>
</template>

<script>
import NavBar from "@/components/navbar";

export default {
  name: "appMain",
  components: {
    NavBar,
  },
  mounted() {
    // This should be handled elsewhere?
    if (window.location.pathname == '/oauth/github') {
      window.location.href = `/#/login?oauth=github&code=${window.location.search.substring(6)}`;
    }
    if (localStorage.jwt) {  
      // Need to set the JWT token to state here
      //console.log(`[App.js] found jwt: ${localStorage.jwt}`); // eslint-disable-line no-console
      this.$store.dispatch("jwtSet", localStorage.jwt);
    } else {
      console.log(`[App.js] didn't find JWT, checking if logged in`); // eslint-disable-line no-console
      if (!this.loggedIn ) this.$router.push("/login");
    }
  }
};
</script>
