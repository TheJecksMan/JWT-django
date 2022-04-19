<template>
    <main>
        <header class="header">
            <div class="header_container">
                <div class="header_nav">
                    <span class="header-text">SmartNoteBook</span>
                </div>
                <div class="header_nav">
                    <span class="header-text">Главная</span>
                    <span class="header-text">Новости</span>
                    <span class="header-text">О приложении</span>
                </div>
            </div>
        </header>
    </main>
</template>

<style scoped>
.header {
    position: fixed;
    width: 100%;
    height: 48px;
    background-color: #303b44;
}

.header_container {
    margin: 0 auto;;
    display: flex;
    justify-content: space-between;
}

/* .header_nav {
    display: flex;
    align-items: center;
} */

.header-text {
    margin-left: 8px;
    margin-right: 10px;
    padding-left: 4px;
    font-family: Raleway-Bold;
    font-size: 16px;
    color: white;
    cursor: pointer;
}
</style>