<script>
import MarkdownItVue from "vue3-markdown-it";
import "@/assets/markdown.css";

import MdEditor from "md-editor-v3";
import "md-editor-v3/lib/style.css";

export default {
  components: {
    MarkdownItVue,
    MdEditor,
  },
  data() {
    return {
      num_page_comment: 1,
      count_comments: 0,
      data: {},
      comments: {},
      next: {},
      previous: {},
      text: "",
    };
  },
  beforeMount() {
    this.getPost();
    this.getComments();
  },
  methods: {
    async getPost() {
      let id = Object.values(this.$route.params)[0];

      const result = await fetch(`http://${import.meta.env.VITE_BACKEND_HOST}/api/v2/post?id=` + id);
      if (result.status != 200) {
        this.$router.replace({ path: "/error" });
      }
      const data = await result.json();
      this.data = data;
    },
    async getComments() {
      let id = Object.values(this.$route.params)[0];
      const result = await fetch(
        `http://localhost:8000/api/v2/news/get_comment?news=${id}&ordering=-date&page=${this.num_page_comment}`
      );
      const data = await result.json();
      this.comments = data.results;
      this.previous = data.previous;
      this.next = data.next;
      this.count_comments = data.count;
    },

    async sendComment() {
      const csrfToken = this.$cookies.get("csrftoken");

      const data = {
        text: this.text,
        news_id: Object.values(this.$route.params)[0],
      };

      const response = await fetch(
        "http://localhost:8000/api/v2/news/add_comment",
        {
          method: "POST",
          mode: "cors",
          credentials: "include",
          headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
          },
          body: JSON.stringify(data),
        }
      );
      // const res = await result.json();
      if (response.status == 200) {
        await this.getComments();
        this.text = "";
      } else {
        const data = await response.json();
        alert(data.detail.text);
      }
    },
    async changePages(page) {
      const result = await fetch(page);
      const data = await result.json();
      this.comments = data.results;
      this.previous = data.previous;
      this.next = data.next;
    },
  },
};
</script>

<template>
  <div class="wrapper">
    <div class="container">
      <div class="container-news">
        <router-link :to="{ name: 'news' }">
          <span class="back">← Вернуться</span>
        </router-link>
        <div class="date_news">
          {{ data.date }}
        </div>
        <div class="tags">
          <span class="tag" v-for="tag in data.tags" :key="tag">
            {{ tag }}
          </span>
        </div>
        <div class="title_news">
          {{ data.title }}
        </div>
        <div class="line_news"></div>
        <div class="body_news">
          <MarkdownItVue
            :source="data.full_text"
            :html="true"
            :typographer="true"
            :xhtmlOut="true"
            :linkify="true"
            :breaks="true"
          />
        </div>
        <div class="line_news"></div>
        <div class="container-comment">
          <span class="title-comment">Комментарии</span>
        </div>
        <div class="container-comment">
          <div class="create-comment">
            <md-editor v-model="text" language="en-US" />
            <div class="send-commnet">
              <button
                class="button button-comment"
                @click="sendComment"
                type="submit"
              >
                Отправить
              </button>
            </div>
          </div>
          <div class="comment">
            <div v-if="count_comments == 0">
              <div class="body-comment">
                Тут пока нет комментариев.. Будьте первым!
              </div>
            </div>
            <div v-else>
              <div
                class="comments-div"
                v-for="comment in comments"
                :key="comment.id"
              >
                <div class="user-comment">
                  <span class="user-color">Пользователь: </span
                  >{{ comment.user }}
                </div>
                <div class="body-comment">
                  <MarkdownItVue
                    :source="comment.comment"
                    :html="true"
                    :typographer="true"
                    :xhtmlOut="true"
                    :linkify="true"
                    :breaks="true"
                  />
                </div>
              </div>
              <div v-if="count_comments != 0" class="paginator">
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
                  <span
                    @click="changePages(next)"
                    class="pages"
                    v-if="next !== null"
                  >
                    Следующая →
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  padding: 100px 0 !important;
}
.container-news {
  margin: 0 30px 60px 20px;
}
.back {
  color: #34495e;
  font-family: "Raleway", sans-serif;
  border: 1px solid rgba(60, 60, 60, 0.12);
  border-radius: 5px;
  padding: 5px;
  margin-bottom: 10px;
}
.date_news {
  color: #3ecf8e;
  font-size: 25px;
  font-family: "Raleway", sans-serif;
  margin: 10px 0;
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
.title_news {
  margin-top: 20px;
  margin-bottom: 10px;
  color: #373737;
  font-size: 21px;
  font-family: "Raleway", sans-serif;
}
.body_news {
  color: #5f6061;
  font-size: 17px;
  font-family: "Raleway", sans-serif;
}
.line_news {
  margin: 30px 0 20px;
  border: none;
  border-top: 1px solid #ddd;
}
.container-comment {
  margin-top: 20px;
}
.title-comment {
  color: #373737;
  font-size: 21px;
  font-family: "Raleway", sans-serif;
}
.comments-div {
  margin: 25px 0;
}
/* comments */
.user-comment {
  color: #3ecf8e;
  font-size: 16px;
  font-family: "Raleway", sans-serif;
}
.body-comment {
  font-size: 14px;
  font-family: "Raleway", sans-serif;
  margin: 10px 0;
  color: #5f6061;
}
.create-comment {
  margin: 25px 0;
}
.user-color {
  color: #373737 !important;
}
.send-commnet {
  display: flex;
}
.button {
  font-family: "Raleway", sans-serif;
  cursor: pointer;
  border-radius: 4px;
  border: 1px solid #33aa74;
  background: #33aa74;
  color: #fff;
  height: 48px;
}
.button-comment {
  margin-left: auto;
  margin-top: 10px;
  padding: 0 10px;
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