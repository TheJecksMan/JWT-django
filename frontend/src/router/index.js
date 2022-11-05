import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/AboutView.vue"),
    },
    {
      path: "/news",
      name: "news",
      component: () => import("../views/NewsView.vue"),
    },
    {
      path: "/news/post/:post_pk",
      name: "post",
      component: () => import("../views/DetailNewsView.vue"),
    },
    {
      path: "/:pathMatch(.*)*",
      name: "NotFound",
      component: () => import("../views/PageNotFound.vue")
    },
    {
      path: "/login",
      name: "login",
      component: () => import("../views/LoginUser.vue")
    },
    {
      path: "/logout",
      name: "logout",
      component: () => import("../views/LogoutUser.vue")
    },
    {
      path: "/registration",
      name: "registration",
      component: () => import("../views/RegistartionUser.vue")
    }
  ],
});

export default router;
