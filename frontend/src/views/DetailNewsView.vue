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
      console.log(data);
    },
  },
};
</script>
<template></template>

<style scoped>
</style>