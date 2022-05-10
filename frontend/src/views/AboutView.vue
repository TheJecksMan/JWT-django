<template>
  <div class="wrapper">
    <div class="container">
      <div class="about">
        <section id="container-about-name">
          <h1 class="tagline">SmartNoteBook</h1>
          <span class="description">Мобильное приложение</span>
          <div class="actions">
            <a class="action" href="#">Новости</a>
            <a class="action" href="#">Скачать</a>
          </div>
        </section>
        <section id="container-about-project">
          <span class="project">О проекте</span>
        </section>
        <div class="minimal-about">
          <div class="about_text">
            SmartNoteBook - создавался как дипломная работа. Проект
            предоставляет возможность создание/управления своими заметками.
          </div>
          <div class="about_text">
            Цель проекта состоит в том, чтобы показать минимальную работу с
            требуемыми технологиям.
          </div>
        </div>

        <section id="container-about">
          <div class="about_text">Простота - заметками легко управлять</div>
          <div class="about_text">
            Гибкость - предоставляет возможность входа в свой акканут
          </div>
        </section>
      </div>
      <section id="frameworks">
        <p class="about_text">Используемые frameworks:</p>
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
      </section>
      <section id="languages">
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
      </section>
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
  margin-right: 30px;
}
.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: 150px;
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
#container-about-name {
  padding: 96px 32px;
  text-align: center;
}
.tagline {
  font-family: "Raleway", sans-serif;
  background: -webkit-linear-gradient(315deg, #42d392 25%, #647eff);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-size: 76px;
  line-height: 1.25;
  font-weight: 900;
  letter-spacing: -1.5px;
  max-width: 960px;
  margin: 0 auto;
}
.description {
  font-family: "Raleway", sans-serif;
  max-width: 960px;
  line-height: 1.5;
  color: #213547;
  transition: color 0.5s;
  font-size: 28px;
  margin: 24px auto 40px;
}
.actions {
  margin: 30px 0;
}
.action {
  font-family: "Raleway", sans-serif;
  color: #fff !important;
  background-color: #3ecf8e;
  margin: 10px;
  font-size: 16px;
  border-radius: 8px;
  padding: 13px;
}

#container-about-project {
  border-radius: 5px;
  border: 1px solid rgba(60, 60, 60, 0.12);
  padding: 12px 24px;
  text-align: center;
}

.project {
  font-size: 21px;
  font-family: "Raleway", sans-serif;
}
.minimal-about {
  padding: 35px 0;
}
#container-about {
  display: flex;
  padding: 35px 0;
  justify-content: center;
}
#frameworks {
  padding: 35px 0;
}
</style>
