<template>
  <div class="container">
    <div class="field">
      <div class="control">
        <div class="select is-medium">
          <select v-model="selectedRepo" @change="selectRepo">
            <option disabled value="">Select Repository</option>
            <option v-for="repo in repositories" :key="repo.registryId">{{repo.repositoryName}}</option>
          </select>
        </div>
      </div>
    </div>
    <section v-if="images">
      <hr />
      <p class="subtitle">{{currentStatus}}</p>
      <div class="box" v-for="image in images" :key="image.imageDigest">
        <p><strong>{{image.imageTags}}</strong> {{image.imagePushedAt}} <button class="button is-link is-light" @click="setRelease(image.imageTags[0])">Release</button></p>
      </div>
    </section>
    <hr />
    <p class="has-text-grey-light">{{repositories}}</p>
    <p class="has-text-grey-light">{{images}}</p>
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
      selectedRepo: "",
      images: false,
      currentStatus: false,
    };
  },
  components: {
  },
  methods: {
    selectRepo() {
      console.log(this.selectedRepo); // eslint-disable-line no-console
      axios.get("/api/aws/ecr/get-images", {params: {repository: this.selectedRepo}}).then(response => this.images = response.data);
      this.getStatus();
    },
    setRelease(image) {
      console.log(this.selectedRepo); // eslint-disable-line no-console
      console.log(image); // eslint-disable-line no-console
      axios.post("/api/deploy/release", {repository: this.selectedRepo, image}).then(() => this.getStatus());
    },
    getStatus() {
      axios.get("/api/deploy/status", {params: {repository: this.selectedRepo}}).then(response => {
        console.log(response.data); // eslint-disable-line no-console

        this.currentStatus = response.data;

      });
    },
  },
  mounted() {
    //console.log("LoggedIn: " + this.loggedIn); // eslint-disable-line no-console
    if (!this.loggedIn) this.$router.push("/login");
    axios.get("/api/aws/ecr").then(response => this.repositories = response.data);
  },
};
</script>
