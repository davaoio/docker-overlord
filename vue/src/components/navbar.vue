<template>
    <nav class="navbar is-link" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
          <div class="navbar-item">
            <h2 class="has-text-warning"><strong>Docker Deploy</strong></h2>
          </div>
          <a class="navbar-item" v-if="admin" @click="$router.push('/')">Main</a>
          <a class="navbar-item" v-if="admin" @click="$router.push('admin')">Admin</a>
      </div>

      <div class="navbar-end" v-if="userDetails">
        <div class="navbar-item">
          <p v-if="userDetails.name">Welcome, {{userDetails.name}} (@{{userDetails.login}})</p>
          <p v-if="!userDetails.name">Logged in as: @{{userDetails.login}}</p>
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
      "userDetails", "admin"
    ])
  },
};
</script>
