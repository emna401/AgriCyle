<template>
  <aside class="hidden md:flex w-72 flex-col p-4">
    <div class="agri-card p-4">
      <div class="flex items-center gap-3">
        <div class="w-12 h-12 rounded-xl2 bg-agri-green/15 flex items-center justify-center">
          🌱
        </div>
        <div>
          <div class="font-semibold text-agri-text">Menu</div>
          <div v-if="auth.user" class="text-xs text-gray-500">
            {{ auth.user.username }} • {{ $t("roles." + auth.user.role) }}
          </div>
        </div>
      </div>
    </div>

    <div class="mt-4 agri-card p-3 space-y-1">
      <!-- Public -->
      

      <!-- Profile -->
      <router-link
        v-if="auth.role !== 'ADMIN' && auth.role !== 'SUPERADMIN'"
        class="nav-item"
        to="/app/profile"
      >
        👤 {{ $t("nav.profile") }}
      </router-link>

      <!-- Farmer -->
      <template v-if="auth.role === 'FARMER'">
        <router-link class="nav-item" to="/app/farmer">📌 Farmer Dashboard</router-link>
        <router-link class="nav-item" to="/app/farmer/declarations">♻️ {{ $t("nav.declarations") }}</router-link>
      </template>

      <!-- Beneficiary -->
      <template v-if="auth.role === 'BENEFICIARY'">
        <router-link class="nav-item" to="/app/beneficiary">📌 Beneficiary Dashboard</router-link>
        <router-link class="nav-item" to="/app/catalog">🛒 {{ $t("nav.catalog") }}</router-link>
        <router-link class="nav-item" to="/app/cart">🧺 {{ $t("nav.cart") }}</router-link>
        <router-link class="nav-item" to="/app/orders">📦 {{ $t("nav.orders") }}</router-link>
      </template>

      <!-- Dual -->
      <template v-if="auth.role === 'DUAL'">
        <router-link class="nav-item" to="/app/dual">📌 Dual Dashboard</router-link>
        <router-link class="nav-item" to="/app/catalog">🛒 {{ $t("nav.catalog") }}</router-link>
        <router-link class="nav-item" to="/app/cart">🧺 {{ $t("nav.cart") }}</router-link>
        <router-link class="nav-item" to="/app/orders">📦 {{ $t("nav.orders") }}</router-link>
        <router-link class="nav-item" to="/app/declarations">♻️ {{ $t("nav.declarations") }}</router-link>
      </template>

      <!-- Admin -->
      <template v-if="auth.role === 'ADMIN' || auth.role === 'SUPERADMIN'">
        <router-link class="nav-item" to="/app/admin">🗺️ Admin Dashboard</router-link>
        <router-link class="nav-item" to="/app/admin/declarations">♻️ Déclarations</router-link>
        <router-link class="nav-item" to="/app/admin/products">📦 Produits</router-link>
        <router-link class="nav-item" to="/app/admin/orders">🧾 Commandes</router-link>
        <router-link class="nav-item" to="/app/admin/users">👥 Gestion des utilisateurs</router-link>
      </template>
    </div>

    
  </aside>
</template>

<script setup>
import { useAuthStore } from "../../store/auth";

const auth = useAuthStore();
</script>

<style scoped>
.nav-item {
  display: block;
  padding: 10px 12px;
  border-radius: 14px;
  font-size: 14px;
  color: #1f2937;
  transition: all 0.2s ease;
}
.nav-item:hover {
  background: rgba(46, 204, 113, 0.12);
}
.router-link-active {
  background: rgba(46, 204, 113, 0.2);
  font-weight: 600;
}
</style>
