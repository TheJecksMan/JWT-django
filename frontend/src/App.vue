<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

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
              <div>
                <RouterLink to="/">
                  <span class="item">Главная</span>
                </RouterLink>
              </div>
              <div>
                <RouterLink to="/news">
                  <span class="item">Новости</span>
                </RouterLink>
              </div>
              <div>
                <RouterLink to="/about">
                  <span class="item">О программе</span>
                </RouterLink>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
    <main>
      <router-view> </router-view>
    </main>
  </div>
</template>

<style>
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@900&display=swap");
body {
  padding: 0;
  margin: 0;
}
a {
  text-decoration: none;
}
/* header */
.wrapper {
  z-index: 1000;
  position: absolute;
  width: 100%;
  height: 48px;
  background: transparent;
}
.container {
  margin: 0 auto;
  padding: 16px 0;
  max-width: 1200px;
}
.container__inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-left: auto;
}

.logo {
  display: flex;
  align-items: center;
}
.logo_text {
  color: white;
  margin: 10px;
  font-size: 25px;
  font-family: "Raleway", sans-serif;
}
.navigation {
  margin: 10px;
}
.item {
  color: white;
  margin: 0 10px;
  font-size: 18px;
  font-family: "Raleway", sans-serif;
}
</style>

