<template>
  <div class="container">
    <a class="button" v-if="oauthUrls" :href="oauthUrls.github">Login via GitHub</a>
  </div>
</template>




<script>
import axios from "axios";

export default {
  name: "navbar",
  data() {
    return {
      oauthUrls: false,
    }
  },
  methods: {
    loginSuccess(response) {
      this.$store.dispatch("jwtSet", response.token);
      this.$store.dispatch("userDetails", response.profile);
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
    }
    axios.get("/api/users/oauth-urls").then(response => this.oauthUrls = response.data)
  },
};
</script>
<style scoped>
.g-signin-button {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 3px;
  background-color: #3c82f7;
  color: #fff;
  box-shadow: 0 3px 0 #0f69ff;
}
</style>