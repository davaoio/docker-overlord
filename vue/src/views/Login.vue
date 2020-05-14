<template>
  <section class="hero is-light is-fullheight">
    <div class="hero-body">
      <div class="container">
        <h2 class="subtitle has-text-centered">
          Loading...
        </h2>
      </div>
    </div>
  </section>
</template>




<script>
import axios from "axios";

export default {
  name: "Login",
  methods: {
    loginSuccess(response) {
      this.$store.dispatch("jwtSet", response.token);
      this.$store.dispatch("userDetails", response.profile);
      this.$store.dispatch("admin", response.admin);
      this.$router.push("/");
    },
    oauthGitHub(code) {
      axios.post("/api/users/github",{value: code}).then(response => {
        //console.log(response.data); // eslint-disable-line no-console
        this.loginSuccess(response.data);
      });
    },
  },
  mounted() {
    if (this.$route.query.oauth) {
      this.oauthGitHub(this.$route.query.code);
    } else {
      axios.get("/api/users/oauth-urls").then(response => window.location.href = response.data.github);
    }
    
  },
};
</script>
