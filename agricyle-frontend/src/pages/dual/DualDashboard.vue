<template>
  <div class="relative min-h-screen" :dir="lang">
    <!-- Image d'arrière-plan fixe -->
    <div
      class="fixed inset-0 bg-cover bg-center bg-no-repeat"
      style="background-image: url('https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80')"
    >
      <div class="absolute inset-0 bg-black/40"></div>
    </div>

    <!-- Contenu -->
    <div class="relative z-10">
      <!-- SIDEBAR -->
      <aside :class="sidebarClasses">
        <div class="agri-card p-4 mb-4 bg-white/10 backdrop-blur-lg border border-white/20">
          <div class="flex items-center gap-3" :class="{ 'flex-row-reverse': isRTL }">
            <div class="w-12 h-12 rounded-xl2 bg-gradient-to-r from-agri-green/30 to-agri-blue/30 border border-white/20 flex items-center justify-center shadow-lg flex-shrink-0">
              <span class="text-2xl text-white">👥</span>
            </div>
            <div class="min-w-0 flex-1">
              <div class="font-semibold text-white truncate">{{ isRTL ? 'مزدوج' : 'Dual' }}</div>
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

          <!-- Dashboard Dual (actif) -->
          <router-link class="nav-item" to="/app/dual">
            <div class="flex items-center gap-3 p-3 rounded-xl transition-all duration-300" 
                 :class="{ 
                   'flex-row-reverse': isRTL,
                   'bg-indigo-500/30 border border-indigo-400/30': $route.path === '/app/dual',
                   'hover:bg-white/10': $route.path !== '/app/dual'
                 }">
              <div class="w-10 h-10 rounded-lg bg-gradient-to-r from-agri-green/30 to-agri-blue/30 border border-white/20 flex items-center justify-center flex-shrink-0">
                <span class="text-white text-xl">📌</span>
              </div>
              <div class="min-w-0 flex-1">
                <div class="text-white font-medium truncate">{{ isRTL ? 'لوحة القيادة' : 'Dashboard' }}</div>
                <div class="text-xs text-white/80 truncate">{{ isRTL ? 'نظرة عامة' : 'Vue d\'ensemble' }}</div>
              </div>
            </div>
          </router-link>

          <!-- SECTION FARMER (avec style distinct) -->
          <div class="pt-2">
            <div class="text-xs font-semibold text-emerald-300/80 px-2 mb-1 flex items-center gap-1" :class="{ 'flex-row-reverse': isRTL }">
              <span>👨‍🌾</span>
              <span>{{ isRTL ? 'قسم المزارع' : 'SECTION FARMER' }}</span>
            </div>
            
            <!-- Mes Déclarations -->
            <router-link class="nav-item" to="/app/dual/declarations">
              <div class="flex items-center gap-3 p-3 rounded-xl transition-all duration-300" 
                   :class="{ 
                     'flex-row-reverse': isRTL,
                     'bg-emerald-500/30 border border-emerald-400/30': $route.path === '/app/dual/declarations',
                     'hover:bg-white/10': $route.path !== '/app/dual/declarations'
                   }">
                <div class="w-10 h-10 rounded-lg bg-emerald-500/30 border border-emerald-400/20 flex items-center justify-center flex-shrink-0">
                  <span class="text-emerald-300 text-xl">♻️</span>
                </div>
                <div class="min-w-0 flex-1">
                  <div class="text-white font-medium truncate">{{ isRTL ? 'تصاريحي' : 'Mes Déclarations' }}</div>
                  <div class="text-xs text-white/60 truncate">{{ isRTL ? 'إدارة التصاريح' : 'Gérer mes déclarations' }}</div>
                </div>
              </div>
            </router-link>
          </div>

          <!-- SECTION BENEFICIARY (avec style distinct) -->
          <div class="pt-2">
            <div class="text-xs font-semibold text-purple-300/80 px-2 mb-1 flex items-center gap-1" :class="{ 'flex-row-reverse': isRTL }">
              <span>👤</span>
              <span>{{ isRTL ? 'قسم المستفيد' : 'SECTION BENEFICIAIRE' }}</span>
            </div>

            <!-- Catalogue -->
            <router-link class="nav-item" to="/app/catalog">
              <div class="flex items-center gap-3 p-3 rounded-xl transition-all duration-300" 
                   :class="{ 
                     'flex-row-reverse': isRTL,
                     'bg-purple-500/30 border border-purple-400/30': $route.path === '/app/catalog',
                     'hover:bg-white/10': $route.path !== '/app/catalog'
                   }">
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
              <div class="flex items-center gap-3 p-3 rounded-xl transition-all duration-300" 
                   :class="{ 
                     'flex-row-reverse': isRTL,
                     'bg-amber-500/30 border border-amber-400/30': $route.path === '/app/cart',
                     'hover:bg-white/10': $route.path !== '/app/cart'
                   }">
                <div class="w-10 h-10 rounded-lg bg-amber-500/30 border border-amber-400/20 flex items-center justify-center flex-shrink-0">
                  <span class="text-amber-300 text-xl">🧺</span>
                </div>
                <div class="min-w-0 flex-1">
                  <div class="text-white font-medium truncate">{{ isRTL ? 'السلة' : 'Panier' }}</div>
                  <div class="text-xs text-white/60 truncate">{{ isRTL ? 'سلتك' : 'Votre panier' }}</div>
                </div>
              </div>
            </router-link>

            <!-- Mes commandes -->
            <router-link class="nav-item" to="/app/orders">
              <div class="flex items-center gap-3 p-3 rounded-xl transition-all duration-300" 
                   :class="{ 
                     'flex-row-reverse': isRTL,
                     'bg-blue-500/30 border border-blue-400/30': $route.path === '/app/orders',
                     'hover:bg-white/10': $route.path !== '/app/orders'
                   }">
                <div class="w-10 h-10 rounded-lg bg-blue-500/30 border border-blue-400/20 flex items-center justify-center flex-shrink-0">
                  <span class="text-blue-300 text-xl">📦</span>
                </div>
                <div class="min-w-0 flex-1">
                  <div class="text-white font-medium truncate">{{ isRTL ? 'طلباتي' : 'Mes commandes' }}</div>
                  <div class="text-xs text-white/60 truncate">{{ isRTL ? 'تاريخ الطلبات' : 'Historique' }}</div>
                </div>
              </div>
            </router-link>
          </div>

          <!-- Profil -->
          <div class="pt-2 mt-2 border-t border-white/10">
            <router-link class="nav-item" to="/app/profile">
              <div class="flex items-center gap-3 p-3 rounded-xl transition-all duration-300" 
                   :class="{ 
                     'flex-row-reverse': isRTL,
                     'bg-indigo-500/30 border border-indigo-400/30': $route.path === '/app/profile',
                     'hover:bg-white/10': $route.path !== '/app/profile'
                   }">
                <div class="w-10 h-10 rounded-lg bg-indigo-500/30 border border-indigo-400/20 flex items-center justify-center flex-shrink-0">
                  <span class="text-indigo-300 text-xl">👤</span>
                </div>
                <div class="min-w-0 flex-1">
                  <div class="text-white font-medium truncate">{{ isRTL ? 'الملف الشخصي' : 'Profil' }}</div>
                  <div class="text-xs text-white/80 truncate">{{ isRTL ? 'معلوماتي' : 'Mes informations' }}</div>
                </div>
              </div>
            </router-link>
          </div>
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
                  <span class="text-2xl text-white">👥</span>
                </div>
                <div>
                  <h1 class="text-3xl md:text-4xl font-bold text-white">
                    {{ isRTL ? 'لوحة قيادة مزدوج' : 'Dashboard Dual' }}
                  </h1>
                  <p class="text-white/90 mt-2">
                    {{ isRTL ? 'مزارع ومستفيد في نفس الوقت' : 'Agriculteur et Bénéficiaire' }}
                  </p>
                </div>
              </div>

              <div class="px-4 py-2 bg-white/10 backdrop-blur-sm rounded-full border border-white/20">
                <span class="text-sm text-white/80">
                  {{ isRTL ? 'متصل:' : 'Connecté:' }} {{ auth.user?.username }}
                </span>
              </div>
            </div>
          </div>

          <!-- Statistiques globales -->
          <div class="grid lg:grid-cols-4 gap-6">
            <!-- Stats Farmer -->
            <div class="agri-card p-6 border-l-4 border-l-emerald-500">
              <div class="flex items-center gap-3 mb-2">
                <div class="p-2 bg-emerald-500/20 rounded-lg">
                  <span class="text-emerald-300 text-xl">👨‍🌾</span>
                </div>
                <span class="text-white/60 text-sm">{{ isRTL ? 'تصاريح المزارع' : 'Déclarations Farmer' }}</span>
              </div>
              <div class="text-3xl font-bold text-white">{{ stats.declarations }}</div>
            </div>

            <!-- Stats Beneficiary - Produits -->
            <div class="agri-card p-6 border-l-4 border-l-purple-500">
              <div class="flex items-center gap-3 mb-2">
                <div class="p-2 bg-purple-500/20 rounded-lg">
                  <span class="text-purple-300 text-xl">🛒</span>
                </div>
                <span class="text-white/60 text-sm">{{ isRTL ? 'منتجات' : 'Produits' }}</span>
              </div>
              <div class="text-3xl font-bold text-white">{{ stats.products }}</div>
            </div>

            <!-- Stats Beneficiary - Panier -->
            <div class="agri-card p-6 border-l-4 border-l-amber-500">
              <div class="flex items-center gap-3 mb-2">
                <div class="p-2 bg-amber-500/20 rounded-lg">
                  <span class="text-amber-300 text-xl">🧺</span>
                </div>
                <span class="text-white/60 text-sm">{{ isRTL ? 'السلة' : 'Panier' }}</span>
              </div>
              <div class="text-3xl font-bold text-white">{{ stats.cartItems }}</div>
              <div class="text-sm text-white/80 mt-2">{{ money(stats.cartTotal) }}</div>
            </div>

            <!-- Stats Beneficiary - Commandes -->
            <div class="agri-card p-6 border-l-4 border-l-blue-500">
              <div class="flex items-center gap-3 mb-2">
                <div class="p-2 bg-blue-500/20 rounded-lg">
                  <span class="text-blue-300 text-xl">📦</span>
                </div>
                <span class="text-white/60 text-sm">{{ isRTL ? 'طلبات' : 'Commandes' }}</span>
              </div>
              <div class="text-3xl font-bold text-white">{{ stats.orders }}</div>
            </div>
          </div>

          <!-- Deux sections clairement séparées -->
          <div class="grid lg:grid-cols-2 gap-6 mt-6">
            <!-- Section Farmer (style distinct) -->
            <div class="agri-card p-6 relative overflow-hidden">
              <!-- Badge de section -->
              <div class="absolute top-0 right-0 bg-emerald-500/20 px-3 py-1 rounded-bl-lg text-emerald-300 text-xs font-semibold">
                👨‍🌾 FARMER
              </div>
              
              <div class="flex items-center gap-3 mb-6">
                <div class="p-2 bg-gradient-to-r from-emerald-500/20 to-emerald-400/20 rounded-lg">
                  <span class="text-emerald-300 text-xl">👨‍🌾</span>
                </div>
                <h2 class="text-xl font-semibold text-white">{{ isRTL ? 'نشاط المزارع' : 'Activité Farmer' }}</h2>
              </div>

              <router-link 
                to="/app/dual/declarations" 
                class="block mb-4 p-3 bg-emerald-500/10 hover:bg-emerald-500/20 rounded-xl text-center transition-all border border-emerald-500/20"
              >
                <span class="text-emerald-300">📋 {{ isRTL ? 'إدارة التصاريح' : 'Gérer mes déclarations' }}</span>
              </router-link>

              <div v-if="recentDeclarations.length" class="space-y-3">
                <div v-for="d in recentDeclarations" :key="d.id" class="flex justify-between p-3 bg-white/5 rounded-lg">
                  <div>
                    <div class="text-white">{{ d.packaging_type }}</div>
                    <div class="text-xs text-white/60">{{ isRTL ? 'الكمية' : 'Qté' }}: {{ d.quantity }}</div>
                  </div>
                  <span :class="getStatusBadgeClass(d.status)" class="px-2 py-1 rounded-full text-xs">
                    {{ getStatusLabel(d.status) }}
                  </span>
                </div>
                <div v-if="!recentDeclarations.length" class="text-center text-white/60 py-4">
                  {{ isRTL ? 'لا توجد تصاريح حديثة' : 'Aucune déclaration récente' }}
                </div>
              </div>
            </div>

            <!-- Section Beneficiary (style distinct) -->
            <div class="agri-card p-6 relative overflow-hidden">
              <!-- Badge de section -->
              <div class="absolute top-0 right-0 bg-purple-500/20 px-3 py-1 rounded-bl-lg text-purple-300 text-xs font-semibold">
                👤 BENEFICIAIRE
              </div>
              
              <div class="flex items-center gap-3 mb-6">
                <div class="p-2 bg-gradient-to-r from-purple-500/20 to-purple-400/20 rounded-lg">
                  <span class="text-purple-300 text-xl">👤</span>
                </div>
                <h2 class="text-xl font-semibold text-white">{{ isRTL ? 'نشاط المستفيد' : 'Activité Beneficiaire' }}</h2>
              </div>

              <!-- Liens rapides bénéficiaire -->
              <div class="grid grid-cols-3 gap-2 mb-4">
                <router-link to="/app/catalog" class="p-2 bg-purple-500/20 hover:bg-purple-500/30 rounded-lg text-center text-purple-200 text-sm transition-all">
                  <div>🛒</div>
                  <div class="text-xs">{{ isRTL ? 'الكتالوج' : 'Catalogue' }}</div>
                </router-link>
                <router-link to="/app/cart" class="p-2 bg-amber-500/20 hover:bg-amber-500/30 rounded-lg text-center text-amber-200 text-sm transition-all">
                  <div>🧺</div>
                  <div class="text-xs">{{ isRTL ? 'السلة' : 'Panier' }}</div>
                </router-link>
                <router-link to="/app/orders" class="p-2 bg-blue-500/20 hover:bg-blue-500/30 rounded-lg text-center text-blue-200 text-sm transition-all">
                  <div>📦</div>
                  <div class="text-xs">{{ isRTL ? 'الطلبات' : 'Commandes' }}</div>
                </router-link>
              </div>

              <!-- Top produits -->
              <div v-if="topProducts.length" class="space-y-2 mb-4">
                <h3 class="text-white/80 text-sm mb-2 flex items-center gap-1">
                  <span>⭐</span> {{ isRTL ? 'أفضل المنتجات' : 'Top produits' }}
                </h3>
                <div v-for="p in topProducts" :key="p.id" class="flex justify-between p-2 bg-white/5 rounded-lg">
                  <span class="text-white text-sm">{{ p.name }}</span>
                  <span class="text-white font-semibold">{{ money(p.price) }}</span>
                </div>
              </div>

              <!-- Dernières commandes -->
              <div v-if="recentOrders.length">
                <h3 class="text-white/80 text-sm mb-2 flex items-center gap-1">
                  <span>📦</span> {{ isRTL ? 'آخر الطلبات' : 'Dernières commandes' }}
                </h3>
                <div v-for="o in recentOrders" :key="o.id" class="flex justify-between p-2 bg-white/5 rounded-lg mb-2">
                  <span class="text-white text-sm">#{{ o.id }}</span>
                  <span :class="getOrderStatusBadgeClass(o.status)" class="px-2 py-0.5 rounded-full text-xs">
                    {{ getOrderStatusLabel(o.status) }}
                  </span>
                </div>
              </div>

              <div v-if="!topProducts.length && !recentOrders.length" class="text-center text-white/60 py-4">
                {{ isRTL ? 'لا يوجد نشاط' : 'Aucune activité' }}
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from "vue";
import { useRoute } from "vue-router";
import { useAuthStore } from "../../store/auth";
import { useI18n } from "vue-i18n";
import { getMyDeclarations, getProducts, getMyCart, getMyOrders } from "../../api/exports";

