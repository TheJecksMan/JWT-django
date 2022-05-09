<script>
export default {
  data() {
    return {
      data: {},
    };
  },
  beforeMount() {
    this.getPost();
  },
  methods: {
    async getPost() {
      let id = Object.values(this.$route.params)[0];

      const result = await fetch("http://localhost:8000/api/v2/post?id=" + id);
      const data = await result.json();
      this.data = data;
    },
  },
};
</script>

<template>
  <div class="wrapper">
    <div class="container">
      <div class="container-news">
        <router-link :to="{ name: 'news' }">
          <span class="back">← Вернуться</span>
        </router-link>
        <div class="date_news">
          {{ data.date }}
        </div>
        <div class="tags">
          <span class="tag" v-for="tag in data.tags" :key="tag">
            {{ tag }}
          </span>
        </div>
        <div class="title_news">
          {{ data.title }}
        </div>
        <div class="body_news">
          {{ data.full_text }}
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  padding: 100px 0 !important;
  display: flex !important;
}
.container-news {
  margin: 0 20px 60px 20px;
}
.back {
  color: #34495e;
  font-family: "Raleway", sans-serif;
  border: 1px solid rgba(60, 60, 60, 0.12);
  border-radius: 5px;
  padding: 5px;
  margin-bottom: 10px;
}
.date_news {
  color: #3ecf8e;
  font-size: 25px;
  font-family: "Raleway", sans-serif;
  margin: 10px 0;
}
.tag {
  margin-right: 10px;
  font-family: "Raleway", sans-serif;
  background: #42b983;
  padding: 2px 8px;
  color: #fff;
  border-radius: 5px;
  text-transform: uppercase;
}
.title_news {
  margin: 10px 0;
  color: #373737;
  font-size: 21px;
  font-family: "Raleway", sans-serif;
}
.body_news {
  color: #5f6061;
  font-size: 17px;
  font-family: "Raleway", sans-serif;
  line-height: 1.4;
  white-space: pre-line;
}
</style>