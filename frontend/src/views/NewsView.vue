<template>
  <div class="wrapper">
    <div class="container">
      <div class="container-content">
        <div class="container-news">
          <div class="head_info">
            <span class="news_id">#2</span>
            <span class="news_date">Monday, May 2, 2022</span>
          </div>
          <div class="head_tag">
            <span class="tag">news</span>
          </div>
          <div class="head_news">
            <span class="news_head">
              Немного примеров/мыслей навеянных датой 1 Мая…
            </span>
          </div>
          <div class="body_news">
            Вчера прилетела "напоминалка" с одного "нынче в опале" ресурса, о
            том, что два года назад я поделился с друзьями/подписчиками своим
            свежим опытом общения с современными "производственниками"...
            Выполняю их рекомендации-пожелания (поделиться на HABR), примерно в
            ключе "лучше поздно, чем никогда" :)
          </div>
          <div class="line_news"></div>
        </div>
      </div>
      <div class="container-sidebar">
        <div class="sidebar">
          <div class="sidebar__box">
            <span class="sidebar_text">Официальные новости SmartNoteBook</span>
            <p>
              <span class="sidebar_text sidebar_body_text">
                В данном разделе публикуются отчёты о разработке.
              </span>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<style scoped>
.container {
  padding: 60px 0;
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
}
.container-content {
  width: 95%;
}
/* news */
.container-news {
  margin: 0 20px 60px 20px;
}
.head_info {
  margin: 5px 0;
}
.news_id {
  color: #3ecf8e;
  font-size: 25px;
  font-family: "Raleway", sans-serif;
}
.news_date {
  color: #3ecf8e;
  margin: 0 10px;
  font-size: 25px;
  font-family: "Raleway", sans-serif;
}
.head_news {
  margin-bottom: 5px;
}
.news_head {
  color: #373737;
  font-size: 21px;
  font-family: "Raleway", sans-serif;
}
.body_news {
  color: #5f6061;
  font-size: 17px;
  font-family: "Raleway", sans-serif;
  line-height: 1.4;
  white-space: pre-line;
}
.head_tag {
  margin: 5px 0;
}
.tag {
  margin-right: 10px;
  font-family: "Raleway", sans-serif;
  background: #42b983;
  padding: 2px 8px;
  color: #fff;
  border-radius: 5px;
  text-transform: uppercase;
}
.line_news {
  margin: 30px 0 20px;
  border: none;
  border-top: 1px solid #ddd;
}
/* sidebar */
.container-sidebar {
  display: block;
}
.sidebar {
  box-sizing: border-box;
  margin: 0;
}
.sidebar__box {
  text-align: center;
  background: #f9f9f9;
  padding: 15px;
  border-radius: 5px;
}
.sidebar_text {
  color: #373737;
  font-size: 21px;
  font-family: "Raleway", sans-serif;
}
.sidebar_body_text {
  font-size: 18px !important;
}
/* paginator */
.container-paginator {
  display: flex;
  justify-content: center;
}
.paginator {
  display: inline-block;
}
.paginator a {
  color: black;
  padding: 8px 16px;
  text-decoration: none;
  border-radius: 5px;
  font-family: "Raleway", sans-serif;
}
.paginator a.active {
  background-color: #42b983;
  color: white;
}
.paginator a:hover:not(.active) {
  transition: background-color 0.5s linear;
  background-color: #ddd;
}
</style>