const route = useRoute();
const auth = useAuthStore();
const { locale } = useI18n();

const lang = ref('fr');
const isRTL = computed(() => lang.value === 'ar');

// Sidebar classes
const sidebarClasses = computed(() => {
  const base = ['fixed', 'top-0', 'h-full', 'w-72', 'flex', 'flex-col', 'p-4', 'bg-black/40', 'backdrop-blur-xl', 'border-white/20', 'transition-all', 'duration-500', 'z-40', 'hidden', 'lg:flex'];
  return isRTL.value ? [...base, 'right-0', 'border-l'] : [...base, 'left-0', 'border-r'];
});

// Content classes
const contentContainerClasses = computed(() => {
  const base = ['transition-all', 'duration-500', 'pt-20', 'px-4', 'md:px-6', 'lg:px-8', 'pb-10'];
  return isRTL.value ? [...base, 'lg:mr-72'] : [...base, 'lg:ml-72'];
});

// Données
const declarations = ref([]);
const products = ref([]);
const cart = ref(null);
const orders = ref([]);

const stats = ref({ 
  declarations: 0, 
  products: 0, 
  cartItems: 0, 
  cartTotal: 0, 
  orders: 0 
});

// Utilitaires
function money(v) {
  return new Intl.NumberFormat(lang.value === 'ar' ? 'ar-TN' : 'fr-TN', {
    style: 'currency', 
    currency: 'TND',
    minimumFractionDigits: 3,
    maximumFractionDigits: 3
  }).format(Number(v || 0));
}

