<template>
  <div class="min-h-screen bg-agri-bg">
    <Navbar :showNotifications="false" />

    <main class="max-w-5xl mx-auto px-4 py-6">
      <router-view />
    </main>

    <Footer />
  </div>
</template>

<script setup>
import Navbar from "../components/common/Navbar.vue";
import Footer from "../components/common/Footer.vue";
</script>
