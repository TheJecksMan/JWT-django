import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import Markdown from 'vue3-markdown-it';
import VueCookies from 'vue-cookies';

const app = createApp(App);

app.use(router);
app.use(Markdown);
app.use(VueCookies);

app.mount("#app");