// Statuts déclarations
function getStatusLabel(s) {
  const labels = { 
    'PENDING': isRTL.value ? 'قيد الانتظار' : 'En attente', 
    'CONFIRMED': isRTL.value ? 'مؤكد' : 'Confirmé', 
    'COLLECTED': isRTL.value ? 'تم التجميع' : 'Collecté', 
    'CANCELLED': isRTL.value ? 'ملغي' : 'Annulé' 
  };
  return labels[s] || s;
}

function getStatusBadgeClass(s) {
  const classes = { 
    'PENDING': 'bg-yellow-500/20 text-yellow-200', 
    'CONFIRMED': 'bg-green-500/20 text-green-200', 
    'COLLECTED': 'bg-blue-500/20 text-blue-200', 
    'CANCELLED': 'bg-red-500/20 text-red-200' 
  };
  return classes[s] || 'bg-gray-500/20 text-gray-200';
}

// Statuts commandes
function getOrderStatusLabel(s) {
  const labels = { 
    'PENDING': isRTL.value ? 'قيد الانتظار' : 'En attente', 
    'CONFIRMED': isRTL.value ? 'مؤكد' : 'Confirmé', 
    'PROCESSING': isRTL.value ? 'قيد المعالجة' : 'En traitement', 
    'SHIPPED': isRTL.value ? 'تم الشحن' : 'Expédié', 
    'DELIVERED': isRTL.value ? 'تم التسليم' : 'Livré', 
    'CANCELLED': isRTL.value ? 'ملغي' : 'Annulé' 
  };
  return labels[s] || s;
}

