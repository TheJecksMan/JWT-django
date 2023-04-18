<script>
export default {
  data() {
    return {
      username: "",
      password: "",
      is_error: false,
      activeClass: "form__field-input",
      errorClass: "form__field-input input__error",
    };
  },

  methods: {
    async login() {
      this.is_error = false;
      if (this.user == "" && this.password == "") {
        this.is_error = true;
        return;
      }

      const data = {
        username: this.username,
        password: this.password,
      };
      const csrfToken = this.$cookies.get("csrftoken");

      const result = await fetch(
        `http://${import.meta.env.VITE_BACKEND_HOST}/api/v2/auth/login_site`,
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
        this.$router.push("/news");
      } else {
        this.is_error = true;
      }
    },
  },
};
</script>


<template>
  <div class="wrapper">
    <div class="container">
      <div class="box">
        <div class="box_title">Вход</div>
        <div class="box_form">
          <div class="form_inputs">
            <span class="form__field-label">Логин</span>
            <div class="form__field">
              <input
                type="text"
                :class="[is_error ? errorClass : '', activeClass]"
                v-model="username"
              />
            </div>
          </div>
          <div class="form_inputs">
            <span class="form__field-label">Пароль</span>
            <div class="form__field">
              <input
                type="password"
                :class="[is_error ? errorClass : '', activeClass]"
                v-model="password"
              />
            </div>
          </div>
          <div v-if="is_error == true" class="error">
            Некорректный логин или пароль. Проверьте введёные данные!
          </div>
          <div class="form__buttons">
            <button @click="login" type="sumbit" class="button">Войти</button>
            <div class="resset_password">Забыли пароль?</div>
          </div>
        </div>
      </div>
      <div class="box box_register">
        <span class="form__field-label form__reg">
          Ещё нет аккаунт?
          <router-link :to="{ name: 'registration' }">
            Загрегистрируйся!
          </router-link>
        </span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.wrapper {
  height: 100vh;
  width: 100%;
  min-width: 320px;
  overflow-x: hidden;
  background: #f4f4f4;
}
/* list */
.container {
  margin: 0 auto;
  margin-top: 220px;
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
.box_form {
  margin: 0;
}
.box_title {
  font-family: "Raleway", sans-serif;
  font-size: 22px;
  line-height: 26px;
  font-weight: 700;
}
.form_inputs {
  margin-top: 30px;
}
.form__field-input {
  width: 100%;
  height: 40px;
  background: #fff;
  border: 1px solid #dbdbdb;
  font-size: 14px;
  font-family: "Raleway", sans-serif;
  padding: 0 14px;
  box-sizing: border-box;
}
.form__field-label {
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
  font-size: 14px;
  font-family: "Raleway", sans-serif;
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
.resset_password {
  margin-top: 15px;
  font-size: 14px;
  font-family: "Raleway", sans-serif;
}
.error {
  color: #de5959;
  font-size: 12px;
  font-family: "Raleway", sans-serif;
  font-weight: 500;
  line-height: 18px;
  margin-top: 12px;
  animation: color_change 1s;
}

@keyframes color-change {
  0% {
    border-color: #ff6e6e;
  }
  100% {
    border-color: #dbdbdb;
  }
}

.input__error {
  animation: color-change 8s 1;
}
</style>