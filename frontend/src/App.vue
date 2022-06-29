<template>
  <div class="wrapper_main">
    <header>
      <div class="wrapper">
        <div class="container">
          <div class="container__inner">
            <div class="logo">
              <img src="@/assets/logo.svg" alt="" width="35" height="35" />
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
  margin: 10px;
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