function getOrderStatusBadgeClass(s) {
  const classes = { 
    'PENDING': 'bg-yellow-500/20 text-yellow-200', 
    'CONFIRMED': 'bg-green-500/20 text-green-200', 
    'PROCESSING': 'bg-blue-500/20 text-blue-200', 
    'SHIPPED': 'bg-purple-500/20 text-purple-200', 
    'DELIVERED': 'bg-emerald-500/20 text-emerald-200', 
    'CANCELLED': 'bg-red-500/20 text-red-200' 
  };
  return classes[s] || 'bg-gray-500/20 text-gray-200';
}

// Computed
const recentDeclarations = computed(() => declarations.value.slice(0, 3));
const topProducts = computed(() => 
  products.value
    .filter(p => p.is_active && p.stock > 0)
    .sort((a, b) => b.stock - a.stock)
    .slice(0, 3)
);
const recentOrders = computed(() => 
  orders.value
    .filter(o => o.status !== "CART")
    .sort((a, b) => b.id - a.id)
    .slice(0, 3)
);

// Chargement
async function loadData() {
  try {
    const [dRes, pRes, cRes, oRes] = await Promise.all([
      getMyDeclarations(), 
      getProducts(), 
      getMyCart(), 
      getMyOrders()
    ]);
    
    declarations.value = dRes.data || [];
    products.value = pRes.data || [];
    cart.value = cRes.data;
    orders.value = oRes.data || [];

    stats.value = {
      declarations: declarations.value.length,
      products: products.value.filter(p => p.is_active && p.stock > 0).length,
      cartItems: cart.value?.items?.reduce((s, it) => s + (it.qty || 0), 0) || 0,
      cartTotal: Number(cart.value?.total_amount || 0),
      orders: orders.value.filter(o => o.status !== "CART").length
    };
  } catch (error) {
    console.error("Erreur lors du chargement des données:", error);
  }
}

