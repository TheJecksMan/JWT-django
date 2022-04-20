<template>
    <main>
        <header class="header">
            <div class="container">
                <div class="header__inner">
                    <div class="header__logo">SmartNoteBook</div>

                    <nav class="nav">
                        <a class="nav__link" href="#">Новости</a>
                        <a class="nav__link btn" href="#">О нас</a>
                    </nav>

                </div>
            </div>
        </header>
    </main>
</template>

<style>
/* Container */
.container {
    max-width: 1200px;
    width: 100%;
    margin: 0 auto;
}

@media(max-width: 1230px) {
    .container {
        max-width: 900px;
    }
}

@media(max-width: 992px) {
    .container {
        max-width: 700px;
    }
}

@media(max-width: 768px) {
    .container {
        max-width: 600px;
    }
}

body{
  margin: 0;
}

.header {
    width: 100%;
    padding-top: 25px;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
}

.header__inner {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.header__logo {
    font-size: 28px;
    font-weight: 700;
    color: #fff;
}

/* Nav */
.nav {
    font-size: 18px;
}

.nav__link {
    display: inline-block;
    vertical-align: top;
    margin: 0 15px;
    position: relative;

    color: #fff;
    text-decoration: none;

    transition: color .1s linear;
}

</style>