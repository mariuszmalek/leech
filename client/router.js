import Vue from 'vue'
import Router from 'vue-router'
import { scrollBehavior } from '~/utils'

import MyRouter from '@/routes/index'

Vue.use(Router)


export function createRouter() {
  return new Router({
    MyRouter,
    scrollBehavior,
    mode: 'history'
  })
}
