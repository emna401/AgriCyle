<template>
  <div class="relative min-h-screen" :dir="lang">
    <!-- Image d'arrière-plan fixe -->
    <div
      class="fixed inset-0 bg-cover bg-center bg-no-repeat"
      style="background-image: url('https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80')"
    >
      <!-- Overlay sombre pour améliorer la lisibilité -->
      <div class="absolute inset-0 bg-black/40"></div>
    </div>

    <!-- Contenu par-dessus l'image -->
    <div class="relative z-10">
      <!-- SIDEBAR BENEFICIARY -->
      <aside :class="sidebarClasses">
        <div class="agri-card p-4 mb-4 bg-white/10 backdrop-blur-lg border border-white/20">
          <div class="flex items-center gap-3" :class="{ 'flex-row-reverse': isRTL }">
            <div class="w-12 h-12 rounded-xl2 bg-gradient-to-r from-agri-green/30 to-agri-blue/30 border border-white/20 flex items-center justify-center shadow-lg flex-shrink-0">
              <span class="text-2xl text-white">👤</span>
            </div>
            <div class="min-w-0 flex-1">
              <div class="font-semibold text-white truncate">{{ isRTL ? 'المستفيد' : 'Bénéficiaire' }}</div>
              <div v-if="auth.user" class="text-xs text-white/80 mt-1 truncate">
                {{ auth.user.username }} • {{ auth.user.role }}
              </div>
            </div>
          </div>
        </div>

        <div class="agri-card p-4 space-y-2 bg-white/10 backdrop-blur-lg border border-white/20 flex-1 overflow-y-auto">
          <div class="text-xs font-semibold text-white/60 px-2 mb-2">
            {{ isRTL ? 'القائمة الرئيسية' : 'MENU PRINCIPAL' }}
          </div>

          <!-- Dashboard (actif) -->
          <router-link class="nav-item" to="/app/beneficiary">
            <div class="flex items-center gap-3 p-3 rounded-xl bg-gradient-to-r from-agri-green/30 to-agri-blue/30 border border-white/30" :class="{ 'flex-row-reverse': isRTL }">
              <div class="w-10 h-10 rounded-lg bg-gradient-to-r from-agri-green/40 to-agri-blue/40 border border-white/30 flex items-center justify-center flex-shrink-0">
                <span class="text-white text-xl">📌</span>
              </div>
              <div class="min-w-0 flex-1">
                <div class="text-white font-medium truncate">{{ isRTL ? 'لوحة القيادة' : 'Dashboard' }}</div>
                <div class="text-xs text-white/80 truncate">{{ isRTL ? 'نظرة عامة' : 'Vue d\'ensemble' }}</div>
              </div>
            </div>
          </router-link>

          <!-- Catalogue -->
          <router-link class="nav-item" to="/app/catalog">
            <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300" :class="{ 'flex-row-reverse': isRTL }">
              <div class="w-10 h-10 rounded-lg bg-purple-500/30 border border-purple-400/20 flex items-center justify-center flex-shrink-0">
                <span class="text-purple-300 text-xl">🛒</span>
              </div>
              <div class="min-w-0 flex-1">
                <div class="text-white font-medium truncate">{{ isRTL ? 'الكتالوج' : 'Catalogue' }}</div>
                <div class="text-xs text-white/60 truncate">{{ isRTL ? 'تصفح المنتجات' : 'Parcourir les produits' }}</div>
              </div>
            </div>
          </router-link>

          <!-- Panier -->
          <router-link class="nav-item" to="/app/cart">
            <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300" :class="{ 'flex-row-reverse': isRTL }">
              <div class="w-10 h-10 rounded-lg bg-amber-500/30 border border-amber-400/20 flex items-center justify-center flex-shrink-0">
                <span class="text-amber-300 text-xl">🧺</span>
              </div>
              <div class="min-w-0 flex-1">
                <div class="text-white font-medium truncate">{{ isRTL ? 'السلة' : 'Panier' }}</div>
                <div class="text-xs text-white/60 truncate">
                  <span v-if="stats.cartItems > 0" class="bg-amber-500/30 px-1.5 py-0.5 rounded-full">
                    {{ stats.cartItems }}
                  </span>
                  <span v-else>{{ isRTL ? 'سلتك فارغة' : 'Votre panier' }}</span>
                </div>
              </div>
            </div>
          </router-link>

          <!-- Mes commandes -->
          <router-link class="nav-item" to="/app/orders">
            <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300" :class="{ 'flex-row-reverse': isRTL }">
              <div class="w-10 h-10 rounded-lg bg-blue-500/30 border border-blue-400/20 flex items-center justify-center flex-shrink-0">
                <span class="text-blue-300 text-xl">📦</span>
              </div>
              <div class="min-w-0 flex-1">
                <div class="text-white font-medium truncate">{{ isRTL ? 'طلباتي' : 'Mes commandes' }}</div>
                <div class="text-xs text-white/60 truncate">{{ isRTL ? 'تاريخ الطلبات' : 'Historique' }}</div>
              </div>
            </div>
          </router-link>

          <!-- Profil - CORRIGÉ: lien vers /app/profile -->
          <!-- Nouveau lien vers /app/profile -->
   <router-link class="nav-item" to="/app/profile">
  <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300" :class="{ 'flex-row-reverse': isRTL }">
    <div class="w-10 h-10 rounded-lg bg-indigo-500/30 border border-indigo-400/20 flex items-center justify-center flex-shrink-0">
      <span class="text-indigo-300 text-xl">👤</span>
    </div>
    <div class="min-w-0 flex-1">
      <div class="text-white font-medium truncate">{{ isRTL ? 'الملف الشخصي' : 'Profil' }}</div>
      <div class="text-xs text-white/60 truncate">{{ isRTL ? 'معلوماتي' : 'Mes informations' }}</div>
    </div>
  </div>
