<script>
export default {
  data() {
    return {
      data: {},
      next: {},
      previous: {},
    };
  },
  beforeMount() {
    this.getNews();
  },
  methods: {
    async getNews() {      
      const result = await fetch(`http://${import.meta.env.VITE_BACKEND_HOST}/api/v2/news?page=1`);
      const data = await result.json();
      this.previous = data.previous;
      this.next = data.next;
      this.data = data.results;
    },
    async changePages(page) {
      const result = await fetch(page);
      const data = await result.json();
      this.previous = data.previous;
      this.next = data.next;
      this.data = data.results;
      window.scrollTo(0, 0);
    },
  },
};
</script>

<template>
  <div class="wrapper">
    <div class="container">
      <div class="container-content">
        <TransitionGroup name="list">
          <div class="container-news" v-for="item in data" :key="item.id">
            <div class="head_info">
              <span class="news_id">#{{ item.id }}</span>
              <span class="news_date">{{ item.date }}</span>
            </div>
            <div class="head_tag">
              <span class="tag" v-for="tag in item.tags" :key="tag">
                {{ tag }}
              </span>
            </div>
            <div class="head_news">
              <router-link :to="{ name: 'post', params: { post_pk: item.id } }">
                <span class="news_head">
                  {{ item.title }}
                </span>
              </router-link>
            </div>
            <div class="body_news">
              {{ item.anons }}
            </div>
            <div class="line_news"></div>
          </div>
        </TransitionGroup>
        <div class="paginator">
          <div>
            <span
              @click="changePages(previous)"
              class="pages"
              v-if="previous !== null"
            >
              ← Предыдущая
            </span>
          </div>
          <div>
            <span @click="changePages(next)" class="pages" v-if="next !== null">
              Следующая →
            </span>
          </div>
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
/* animation list news */
.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

.wrapper {
  max-width: 1200px;
  margin: 0 auto;
}
/* list */
.container {
  padding: 100px 20px;
  display: flex;
}
.container-content {
  width: 95%;
}
/* news */
.container-news {
  margin-bottom: 60px;
  box-sizing: border-box;
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
.news_head:hover {
  color: #3ecf8e !important;
  transition: 0.3s linear;
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
  display: flex;
  flex-wrap: wrap;
}
.tag {
  margin-bottom: 5px;
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
@media (max-width: 1024px) {
  .sidebar {
    display: none;
  }
}
.sidebar {
  box-sizing: border-box;
  padding-left: 20px;
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
.paginator {
  display: flex;
  justify-content: space-between;
  margin: 0 20px;
}
.pages {
  font-family: "Raleway", sans-serif;
  border: 1px solid rgba(60, 60, 60, 0.12);
  border-radius: 5px;
  padding: 5px;
  cursor: pointer;
}
</style>
