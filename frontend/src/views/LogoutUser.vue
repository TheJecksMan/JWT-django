<script>
export default {
  methods: {
    async logout() {
      const csrfToken = this.$cookies.get("csrftoken");

      await fetch(`http://${import.meta.env.VITE_BACKEND_HOST}/api/v2/auth/logout`, {
        method: "POST",
        mode: "cors",
        credentials: "include",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
      });
      this.$router.push("/news");
    },
    cancel() {
      this.$router.push("/news");
    },
  },
};
</script>

<template>
  <div class="wrapper">
    <div class="content">
      <div class="content__inner">
        <div class="text">Вы уверены что хотите выйти?😢..</div>
        <div class="variant">
          <div @click="cancel" class="button">Нет</div>
          <div @click="logout" class="button">Да</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.wrapper {
  align-items: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  background: white;
  width: 100%;
  height: 100vh;
  margin: 0 auto;
  text-align: center;
}
.content__inner {
  display: flex;
  flex-direction: column;
}
.text {
  color: black;
  font-size: 32px;
  font-family: "Raleway", sans-serif;
}
.content {
  display: flex;
}
.variant {
  margin-top: 20px;
  display: flex;
  justify-content: space-around;
}
.button {
  text-align: center;

  padding: 10px;
  font-family: "Raleway", sans-serif;
  cursor: pointer;
  border-radius: 4px;
  border: 1px solid #33aa74;
  background: #33aa74;
  color: #fff;
}
</style>