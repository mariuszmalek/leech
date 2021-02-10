<template>
    <div id="wrapper">

        <Sidebar />

        <div class="main_content">

            <Header />
            <Nuxt />

        </div>

    </div>
</template>
<script>
import Sidebar from '../components/partials/Sidebar'
import Header from '../components/partials/Header'
export default {
    components: {
        Sidebar,
        Header
    }
}
</script>
