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

          <!-- Dashboard -->
          <router-link class="nav-item" to="/app/beneficiary">
            <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300" :class="{ 'flex-row-reverse': isRTL }">
              <div class="w-10 h-10 rounded-lg bg-gradient-to-r from-agri-green/30 to-agri-blue/30 border border-white/20 flex items-center justify-center flex-shrink-0">
                <span class="text-white text-xl">📌</span>
              </div>
              <div class="min-w-0 flex-1">
                <div class="text-white font-medium truncate">{{ isRTL ? 'لوحة القيادة' : 'Dashboard' }}</div>
                <div class="text-xs text-white/60 truncate">{{ isRTL ? 'نظرة عامة' : 'Vue d\'ensemble' }}</div>
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
                <div class="text-xs text-white/60 truncate">{{ isRTL ? 'سلتك' : 'Votre panier' }}</div>
              </div>
            </div>
          </router-link>

          <!-- Mes commandes (actif) -->
          <router-link class="nav-item" to="/app/orders">
            <div class="flex items-center gap-3 p-3 rounded-xl bg-blue-500/30 border border-blue-400/30" :class="{ 'flex-row-reverse': isRTL }">
              <div class="w-10 h-10 rounded-lg bg-blue-500/40 border border-blue-400/30 flex items-center justify-center flex-shrink-0">
                <span class="text-blue-200 text-xl">📦</span>
              </div>
              <div class="min-w-0 flex-1">
                <div class="text-white font-medium truncate">{{ isRTL ? 'طلباتي' : 'Mes commandes' }}</div>
                <div class="text-xs text-white/80 truncate">{{ isRTL ? 'تاريخ الطلبات' : 'Historique' }}</div>
              </div>
            </div>
          </router-link>

          <!-- Profil -->
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
      <main>
        <div class="space-y-6">
          <!-- Header -->
          <div class="mb-8">
            <div class="flex items-center justify-between mb-6 flex-wrap gap-4" :class="{ 'flex-row-reverse': isRTL }">
              <div class="flex items-center gap-4" :class="{ 'flex-row-reverse': isRTL }">
                <div class="p-3 bg-white/20 backdrop-blur-sm rounded-xl border border-white/30 flex-shrink-0">
                  <span class="text-2xl text-white">📦</span>
                </div>
                <div>
                  <h1 class="text-3xl md:text-4xl font-bold text-white">
                    {{ isRTL ? 'طلباتي' : 'Mes Commandes' }}
                  </h1>
                  <p class="text-white/90 mt-2">
                    {{ isRTL ? 'متابعة حالات الطلبات' : 'Suivi des statuts' }}
                  </p>
                </div>
              </div>

              <div class="flex items-center gap-3" :class="{ 'flex-row-reverse': isRTL }">
                <!-- Bouton Panier -->
                <router-link
                  to="/app/cart"
                  class="px-4 py-2 border border-white/20 rounded-lg text-sm font-medium text-white/80 hover:bg-white/10 transition-all flex items-center gap-2"
                  :class="{ 'flex-row-reverse': isRTL }"
                >
                  <span>🧺</span>
                  <span>{{ isRTL ? 'السلة' : 'Panier' }}</span>
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
            <h3 class="text-xl font-semibold text-white mb-2">{{ isRTL ? 'جاري تحميل الطلبات' : 'Chargement des commandes' }}</h3>
          </div>

          <!-- Error State -->
          <div v-if="error" class="agri-card p-6 bg-gradient-to-r from-red-500/10 to-red-500/5 border border-red-500/20">
            <div class="flex items-center gap-4" :class="{ 'flex-row-reverse': isRTL }">
              <div class="p-2 bg-red-500/20 rounded-lg flex-shrink-0">
                <span class="text-red-300 text-xl">❌</span>
              </div>
              <div class="flex-1">
                <h4 class="font-medium text-red-200">{{ isRTL ? 'خطأ' : 'Erreur' }}</h4>
                <p class="text-sm text-red-200/90 mt-1">{{ error }}</p>
              </div>
              <button @click="load" class="px-4 py-2 bg-red-500/20 hover:bg-red-500/30 text-red-300 rounded-lg transition-colors">
                {{ isRTL ? 'إعادة المحاولة' : 'Réessayer' }}
              </button>
            </div>
          </div>

          <!-- Liste des commandes -->
          <div v-if="orders.length && !loading" class="grid md:grid-cols-2 gap-6">
            <div
              v-for="o in orders"
              :key="o.id"
              class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20 hover:border-white/40"
            >
              <!-- En-tête commande -->
              <div class="flex items-start justify-between gap-3 mb-4" :class="{ 'flex-row-reverse': isRTL }">
                <div class="flex items-center gap-3">
                  <div class="p-2 bg-gradient-to-r from-blue-500/20 to-blue-400/20 rounded-lg">
                    <span class="text-blue-300 text-xl">📦</span>
                  </div>
                  <div>
                    <div class="font-semibold text-white text-lg">{{ isRTL ? 'طلب' : 'Order' }} #{{ o.id }}</div>
                    <div class="text-xs text-white/60 mt-1">{{ fmt(o.created_at) }}</div>
                  </div>
                </div>
                <span :class="getOrderStatusBadgeClass(o.status)" class="px-3 py-1 rounded-full text-xs font-medium">
                  {{ getOrderStatusLabel(o.status) }}
                </span>
              </div>

              <!-- Total -->
              <div class="mb-4 p-3 bg-white/5 rounded-xl border border-white/10">
                <div class="flex justify-between items-center" :class="{ 'flex-row-reverse': isRTL }">
                  <span class="text-white/70">{{ isRTL ? 'المجموع' : 'Total' }}</span>
                  <span class="text-xl font-bold text-white">{{ money(o.total_amount) }}</span>
                </div>
              </div>

              <!-- Articles -->
              <div v-if="o.items?.length" class="space-y-2">
                <div class="text-xs font-medium text-white/60 mb-2">
                  {{ isRTL ? 'المنتجات' : 'Articles' }}:
                </div>
                <div
                  v-for="it in o.items"
                  :key="it.id"
                  class="flex justify-between items-center text-sm p-2 bg-white/5 rounded-lg border border-white/10"
                  :class="{ 'flex-row-reverse': isRTL }"
                >
                  <span class="text-white/80">
                    {{ it.product_name || it.product?.name || (isRTL ? 'منتج' : 'Produit') }} 
                    <span class="text-white/60">× {{ it.qty }}</span>
                  </span>
                  <span class="font-medium text-white">{{ money(Number(it.unit_price) * Number(it.qty)) }}</span>
                </div>
              </div>

              <!-- Pied de carte -->
              <div class="mt-4 pt-3 border-t border-white/10 flex items-center justify-between text-xs text-white/40" :class="{ 'flex-row-reverse': isRTL }">
                <span>{{ isRTL ? 'تم الإنشاء' : 'Créé' }}: {{ fmt(o.created_at) }}</span>
                <span class="px-2 py-1 bg-white/5 rounded-full">{{ o.items?.length || 0 }} {{ isRTL ? 'منتج' : 'article' }}{{ o.items?.length > 1 ? 's' : '' }}</span>
              </div>
            </div>
          </div>

          <!-- Empty State -->
          <div
            v-else-if="!loading && !error && orders.length === 0"
            class="agri-card p-12 text-center bg-white/10 backdrop-blur-lg border border-white/20"
          >
            <div class="text-6xl mb-6 opacity-50">📦</div>
            <h3 class="text-2xl font-bold text-white mb-3">
              {{ isRTL ? 'لا توجد طلبات' : 'Aucune commande' }}
            </h3>
            <p class="text-white/80 mb-8 max-w-md mx-auto">
              {{ isRTL ? 'ستظهر طلباتك هنا.' : 'Tes commandes apparaîtront ici.' }}
            </p>
            <router-link
              to="/app/catalog"
              class="inline-block px-6 py-3 bg-gradient-to-r from-agri-green to-agri-green-dark text-white rounded-xl font-medium shadow-lg shadow-agri-green/20 hover:shadow-xl transition-all"
            >
              {{ isRTL ? 'الذهاب إلى الكتالوج' : 'Aller au catalogue' }}
            </router-link>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from "vue";
import { useAuthStore } from "../../store/auth";
import { useI18n } from "vue-i18n";
import { getMyOrders } from "../../api/exports";

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

const loading = ref(false);
const error = ref("");
const orders = ref([]);

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

async function load() {
  loading.value = true;
  error.value = "";
  try {
    const res = await getMyOrders();
    orders.value = (res.data || [])
      .filter((o) => o.status !== "CART")
      .sort((a, b) => (b.id || 0) - (a.id || 0));
  } catch (e) {
    error.value = isRTL.value ? "تعذر تحميل الطلبات." : "Impossible de charger les commandes.";
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
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

  load();
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

  .md\:grid-cols-2 {
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

/* Animation différée */
.agri-card:nth-child(2) {
  animation-delay: 0.1s;
}
.agri-card:nth-child(3) {
  animation-delay: 0.2s;
}
.agri-card:nth-child(4) {
  animation-delay: 0.3s;
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

.hover\:from-agri-green-dark:hover {
  --tw-gradient-from: #2f855a;
}

.hover\:to-agri-green:hover {
  --tw-gradient-to: #48bb78;
}

.shadow-agri-green\/20 {
  box-shadow: 0 4px 15px rgba(72, 187, 120, 0.2);
}
</style>