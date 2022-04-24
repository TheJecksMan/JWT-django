<script setup>
import Header from "@/components/Header.vue";
</script>

<template>
  <main>
    <div class="wrapper_page">
      <Header />
      <div class="page">
        <div class="shape">
          <div class="span_150 item_shape"></div>
          <div class="span_50 item_shape"></div>
          <div class="span_60 item_shape"></div>
          <div class="span_70 item_shape"></div>
          <div class="span_100 item_shape"></div>
          <div class="span_200 item_shape"></div>
          <div class="span_55 item_shape"></div>
          <div class="span_75 item_shape"></div>
          <div class="span_51 item_shape"></div>
          <div class="span_101 item_shape"></div>
        </div>
        <div class="center_page">
          <h1><span class="item">SmartNotebook</span></h1>
          <div class="description">
            <span class="item">
              Мобильное приложение для составление ежедневных задач, создания
              заметок и даёт много различных приемуществ.
            </span>
          </div>
          <div class="download_page">
            <img src="@/assets/cloud-arrow-down.svg" />
            <span class="download_text">Скачать</span>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<style>
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@900&display=swap");
body {
  padding: 0;
  margin: 0;
}
.wrapper_page {
  height: 100vh;
  background: linear-gradient(150deg, #281483 15%, #8f6ed5 70%, #d782d9 94%);
}

.item_shape {
  position: absolute;
}
/* Shape */
.span_150 {
  left: -4%;
  bottom: auto;
  background: hsla(0, 0%, 100%, 0.1);
  height: 150px;
  width: 150px;
  border-radius: 50%;
}
.span_50 {
  right: 4%;
  top: 10%;
  background: hsla(0, 0%, 100%, 0.1);
  height: 50px;
  width: 50px;
  border-radius: 50%;
}

.span_60 {
  top: 280px;
  right: 5.66666%;
  background: hsla(0, 0%, 100%, 0.3);
  height: 50px;
  width: 50px;
  border-radius: 50%;
}

.span_70 {
  top: 320px;
  right: 7%;
  background: hsla(0, 0%, 100%, 0.15);
  height: 75px;
  width: 75px;
  border-radius: 50%;
}

.span_100 {
  top: 38%;
  left: 1%;
  right: auto;
  background: hsla(0, 0%, 100%, 0.05);
  height: 100px;
  width: 100px;
  border-radius: 50%;
}

.span_200 {
  width: 200px;
  height: 200px;
  top: 44%;
  left: 10%;
  right: auto;
  background: hsla(0, 0%, 100%, 0.15);
  border-radius: 50%;
}

.span_55 {
  right: 50%;
  bottom: 50%;
  background: hsla(0, 0%, 100%, 0.1);
  height: 50px;
  width: 50px;
  border-radius: 50%;
}

.span_75 {
  bottom: 70px;
  right: 2%;
  background: hsla(0, 0%, 100%, 0.2);
  height: 100px;
  width: 100px;
  border-radius: 50%;
}

.span_51 {
  bottom: 1%;
  right: 2%;
  background: hsla(0, 0%, 100%, 0.1);
  height: 50px;
  width: 50px;
  border-radius: 50%;
}
.span_101 {
  bottom: 1%;
  left: 1%;
  right: auto;
  background: hsla(0, 0%, 100%, 0.05);
  height: 100px;
  width: 100px;
  border-radius: 50%;
}

/* main */
.center_page {
  display: flex;
  margin: 10% auto;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  max-width: 700px;
}

.item_page {
  color: white;
  font-family: "Raleway", sans-serif;
}
.download_text {
  color: black;
  margin-left: 10px;
}
.description {
  display: flex;
  align-items: center;
}
.download_page {
  display: flex;
  margin-top: 10px;
  color: black;
  font-family: "Raleway", sans-serif;
  text-transform: uppercase;
  background-color: #fff;
  border-color: #fff;
  border-radius: 5px;
  padding: 0.625rem 1.25rem;
}
</style>
