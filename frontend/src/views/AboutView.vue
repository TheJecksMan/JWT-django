<template>
  <div class="wrapper">
    <div class="container">
      <div class="about">
        <p class="about_text">
          SmartNoteBook является разработкой, которая создавалась для дипломной
          работы.
        </p>
        <p class="about_text">
          В данной работе использовались следующие технологии:
        </p>
      </div>
      <div class="frameworks">
        <p class="about_text">frameworks:</p>
        <div class="grid-container">
          <div class="image">
            <img src="@/assets/Django_logo.svg" alt="" />
          </div>
          <div class="image">
            <img src="@/assets/Vue_logo.svg" alt="" />
          </div>
          <div class="image">
            <img src="@/assets/Android_logo.svg" alt="" />
          </div>
        </div>
      </div>
      <div class="languages">
        <p class="about_text">Языки программирования:</p>
        <div class="grid-container">
          <div class="image">
            <img src="@/assets/Java_logo.svg" alt="" />
          </div>
          <div class="image">
            <img src="@/assets/Kotlin_logo.svg" alt="" />
          </div>
          <div class="image">
            <img src="@/assets/Python_logo.svg" alt="" />
          </div>
          <div class="image">
            <img src="@/assets/js_logo.svg" alt="" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.wrapper {
  max-width: 1200px;
  margin: 0 auto;
}
.container {
  padding: 100px 20px;
}
.about_text {
  color: #373737;
  font-size: 18px;
  font-family: "Raleway", sans-serif;
}
.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: 200px;
  grid-row-gap: 1em;
  grid-column-gap: 1em;
}
.image {
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f9f9f9;
  padding: 20px;
}
img {
  max-width: 100%;
  max-height: 100%;
}
</style>