</router-link>
        </div>
      </aside>

      <!-- Main Content -->
      <main >
        <div class="space-y-6">
          <!-- Header -->
          <div class="mb-8">
            <div class="flex items-center justify-between mb-6 flex-wrap gap-4" :class="{ 'flex-row-reverse': isRTL }">
              <div class="flex items-center gap-4" :class="{ 'flex-row-reverse': isRTL }">
                <div class="p-3 bg-white/20 backdrop-blur-sm rounded-xl border border-white/30 flex-shrink-0">
                  <span class="text-2xl text-white">🏭</span>
                </div>
                <div>
                  <h1 class="text-3xl md:text-4xl font-bold text-white">
                    {{ isRTL ? 'لوحة قيادة المستفيد' : 'Beneficiary Dashboard' }}
                  </h1>
                  <p class="text-white/90 mt-2">
                    {{ isRTL ? 'الكتالوج، السلة والطلبات' : 'Catalogue, panier & commandes' }}
                  </p>
                </div>
              </div>

              <div class="flex items-center gap-3" :class="{ 'flex-row-reverse': isRTL }">
                <!-- Boutons rapides -->
                <router-link
                  to="/app/catalog"
                  class="px-4 py-2 bg-gradient-to-r from-agri-green to-agri-green-dark text-white rounded-xl font-medium shadow-lg shadow-agri-green/20 hover:shadow-xl transition-all flex items-center gap-2"
                  :class="{ 'flex-row-reverse': isRTL }"
                >
                  <span>🛒</span>
                  <span>{{ isRTL ? 'الكتالوج' : 'Catalogue' }}</span>
                </router-link>

                <router-link
                  to="/app/cart"
                  class="px-4 py-2 border border-white/20 rounded-lg text-sm font-medium text-white/80 hover:bg-white/10 transition-all flex items-center gap-2"
                  :class="{ 'flex-row-reverse': isRTL }"
                >
                  <span>🧺</span>
                  <span>{{ isRTL ? 'السلة' : 'Panier' }}</span>
                  <span v-if="stats.cartItems > 0" class="bg-amber-500/30 px-1.5 py-0.5 rounded-full text-xs">
                    {{ stats.cartItems }}
                  </span>
                </router-link>

                <div class="px-4 py-2 bg-white/10 backdrop-blur-sm rounded-full border border-white/20">
                  <span class="text-sm text-white/80">
                    {{ isRTL ? 'متصل:' : 'Connecté:' }} {{ auth.user?.username }}
                  </span>
                </div>
              </div>
            </div>
          </div>

          <!-- Loading State -->
          <div v-if="loading" class="agri-card p-12 text-center bg-white/10 backdrop-blur-lg border border-white/20">
            <div class="inline-block animate-spin text-4xl mb-4 text-white/80">⟳</div>
            <h3 class="text-xl font-semibold text-white mb-2">{{ isRTL ? 'جاري تحميل البيانات' : 'Chargement des données' }}</h3>
          </div>

          <!-- Cartes statistiques -->
          <div v-else class="grid lg:grid-cols-3 gap-6">
            <!-- Produits disponibles -->
            <div class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
              <div class="flex items-center gap-3 mb-4" :class="{ 'flex-row-reverse': isRTL }">
                <div class="p-2 bg-gradient-to-r from-emerald-500/20 to-emerald-400/20 rounded-lg">
                  <span class="text-emerald-300 text-xl">📦</span>
                </div>
                <div>
                  <h3 class="text-lg font-semibold text-white">{{ isRTL ? 'المنتجات' : 'Produits' }}</h3>
                  <p class="text-sm text-white/70">{{ isRTL ? 'المتاحة' : 'Disponibles' }}</p>
                </div>
              </div>

              <div class="text-4xl font-bold text-white">{{ stats.products }}</div>
              <div class="text-sm text-white/60 mt-2">{{ isRTL ? 'منتج نشط في المخزون' : 'Produits actifs en stock' }}</div>
            </div>

            <!-- Panier -->
            <div class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
              <div class="flex items-center gap-3 mb-4" :class="{ 'flex-row-reverse': isRTL }">
                <div class="p-2 bg-gradient-to-r from-amber-500/20 to-amber-400/20 rounded-lg">
                  <span class="text-amber-300 text-xl">🧺</span>
                </div>
                <div>
                  <h3 class="text-lg font-semibold text-white">{{ isRTL ? 'السلة' : 'Panier' }}</h3>
                  <p class="text-sm text-white/70">{{ isRTL ? 'قيد التقدم' : 'En cours' }}</p>
                </div>
              </div>

              <div class="text-4xl font-bold text-white">{{ stats.cartItems }}</div>
              <div class="text-sm text-white/60 mt-2">{{ isRTL ? 'عناصر في سلتك' : 'Articles dans ton panier' }}</div>
              
              <div class="mt-4 p-3 bg-white/5 rounded-xl border border-white/10">
                <div class="text-sm text-white/80 flex justify-between" :class="{ 'flex-row-reverse': isRTL }">
                  <span>{{ isRTL ? 'المجموع' : 'Total' }}:</span>
                  <span class="font-bold text-white">{{ money(stats.cartTotal) }}</span>
                </div>
              </div>
            </div>

            <!-- Commandes -->
            <div class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
              <div class="flex items-center gap-3 mb-4" :class="{ 'flex-row-reverse': isRTL }">
                <div class="p-2 bg-gradient-to-r from-blue-500/20 to-blue-400/20 rounded-lg">
                  <span class="text-blue-300 text-xl">📊</span>
                </div>
                <div>
                  <h3 class="text-lg font-semibold text-white">{{ isRTL ? 'الطلبات' : 'Commandes' }}</h3>
                  <p class="text-sm text-white/70">{{ isRTL ? 'السجل' : 'Historique' }}</p>
                </div>
              </div>

              <div class="text-4xl font-bold text-white">{{ stats.orders }}</div>
              <div class="text-sm text-white/60 mt-2">{{ isRTL ? 'طلبات سابقة' : 'Commandes passées' }}</div>
            </div>
          </div>

          <!-- Deuxième ligne : Produits phares et Dernières commandes -->
          <div class="grid lg:grid-cols-2 gap-6 mt-6">
            <!-- Produits phares -->
            <div class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
              <div class="flex items-center gap-3 mb-4" :class="{ 'flex-row-reverse': isRTL }">
                <div class="p-2 bg-gradient-to-r from-purple-500/20 to-purple-400/20 rounded-lg">
                  <span class="text-purple-300 text-xl">⭐</span>
                </div>
                <div>
                  <h3 class="text-lg font-semibold text-white">{{ isRTL ? 'منتجات مميزة' : 'Produits phares' }}</h3>
                  <p class="text-sm text-white/70">{{ isRTL ? 'أفضل المخزون / السعر' : 'Top stock / prix' }}</p>
                </div>
              </div>

              <div v-if="topProducts.length" class="space-y-3">
                <div
                  v-for="p in topProducts"
                  :key="p.id"
                  class="flex items-center justify-between p-3 bg-white/5 rounded-xl border border-white/10"
                  :class="{ 'flex-row-reverse': isRTL }"
                >
                  <div>
                    <div class="font-medium text-white">{{ p.name }}</div>
                    <div class="text-xs text-white/60 mt-1">
                      {{ p.category || (isRTL ? 'فئة' : 'Catégorie') }} • {{ isRTL ? 'المخزون' : 'stock' }} {{ p.stock }}
                    </div>
                  </div>
                  <div class="text-sm font-semibold text-white">{{ money(p.price) }}</div>
                </div>

                <router-link
                  to="/app/catalog"
                  class="block text-center text-sm text-emerald-300 hover:text-emerald-200 mt-2"
                >
                  {{ isRTL ? 'عرض الكل ←' : 'Voir tout →' }}
                </router-link>
              </div>

              <div v-else class="text-white/70 text-center py-4">
                {{ isRTL ? 'لا توجد منتجات.' : 'Aucun produit.' }}
              </div>
            </div>

            <!-- Dernières commandes -->
            <div class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
              <div class="flex items-center gap-3 mb-4" :class="{ 'flex-row-reverse': isRTL }">
                <div class="p-2 bg-gradient-to-r from-blue-500/20 to-blue-400/20 rounded-lg">
                  <span class="text-blue-300 text-xl">📦</span>
                </div>
                <div>
                  <h3 class="text-lg font-semibold text-white">{{ isRTL ? 'آخر الطلبات' : 'Dernières commandes' }}</h3>
                  <p class="text-sm text-white/70">{{ isRTL ? 'آخر حالة' : 'Dernier statut' }}</p>
                </div>
              </div>

              <div v-if="lastOrders.length" class="space-y-3">
                <div
                  v-for="o in lastOrders"
                  :key="o.id"
                  class="flex items-center justify-between p-3 bg-white/5 rounded-xl border border-white/10"
                  :class="{ 'flex-row-reverse': isRTL }"
                >
                  <div>
                    <div class="font-medium text-white">{{ isRTL ? 'طلب' : 'Order' }} #{{ o.id }}</div>
                    <div class="text-xs text-white/60 mt-1">{{ fmt(o.created_at) }}</div>
                  </div>
                  <span :class="getOrderStatusBadgeClass(o.status)" class="px-3 py-1 rounded-full text-xs font-medium">
                    {{ getOrderStatusLabel(o.status) }}
                  </span>
                </div>

                <router-link
                  to="/app/orders"
                  class="block text-center text-sm text-emerald-300 hover:text-emerald-200 mt-2"
                >
                  {{ isRTL ? 'عرض طلباتي ←' : 'Voir mes commandes →' }}
                </router-link>
              </div>

              <div v-else class="text-white/70 text-center py-4">
                {{ isRTL ? 'لا توجد طلبات.' : 'Aucune commande.' }}
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, reactive, ref } from "vue";
import { useAuthStore } from "../../store/auth";
import { useI18n } from "vue-i18n";
import { getProducts, getMyCart, getMyOrders } from "../../api/exports";

