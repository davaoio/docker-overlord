<template>
  <section class="section">
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
      <div class="notification is-warning is-light" v-if="currentStatus">
        <strong>Current Image:</strong> {{currentStatus.image_tag}} ({{moment.utc(currentStatus.released).fromNow()}})
      </div>
      <div class="box" v-for="image in images" :key="image.imageDigest">
        <p><strong>{{image.imageTags}}</strong> {{image.imagePushedAt}} <button class="button is-small is-link is-light" v-if="!currentStatus || image.imageTags[0] != currentStatus.image_tag" @click="setRelease(image.imageTags[0])">Release</button></p>
      </div>
    </section>
  </section>
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
      //console.log(this.selectedRepo); // eslint-disable-line no-console
      axios.get("/api/aws/ecr/get-images", {params: {repository: this.selectedRepo}}).then(response => this.images = response.data);
      this.getStatus();
    },
    setRelease(image) {
      axios.post("/api/deploy/release", {repository: this.selectedRepo, image}).then(() => this.getStatus());
    },
    getStatus() {
      axios.get("/api/deploy/status", {params: {repository: this.selectedRepo}}).then(response => this.currentStatus = response.data);
    },
  },
  mounted() {
    //console.log("LoggedIn: " + this.loggedIn); // eslint-disable-line no-console
    if (!this.loggedIn) this.$router.push("/login");
    axios.get("/api/aws/ecr").then(response => this.repositories = response.data);
  },
};
</script>
