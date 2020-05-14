<template>
    <nav class="navbar is-link" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
          <h1 class="title has-text-light">Docker Deploy</h1>
      </div>

      <div class="navbar-end" v-if="loggedIn">
        <div class="navbar-item">
          <p>Welcome, {{userDetails.name}} (@{{userDetails.login}})</p>
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