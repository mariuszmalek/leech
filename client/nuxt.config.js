module.exports = {
  mode: 'spa',
  router: {
    base: process.env.DEPLOY_ENV === 'GH_PAGES' ? '/leech/' : '/',
    linkExactActiveClass: 'is-active'
  },
  /*
  ** Headers of the page
  */
  head: {
    titleTemplate: '%s | Leech',
    title: 'Leech',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Leech admin panel' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {
        rel: 'stylesheet',
        href:
          'https://fonts.googleapis.com/css?family=Heebo:400,500,700|Markazi+Text:400,600,700'
      }
    ]
  },

  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },

  /*
  ** Global CSS
  */
  css: [],

  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
    '~/plugins/globals',
    '~/plugins/vue-multiselect',
    '~/plugins/vee-validate',
    '~/plugins/vue-flatpickr',
    '~/plugins/vue-notification.client',
    '~/plugins/vue-goodtable.client',
    '~/plugins/apex-charts.client',
    '~/plugins/vue2-editor.client',
    '~/plugins/vue2-dropzone.client'
  ],

  /*
  ** Nuxt.js modules
  */
  modules: ['@nuxtjs/style-resources', '@nuxtjs/pwa'],

  styleResources: {
    stylus: ['~assets/css/global.styl']
  },
  /*
  ** Build configuration
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    extend(config, ctx) {
      // Run ESLint on save
      if (ctx.isDev && ctx.isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  }
}
