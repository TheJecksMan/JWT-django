<script>
export default {
  data() {
    return {
      email: "",
      username: "",
      password: "",
      password_repeat: "",
      is_error: false,
      activeClass: "form__field-input",
      errorClass: "form__field-input input__error",
    };
  },
  methods: {
    async registration() {
      // this.is_error = false;
      // if (this.user == "" && this.password == "") {
      //   this.is_error = true;
      //   return;
      // }

      const data = {
        email: this.email,
        username: this.username,
        password: this.password,
        password_repeat: this.password_repeat,
      };
      const csrfToken = this.$cookies.get("csrftoken");

      const result = await fetch(
        `http://${import.meta.env.VITE_BACKEND_HOST}/api/v2/auth/registration`,
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
      if (result.status == 200) {
        this.$router.push("/login");
      } else {
        this.is_error = true;
      }
    },
  },
};
</script>

<template>
  <div class="layout">
    <div class="layout__page">
      <div class="box">
        <div class="box_title">Регистрация</div>
        <div class="box_form">
          <div class="form__imputs">
            <span class="form__field-label">Email</span>
            <div>
              <input
                type="email"
                class="form__field-input"
                placeholder="example@gmail.com"
                v-model="email"
              />
            </div>
          </div>
          <div class="form__imputs">
            <span class="form__field-label">Логин</span>
            <div>
              <input
                type="text"
                class="form__field-input"
                placeholder="user"
                v-model="username"
              />
            </div>
          </div>
          <div class="form__imputs">
            <span class="form__field-label">Пароль</span>
            <div>
              <input
                type="password"
                class="form__field-input"
                v-model="password"
              />
            </div>
          </div>
          <div class="form__imputs">
            <span class="form__field-label">Повторите пароль</span>
            <div>
              <input
                type="password"
                class="form__field-input"
                v-model="password_repeat"
              />
            </div>
          </div>
          <div class="form__buttons">
            <button @click="registration" type="sumbit" class="button">
              Зарегистрироваться
            </button>
          </div>
        </div>
      </div>
      <div class="box box_register">
        <span class="form__field-label form__reg">
          Уже есть аккаунт?
          <router-link :to="{ name: 'login' }">Войдите!</router-link>
        </span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.layout {
  height: 100vh;
  width: 100%;
  min-width: 320px;
  overflow-x: hidden;
}
.layout__page {
  margin: 0 auto;
  margin-top: 200px;
  max-width: 460px;
}
.box {
  background: #fff;
  box-shadow: 0 2px 4px 0 rgb(0 0 0 / 10%);
  border-radius: 4px;
  padding: 40px;
  margin-bottom: 20px;
}
.box_register {
  padding: 20px !important;
  text-align: center;
}
.box_title {
  font-family: "Raleway", sans-serif;
  font-size: 22px;
  line-height: 26px;
  font-weight: 700;
}
.form__imputs {
  margin-top: 30px;
}
.form__field-input {
  width: 100%;
  height: 40px;
  background: #fff;
  border: 1px solid #dbdbdb;
  padding: 0 14px;
  box-sizing: border-box;
  font-size: 14px;
  font-family: "Raleway", sans-serif;
  color: #333;
}
.form__field-label {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  line-height: 16px;
  color: #333;
  font-size: 14px;
  font-family: "Raleway", sans-serif;
  font-weight: 700;
  margin-bottom: 12px;
  display: inline-block;
  width: 100%;
  vertical-align: baseline;
}
.form__reg {
  margin-bottom: 0 !important;
}
.form__buttons {
  margin-top: 28px;
}
.button {
  font-family: "Raleway", sans-serif;
  cursor: pointer;
  border-radius: 4px;
  border: 1px solid #33aa74;
  background: #33aa74;
  color: #fff;
  width: 100%;
  height: 48px;
}
.form__field_socials {
  margin-top: 36px;
}
</style>
