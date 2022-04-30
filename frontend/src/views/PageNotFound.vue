<template>
  <div class="wrapper_not_found">
    <div class="content_not_found">
      <img class="error" src="@/assets/crying-emoji-svgrepo-com.svg" />
      <div class="content__inner">
        <span class="error_text">Запрашиваемый ресурс не найден😢..</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@900&display=swap");

.wrapper_not_found {
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
}
.error {
  width: 250px;
  height: 250px;
}
.error_text {
  color: black;
  font-size: 32px;
  font-family: "Raleway", sans-serif;
}
</style>