<template>
  <section class="section">
    <div class="columns">
      <div class="column is-4">
        <nav class="panel">
          <p class="panel-heading">
            Users
          </p>
          <a class="panel-block" v-for="user in users" :key="user.id" :class="{'is-active': selectedUser == user.id}" @click="selectedUser = user.id">
            {{displayName(user.profile)}}
          </a>
        </nav>
      </div>
      <div class="column is-8">
        <div class="container" v-if="userProfile">
          <div class="media">
            <div class="media-left">
              <figure class="image is-48x48">
                <img :src="userProfile.avatar_url">
              </figure>
            </div>
            <div class="media-content">
              <p class="title is-4">{{userProfile.name}}</p>
              <p class="subtitle is-6">@{{userProfile.login}}</p>
            </div>
          </div>
          <hr />
          <h1 class="subtitle">Repositories</h1>
          <div v-for="respository in repositories" :key="respository.id">
            <label class="checkbox">
              <input type="checkbox" :value="respository.repositoryName" v-model="userRepos" @change="setRepos">
              {{respository.repositoryName}}
            </label>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>


<script>
import axios from "axios";
//import SomeComponent from "@/components/somecomponent";
import { mapGetters } from "vuex";

export default {
  name: "admin",
  computed: {
    ...mapGetters([
      "loggedIn", "admin"
    ])
  },
  data() {
    return {
      users: false,
      selectedUser: false,
      userProfile: false,
      repositories: false,
      userRepos: [],
    };
  },
  watch: {
    selectedUser() {
      this.userProfile = false;
      this.userRepos = [];
      //console.log('You selected: ' + this.selectedUser); // eslint-disable-line no-console
      this.userProfile = JSON.parse(this.getProfile(this.selectedUser).profile);
      this.getRepos(this.selectedUser);
    },
  },
  mounted() {
    if (!this.loggedIn) this.$router.push("/login");
    if (!this.admin) this.$router.push("/");
    this.getUsers();
    axios.get("/api/aws/ecr").then(response => this.repositories = response.data);
  },
  methods: {
    getUsers() {
      axios.get("/api/users/all").then(response => this.users = response.data);
    },
    getProfile(id) {
      return this.users.find(user => user.id == id);
    },
    displayName(profile) {
      const userProfile = JSON.parse(profile);
      if (userProfile.name) return userProfile.name;
      return `@${userProfile.login}`;
    },
    getRepos(id) {
      axios.get("/api/users/get-repos", {params: {id}}).then(response => {
        console.log(response.data); // eslint-disable-line no-console
        if (response.data.repos) {
          this.userRepos = JSON.parse(response.data.repos);
        } else {
          this.userRepos = [];
        }
      });
    },
    setRepos() {
      axios.post("/api/users/set-repos", {id: this.selectedUser, repos: this.userRepos});
    },
  },
};
</script>
