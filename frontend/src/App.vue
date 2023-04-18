<script>
export default {
  data() {
    return {
      username: "",
    };
  },
  beforeMount() {
    this.getUser();
  },
  methods: {
    async getUser() {
      const csrfToken = this.$cookies.get("csrftoken");
      const result = await fetch(
        `http://${import.meta.env.VITE_BACKEND_HOST}/api/v2/profile/current`,
        {
          method: "POST",
          mode: "cors",
          credentials: "include",
          headers: {
            "X-CSRFToken": csrfToken,
            Accept: "application/json",
            "Content-Type": "application/json",
            "X-Requested-With": "XMLHttpRequest",
          },
        }
      );
      const data = await result.json();
      this.username = data.username;
      console.log(this.username);
    },
  },
};
</script>

<template>
  <div class="wrapper_main">
    <header>
      <div class="wrapper">
        <div class="container">
          <div class="container__inner">
            <div class="logo">
              <img src="@/assets/logo.svg" alt="" width="15" height="15" />
              <span class="logo_text">SmartNoteBook</span>
            </div>
            <div class="navigation container__inner">
              <div class="item_bar">
                <RouterLink :to="{ name: 'home' }">
                  <span class="item">Главная</span>
                </RouterLink>
              </div>
              <div class="item_bar">
                <RouterLink :to="{ name: 'news' }">
                  <span class="item">Новости</span>
                </RouterLink>
              </div>
              <div class="item_bar">
                <RouterLink :to="{ name: 'about' }">
                  <span class="item">О программе</span>
                </RouterLink>
              </div>
              <div class="item_bar">
                <div v-if="this.username != undefined" class="dropdown">
                  <div class="dropbtn item item-user">
                    {{ username }}
                  </div>
                  <div class="dropdown-content">
                    <RouterLink :to="{ name: 'logout' }">
                      <span class="item">Выход</span>
                    </RouterLink>
                  </div>
                </div>
                <!-- <span v-if="this.username != undefined" class="item item-user">
                  {{ username }}
                </span> -->
                <div v-else>
                  <RouterLink :to="{ name: 'login' }">
                    <span class="item item-login">Войти</span>
                  </RouterLink>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
    <main>
      <router-view></router-view>
    </main>
  </div>
</template>

<style scoped>
@media screen and (max-width: 992px) {
  .item_bar {
    display: none;
  }
}

/* header */
header {
  width: 100%;
  border-bottom: 1px solid rgba(60, 60, 60, 0.12);
  background: white;
  position: fixed;
  z-index: 100;
}
.wrapper {
  background: white !important;
}
.container__inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 0 20px;
}
.logo {
  display: flex;
  align-items: center;
}
.navigation {
}
.logo_text {
  color: black;
  margin: 10px;
  font-size: 25px;
  font-family: "Raleway", sans-serif;
  cursor: default;
}
.item {
  color: black;
  margin: 0 10px;
  font-size: 18px;
  font-family: "Raleway", sans-serif;
}
.item-user {
  color: #3ecf8e !important;
  cursor: default;
}

.item-login {
  color: #3ecf8e !important;
  cursor: pointer !important;
}

.dropdown {
  float: left;
  overflow: hidden;
}
.dropdown .dropbtn {
  border: none;
  outline: none;
  padding: 14px 16px;
  margin: 0;
}
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 100px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
}
.dropdown-content a {
  float: none;
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}
.dropdown-content a:hover {
  background-color: #ddd;
}
.dropdown:hover .dropdown-content {
  display: block;
}
</style>


<style>
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@900&display=swap");
@import "@/assets/main.css";

body {
  padding: 0;
  margin: 0;
  overflow-y: scroll;
}

a {
  color: #3ecf8e !important;
  text-decoration: none !important;
}
a:visited {
  color: #3ecf8e !important;
}
span p h1 h2 h3 h4 h5 {
  font-family: "Raleway", sans-serif;
}
</style>
