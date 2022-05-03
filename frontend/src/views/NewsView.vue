<script>
import PaginatorNews from "@/components/Paginator.vue";
</script>

<template>
  <div class="container">
    <div class="container__inner">
      <div class="container__news">
        <div class="head_info">
          <span class="news_id">#2</span>
          <span class="news_date">Monday, May 2, 2022</span>
        </div>
        <div class="head_tag">
          <span class="tag">news</span>
        </div>
        <div class="head_news">
          <span class="news_head"
            >Немного примеров/мыслей навеянных датой 1 Мая…</span
          >
        </div>
        <div class="body_news">
          Вчера прилетела "напоминалка" с одного "нынче в опале" ресурса, о том,
          что два года назад я поделился с друзьями/подписчиками своим свежим
          опытом общения с современными "производственниками"... Выполняю их
          рекомендации-пожелания (поделиться на HABR), примерно в ключе "лучше
          поздно, чем никогда" :)
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
.container__inner {
  display: flex;
  flex-wrap: wrap;
}
.container__news {
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
  line-height: 1.3;
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
</style>