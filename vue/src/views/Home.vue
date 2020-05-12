<template>
  <div class="container">
    <h1 class="subtitle">Repositories</h1>
    <p>Hello {{userDetails.name}} (Logged in as: @{{userDetails.login}})</p>
    <p>{{repositories}}</p>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  name: "home",
  computed: {
    ...mapGetters([
      "loggedIn", "userDetails"
    ])
  },
  data() {
    return {
      repositories: false,
    };
  },
  components: {
  },
  methods: {
  },
  mounted() {
    //console.log("LoggedIn: " + this.loggedIn); // eslint-disable-line no-console
    if (!this.loggedIn) this.$router.push("/login");
    axios.get("/api/aws/ecr").then(response => this.repositories = response.data);
  },
};
</script>
