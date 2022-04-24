<script setup>
</script>

<template>
  <main>
    <header>
      <div class="wrapper">
        <div class="container">
          <div class="container__inner">
            <div class="logo">SmartNoteBook</div>
            <div class="navigation container__inner">
              <div class="item">Главная</div>
              <div class="item">Новости</div>
              <div class="item">О программе</div>
            </div>
          </div>
        </div>
      </div>
    </header>
  </main>
</template>

<style>
/* main */
body {
  padding: 0;
  margin: 0;
}
/* header */
.wrapper {
  width: 100%;
  height: 48px;
}
.container {
  margin: 0 auto;
  max-width: 1200px;
}
.container__inner {
  display: flex;
  justify-content: space-between;
  margin-left: auto;
}

.logo {
  margin: 10px;
}
.navigation {
  margin: 10px;
}
.item {
  margin: 0 10px;
}
</style>