const auth = useAuthStore();
const { locale } = useI18n();

// Gestion de la langue
const lang = ref('fr');
const isRTL = computed(() => lang.value === 'ar');

// Classes du sidebar
const sidebarClasses = computed(() => {
  const baseClasses = [
    'fixed',
    'top-0',
    'h-full',
    'w-72',
    'flex',
    'flex-col',
    'p-4',
    'bg-black/40',
    'backdrop-blur-xl',
    'border-white/20',
    'transition-all',
    'duration-500',
    'ease-in-out',
    'z-40',
    'hidden',
    'lg:flex'
  ];

  if (lang.value === 'ar') {
    return [...baseClasses, 'right-0', 'border-l'];
  } else {
    return [...baseClasses, 'left-0', 'border-r'];
  }
});

// Classes du conteneur principal
const contentContainerClasses = computed(() => {
  const baseClasses = [
    'transition-all',
    'duration-500',
    'ease-in-out',
    'pt-20',
    'px-4',
    'md:px-6',
    'lg:px-8',
    'pb-10'
  ];

  if (lang.value === 'ar') {
    return [...baseClasses, 'lg:mr-72'];
  } else {
    return [...baseClasses, 'lg:ml-72'];
  }
});

const products = ref([]);
const cart = ref(null);
const orders = ref([]);
const loading = ref(true);

