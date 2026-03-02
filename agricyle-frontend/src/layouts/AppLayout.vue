<template>
  <div class="min-h-screen bg-agri-bg flex">
    <Sidebar />

    <div class="flex-1 flex flex-col">
      <Navbar :showNotifications="true" />

      <main class="flex-1 max-w-6xl w-full mx-auto px-4 py-6">
        <router-view />
      </main>

      <Footer />
    </div>
  </div>
</template>

<script setup>
import Sidebar from "../components/common/Sidebar.vue";
import Navbar from "../components/common/Navbar.vue";
import Footer from "../components/common/Footer.vue";
</script>
