import Vue from 'vue'
import Router from 'vue-router'


Vue.use(Router)


export function createRouter() {
  return new Router({
    mode: 'history',
    routes: [
      {
        path: '/',
        name: 'landing',
        component: () => import('~/pages/index').then(m => m.default || m)
      },
      {
        path: '/login',
        name: 'login',
        component: () => import('~/pages/auth/login').then(m => m.default || m)
      },
      {
        path: '/register',
        name: 'register',
        component: () => import('~/pages/auth/register').then(m => m.default || m)
      },
      {
        path: '/password',
        name: 'password',
        component: () => import('~/pages/auth/password').then(m => m.default || m)
      },
      {
        path: '/dashboard/chat',
        name: 'dashboard.chat',
        component: () => import('~/pages/dashboard/chat').then(m => m.default || m)
      },
      {
        path: '/dashboard/explore',
        name: 'dashboard.explore',
        component: () => import('~/pages/dashboard/explore').then(m => m.default || m)
      },
      {
        path: '/dashboard/feed',
        name: 'dashboard.feed',
        component: () => import('~/pages/dashboard/feed').then(m => m.default || m)
      },
      {
        path: '/dashboard',
        name: 'dashboard',
        component: () => import('~/pages/dashboard/index').then(m => m.default || m)
      },
      {
        path: '/dashboard/market',
        name: 'dashboard.market',
        component: () => import('~/pages/dashboard/market').then(m => m.default || m)
      },
      {
        path: '/dashboard/profile',
        name: 'dashboard.profile',
        component: () => import('~/pages/dashboard/profile').then(m => m.default || m)
      },
      {
        path: '/dashboard/setting',
        name: 'dashboard.setting',
        component: () => import('~/pages/dashboard/setting').then(m => m.default || m)
      },
      {
        path: '/dashboard/trending',
        name: 'dashboard.trending',
        component: () => import('~/pages/dashboard/trending').then(m => m.default || m)
      }
    ]
  })
}
