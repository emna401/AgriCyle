<template>
  <header class="sticky top-0 z-50 bg-black/20 backdrop-blur-lg border-b border-white/10">
    <div class="max-w-6xl mx-auto px-4 py-3 flex items-center justify-between">
      <!-- Left -->
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-white/10 backdrop-blur-sm flex items-center justify-center shadow-lg border border-white/20">
          <span class="text-white text-lg">🌿</span>
        </div>

        <div>
          <div class="font-bold text-lg text-white leading-tight">
            {{ $t("app.name") }}
          </div>
          <div class="text-xs text-white/70 hidden sm:block">
            {{ $t("app.tagline") }}
          </div>
        </div>
      </div>

      <!-- Right -->
      <div class="flex items-center gap-3">
        <LanguageSwitcher />
        <router-link
          v-if="!auth.isLoggedIn"
          to="/login"
          class="agri-btn-header"
        >
          {{ $t("nav.login") }}
        </router-link>

        <button
          v-else
          @click="onLogout"
          class="agri-btn-outline-header"
        >
          {{ $t("nav.logout") }}
        </button>
      </div>
    </div>
  </header>
</template>

<script setup>
import { useAuthStore } from "../../store/auth";
import LanguageSwitcher from "./LanguageSwitcher.vue";
import NotificationBell from "./NotificationBell.vue";

defineProps({
  showNotifications: { type: Boolean, default: false }
});

const auth = useAuthStore();

function onLogout() {
  auth.logout();
  window.location.href = "/";
}
</script>

<style scoped>
/* Styles pour les boutons du header */
.agri-btn-header {
  background: linear-gradient(135deg, #48bb78 0%, #2f855a 100%);
  color: white;
  border-radius: 10px;
  padding: 0.5rem 1.25rem;
  font-weight: 600;
  font-size: 0.875rem;
  transition: all 0.3s ease;
  border: none;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 15px rgba(72, 187, 120, 0.3);
  text-decoration: none;
}

.agri-btn-header:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(72, 187, 120, 0.4);
  background: linear-gradient(135deg, #5cc489 0%, #3a9a6b 100%);
}

.agri-btn-outline-header {
  border: 2px solid white;
  color: white;
  border-radius: 10px;
  padding: 0.5rem 1.25rem;
  font-weight: 600;
  font-size: 0.875rem;
  transition: all 0.3s ease;
  background: transparent;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 15px rgba(255, 255, 255, 0.1);
}

.agri-btn-outline-header:hover {
  background: white;
  color: #2f855a;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(255, 255, 255, 0.2);
}

/* Effet de texte avec ombre pour mieux ressortir */
.text-white {
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.font-bold {
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.4);
}

/* Effet de verre pour le header */
.bg-black\/20 {
  background-color: rgba(0, 0, 0, 0.2);
}

.backdrop-blur-lg {
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
}

.border-white\/10 {
  border-color: rgba(255, 255, 255, 0.1);
}

/* Pour l'icône dans le logo */
.bg-white\/10 {
  background-color: rgba(255, 255, 255, 0.1);
}

.backdrop-blur-sm {
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

/* Responsive */
@media (max-width: 640px) {
  .agri-btn-header,
  .agri-btn-outline-header {
    padding: 0.4rem 0.8rem;
    font-size: 0.75rem;
  }
  
  .text-lg {
    font-size: 1rem;
  }
  
  .text-xs {
    font-size: 0.65rem;
  }
}
</style>