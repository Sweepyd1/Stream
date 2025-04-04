import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import anime_page from '@/views/anime_page.vue'
import profile from '@/views/profile/profile.vue'
import login from '@/views/auth/login.vue'
import register from '@/views/auth/register.vue'
import serial_page from '@/views/serial_page.vue'
import discussions from '@/views/discussions.vue'
import test from '@/views/test.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/anime',
      name: 'anime',
      component: anime_page,
    },
    {
      path: '/discussions',
      name: 'discussions',
      component: discussions,
    },
    {
      path: '/profile',
      name: 'profile',
      component: profile,
    },
    {
      path: '/serial',
      name: 'serial',
      component: serial_page,
    },
    {
      path: '/login',
      name: 'login',
      component: login,
    },
    {
      path: '/register',
      name: 'register',
      component: register,
    },
    {
      path: '/test',
      name: 'test',
      component: test,
    },
    {
      path: '/about',
      name: 'about',
 
      component: () => import('../views/AboutView.vue'),
    },
  ],
})

export default router
