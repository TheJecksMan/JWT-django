<script setup>
</script>

<template>
  <header>
    <div class="wrapper">
      <div class="container">
        <div class="container__inner">
          <span class="logo">SmartNoteBook</span>
          <div class="navigation container__inner">
            <span class="item">Главная</span>
            <span class="item">Новости</span>
            <span class="item">О программе</span>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<style>
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@900&display=swap");
body {
  padding: 0;
  margin: 0;
}
/* header */
.wrapper {
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
  margin-left: auto;
}

.logo {
  color: white;
  margin: 10px;
  font-family: "Raleway", sans-serif;
}
.navigation {
  margin: 10px;
}
.item {
  color: white;
  margin: 0 10px;
  font-family: "Raleway", sans-serif;
}
</style>