const stats = reactive({
  products: 0,
  cartItems: 0,
  cartTotal: 0,
  orders: 0
});

function money(v) {
  const n = Number(v || 0);
  return new Intl.NumberFormat(lang.value === 'ar' ? 'ar-TN' : 'fr-TN', {
    style: 'currency',
    currency: 'TND',
    minimumFractionDigits: 2
  }).format(n);
}

function fmt(d) {
  if (!d) return "-";
  try {
    return new Date(d).toLocaleDateString(lang.value === 'ar' ? 'ar-TN' : 'fr-FR', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  } catch {
    return String(d).replace("T", " ").slice(0, 16);
  }
}

function getOrderStatusLabel(status) {
  const labels = {
    'PENDING': isRTL.value ? 'قيد الانتظار' : 'En attente',
    'CONFIRMED': isRTL.value ? 'مؤكد' : 'Confirmé',
    'PROCESSING': isRTL.value ? 'قيد المعالجة' : 'En traitement',
    'SHIPPED': isRTL.value ? 'تم الشحن' : 'Expédié',
    'DELIVERED': isRTL.value ? 'تم التسليم' : 'Livré',
    'CANCELLED': isRTL.value ? 'ملغي' : 'Annulé',
    'CART': isRTL.value ? 'في السلة' : 'Dans le panier'
  };
  return labels[status] || status;
}

function getOrderStatusBadgeClass(status) {
  const classes = {
    'PENDING': 'bg-yellow-500/20 text-yellow-200 border border-yellow-400/20',
    'CONFIRMED': 'bg-green-500/20 text-green-200 border border-green-400/20',
    'PROCESSING': 'bg-blue-500/20 text-blue-200 border border-blue-400/20',
    'SHIPPED': 'bg-purple-500/20 text-purple-200 border border-purple-400/20',
    'DELIVERED': 'bg-emerald-500/20 text-emerald-200 border border-emerald-400/20',
    'CANCELLED': 'bg-red-500/20 text-red-200 border border-red-400/20',
    'CART': 'bg-amber-500/20 text-amber-200 border border-amber-400/20'
  };
  return classes[status] || 'bg-gray-500/20 text-gray-200 border border-gray-400/20';
}

const topProducts = computed(() =>
  products.value
    .filter((p) => p.is_active !== false && Number(p.stock) > 0)
    .slice()
    .sort((a, b) => Number(b.stock) - Number(a.stock))
    .slice(0, 5)
);

const lastOrders = computed(() =>
  orders.value
    .filter((o) => o.status !== "CART")
    .slice()
    .sort((a, b) => (b.id || 0) - (a.id || 0))
    .slice(0, 5)
);

function compute() {
  stats.products = products.value.filter((p) => p.is_active !== false && Number(p.stock) > 0).length;
  const items = cart.value?.items || [];
  stats.cartItems = items.reduce((s, it) => s + Number(it.qty || 0), 0);
  stats.cartTotal = Number(cart.value?.total_amount || 0);
  stats.orders = orders.value.filter((o) => o.status !== "CART").length;
}

onMounted(async () => {
  const savedLang = localStorage.getItem('lang') || 'fr';
  lang.value = savedLang;
  locale.value = savedLang;

  if (savedLang === 'ar') {
    document.documentElement.dir = 'rtl';
    document.documentElement.lang = 'ar';
  } else {
    document.documentElement.dir = 'ltr';
    document.documentElement.lang = 'fr';
  }

  try {
    const [p, c, o] = await Promise.all([
      getProducts(),
      getMyCart(),
      getMyOrders()
    ]);

    products.value = p.data || [];
    cart.value = c.data;
    orders.value = o.data || [];

    compute();
  } catch (error) {
    console.error("Erreur chargement données:", error);
  } finally {
    loading.value = false;
  }
});
</script>

<style scoped>
/* Styles généraux */
.min-h-screen {
  min-height: 100vh;
}

.fixed {
  position: fixed;
}

.inset-0 {
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}

/* Glassmorphism Card */
.agri-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.agri-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
  background: rgba(255, 255, 255, 0.15);
  border-color: rgba(255, 255, 255, 0.3);
}

