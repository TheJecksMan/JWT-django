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
      count_comments: 0,
      data: {},
      comments: {},
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

      const result = await fetch("http://localhost:8000/api/v2/post?id=" + id);
      if (result.status != 200) {
        this.$router.replace({ path: "/error" });
      }
      const data = await result.json();
      this.data = data;
    },
    async getComments() {
      let id = Object.values(this.$route.params)[0];
      const result = await fetch(
        "http://localhost:8000/api/v2/news/get_comment?news=" + id
      );
      const comments = await result.json();
      this.comments = comments;
      this.count_comments = comments.count;
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
      console.log(response.status);
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
          <div class="comment">
            <div v-if="count_comments == 0">
              <div class="body-comment">
                Тут пока нет комментариев.. Будьте первым!
              </div>
            </div>
            <div v-else>
              <div
                class="comments-div"
                v-for="comment in comments.results"
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
            </div>
          </div>
        </div>
        <div class="create-comment">
          <md-editor v-model="text" language="en-US" />
          <button @click="sendComment" type="submit">Отправить</button>
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
  margin-top: 30px;
}
.title-comment {
  color: #373737;
  font-size: 21px;
  font-family: "Raleway", sans-serif;
}
.comments-div {
  margin: 25px 0;
}
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
</style>