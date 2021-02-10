<template>
  <div class="sidebar">
    <div class="sidebar_header border-b border-gray-200 from-gray-100 to-gray-50 bg-gradient-to-t  uk-visible@s">

      <Logotype />

      <!-- btn night mode -->
      <a href="#" id="night-mode" class="btn-night-mode" data-tippy-placement="left" title="Switch to dark mode"></a>
    </div>
    <div class="border-b border-gray-20 flex justify-between items-center p-3 pl-5 relative uk-hidden@s">
      <h3 class="text-xl"> Navigation </h3>
      <span class="btn-mobile" uk-toggle="target: #wrapper ; cls: sidebar-active"></span>
    </div>
    <div class="sidebar_inner">
      <ul>
        <!-- <li class="active"></li> -->
        <li v-for="(item, index) in menu" :key="index">
          <nuxt-link :to="{ name: item.link }">
            <span> {{ item.name }} </span> <span class="nav-tag" v-if="item.name == 'chat'"> 3</span>
            <!-- <span> {{ item.emoji }} </span> -->
          </nuxt-link>
        </li>
        <li>
          <hr class="my-2">
        </li>
        <li>
          <a href="form-login.html">
            <span> Logout </span> </a>
        </li>
      </ul>
    </div>
  </div>
</template>
<script>
  import Logotype from './Logotype'
  export default {
    components: {
      Logotype
    },
    data() {
      return {
        menu: [{
            id: 1,
            name: 'Feed',
            link: 'dashboard.feed',
            emoji: '🎯' 
          },
          {
            id: 1,
            name: 'Explore',
            link: 'dashboard.explore',
            emoji: '🏄🏽‍♂️'
          },
          {
            id: 1,
            name: 'Chat',
            link: 'dashboard.chat',
            emoji: '🧑🏽‍🦰'
          },
          {
            id: 1,
            name: 'Trending',
            link: 'dashboard.trending',
            emoji: '🥇'
          },
          {
            id: 1,
            name: 'Marketplace',
            link: 'dashboard.market',
            emoji: '🧸'
          },
          {
            id: 1,
            name: 'Setting',
            link: 'dashboard.setting',
            emoji: '💡'
          },
          {
            id: 1,
            name: 'Profile',
            link: 'dashboard.profile',
            emoji: '📊'
          }
        ]
      }
    }
  }

</script>