/* Navigation sidebar */
.nav-item {
  display: block;
  border-radius: 12px;
  transition: all 0.3s ease;
  text-decoration: none;
}

.nav-item:hover {
  background: rgba(255, 255, 255, 0.15);
  transform: translateX(4px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

[dir="rtl"] .nav-item:hover {
  transform: translateX(-4px);
}

.router-link-active {
  background: linear-gradient(135deg, rgba(46, 204, 113, 0.3) 0%, rgba(52, 152, 219, 0.3) 100%);
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 4px 15px rgba(46, 204, 113, 0.2);
}

/* Effet de texte avec ombre */
.text-white {
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.font-bold {
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
}

/* Animation spin */
.animate-spin {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

/* Rounded corners */
.rounded-xl2 {
  border-radius: 14px;
}

/* Responsive */
@media (max-width: 1024px) {
  aside {
    display: none !important;
  }

  .lg\:ml-72, .lg\:mr-72 {
    margin-left: 0 !important;
    margin-right: 0 !important;
  }
}

@media (max-width: 768px) {
  .pt-20 {
    padding-top: 5rem;
  }

  .text-3xl, .text-4xl {
    font-size: 1.75rem;
  }

  .agri-card {
    padding: 1.25rem;
  }

  .lg\:grid-cols-2, .lg\:grid-cols-3 {
    grid-template-columns: 1fr;
  }
}

/* Animation d'entrée */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.agri-card {
  animation: fadeInUp 0.6s ease-out forwards;
  opacity: 0;
}

/* RTL Support */
[dir="rtl"] .flex {
  flex-direction: row-reverse;
}

[dir="rtl"] .gap-3, [dir="rtl"] .gap-4 {
  gap: 1rem;
}

/* Scrollbar personnalisée */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 4px;
}

::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.3);
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.4);
}

/* Classes de couleur personnalisées */
.bg-agri-green {
  background-color: #48bb78;
}

.bg-agri-green-dark {
  background-color: #2f855a;
}

.from-agri-green {
  --tw-gradient-from: #48bb78;
}

.to-agri-green-dark {
  --tw-gradient-to: #2f855a;
}
</style>