onMounted(() => {
  const savedLang = localStorage.getItem('lang') || 'fr';
  lang.value = savedLang;
  locale.value = savedLang;
  document.documentElement.dir = savedLang === 'ar' ? 'rtl' : 'ltr';
  loadData();
});
</script>

<style scoped>
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

.agri-card {
  background: rgba(255,255,255,0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,0.2);
  border-radius: 16px;
  transition: all 0.4s;
}

.agri-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 40px rgba(0,0,0,0.3);
  background: rgba(255,255,255,0.15);
}

/* Bordures colorées pour distinguer les sections */
.border-l-4 {
  border-left-width: 4px;
}

.border-l-emerald-500 {
  border-left-color: #10b981;
}

.border-l-purple-500 {
  border-left-color: #8b5cf6;
}

.border-l-amber-500 {
  border-left-color: #f59e0b;
}

.border-l-blue-500 {
  border-left-color: #3b82f6;
}

.nav-item {
  display: block;
  border-radius: 12px;
  transition: all 0.3s;
  text-decoration: none;
}

.nav-item:hover {
  background: rgba(255,255,255,0.15);
  transform: translateX(4px);
}

[dir="rtl"] .nav-item:hover { 
  transform: translateX(-4px); 
}

.text-white { 
  text-shadow: 0 1px 2px rgba(0,0,0,0.3); 
}

@media (max-width: 1024px) {
  aside { 
    display: none !important; 
  }
  .lg\:ml-72, .lg\:mr-72 { 
    margin: 0 !important; 
  }
}

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

[dir="rtl"] .flex { 
  flex-direction: row-reverse; 
}

/* Badge de section */
.absolute {
  position: absolute;
}

.top-0 {
  top: 0;
}

.right-0 {
  right: 0;
}

[dir="rtl"] .right-0 {
  right: auto;
  left: 0;
}

.rounded-bl-lg {
  border-bottom-left-radius: 0.5rem;
}

[dir="rtl"] .rounded-bl-lg {
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0.5rem;
}

/* Animation spin */
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.animate-spin {
  animation: spin 1s linear infinite;
}
</style>