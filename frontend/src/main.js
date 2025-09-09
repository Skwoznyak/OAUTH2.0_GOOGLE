import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue';

import Home from './components/Home.vue';
import AuthGoogle from './components/AuthGoogle.vue';

const routes = [
    { path: '/', component: Home },
    { path: '/auth/google', component: AuthGoogle }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

createApp(App).use(router).mount('#app');
