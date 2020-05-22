<template>
  <div>
    <section class="hero is-light is-fullheight" v-if="repositories && repositories.length == 0">
      <div class="hero-body">
        <div class="container">
          <h2 class="subtitle has-text-centered">
            You don't have access to any repositories. Please contact the admin.
          </h2>
        </div>
      </div>
    </section>
    <section class="hero is-light is-fullheight" v-if="!repositories">
      <div class="hero-body">
        <div class="container">
          <h2 class="subtitle has-text-centered">
            Loading...
          </h2>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="field" v-if="repositories && repositories.length > 0">
        <div class="control">
          <div class="select is-medium">
            <select v-model="selectedRepo" @change="selectRepo">
              <option disabled value="">Select Repository</option>
              <option v-for="repo in repositories" :key="repo.registryId">{{repo.repositoryName}}</option>
            </select>
          </div>
        </div>
      </div>
      <div class="columns" v-if="images">
        <hr />
        <div class="column">
          <div class="notification is-warning is-light" v-if="currentStatus">
            <strong>Current Image:</strong> {{currentStatus.image_tag}}<br /><small>{{moment.utc(currentStatus.released).fromNow()}}</small>
          </div>
          <div class="box" v-for="image in imagesDesc" :key="image.imageDigest">
            <p><strong>{{image.imageTags}}</strong> {{moment.utc(image.imagePushedAt).fromNow()}} <button class="button is-small is-link is-light" v-if="!currentStatus || image.imageTags[0] != currentStatus.image_tag" @click="setRelease(image.imageTags[0])">Release</button></p>
          </div>
        </div>
        <div class="column">
          <div class="field">
            <label class="label">Container Configuration</label>
            <div class="control">
              <textarea class="textarea" v-model="newConfig" rows="10" placeholder="YAML style configuration"></textarea>
            </div>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-link" @click="saveConfig">Save</button>
            </div>
          </div>
          <hr />
          <p class="has-text-grey-light">{{currentStatus}}</p>
        </div>
      </div>

    </section>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  name: "home",
  computed: {
    ...mapGetters([
      "loggedIn", "userDetails", "admin"
    ]),
    imagesDesc() {
      let arr = this.images;
      return arr.sort(function(a, b) {
        var keyA = new Date(a.imagePushedAt),
          keyB = new Date(b.imagePushedAt);
        // Compare the 2 dates
        if (keyA > keyB) return -1;
        if (keyA < keyB) return 1;
        return 0;
      });
    }
  },
  data() {
    return {
      repositories: false,
      selectedRepo: "",
      images: false,
      currentStatus: false,
      newConfig: null,
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
      axios.get("/api/deploy/status", {params: {repository: this.selectedRepo}}).then(response => {
        this.currentStatus = response.data.deployed;
        if (response.data.deployed) {
          this.newConfig = response.data.deployed.config;
        }
      });
    },
    saveConfig() {
      axios.post("/api/deploy/set-config", {repo: this.selectedRepo, config: this.newConfig}).then(() => this.getStatus());
    },
  },
  mounted() {
    //console.log("LoggedIn: " + this.loggedIn); // eslint-disable-line no-console
    axios.get("/api/aws/ecr").then(response => {
      if (response.data) {
        this.repositories = response.data;
      } else {
        this.repositories = [];
      }
    });
  },
};
</script>
