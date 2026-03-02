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

          <!-- Panier (actif) -->
          <router-link class="nav-item" to="/app/cart">
            <div class="flex items-center gap-3 p-3 rounded-xl bg-amber-500/30 border border-amber-400/30" :class="{ 'flex-row-reverse': isRTL }">
              <div class="w-10 h-10 rounded-lg bg-amber-500/40 border border-amber-400/30 flex items-center justify-center flex-shrink-0">
                <span class="text-amber-200 text-xl">🧺</span>
              </div>
              <div class="min-w-0 flex-1">
                <div class="text-white font-medium truncate">{{ isRTL ? 'السلة' : 'Panier' }}</div>
                <div class="text-xs text-white/80 truncate">
                  <span v-if="totalItems > 0" class="bg-amber-500/30 px-1.5 py-0.5 rounded-full">
                    {{ totalItems }}
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
      <main >
        <div class="space-y-6">
          <!-- Header -->
          <div class="mb-8">
            <div class="flex items-center justify-between mb-6 flex-wrap gap-4" :class="{ 'flex-row-reverse': isRTL }">
              <div class="flex items-center gap-4" :class="{ 'flex-row-reverse': isRTL }">
                <div class="p-3 bg-white/20 backdrop-blur-sm rounded-xl border border-white/30 flex-shrink-0">
                  <span class="text-2xl text-white">🧺</span>
                </div>
                <div>
                  <h1 class="text-3xl md:text-4xl font-bold text-white">
                    {{ isRTL ? 'سلة التسوق' : 'Panier' }}
                  </h1>
                  <p class="text-white/90 mt-2">
                    {{ isRTL ? 'أضف أو أزل المنتجات' : 'Ajoute / retire des produits' }}
                  </p>
                </div>
              </div>

              <div class="flex items-center gap-3" :class="{ 'flex-row-reverse': isRTL }">
                <!-- Bouton Catalogue -->
                <router-link
                  to="/app/catalog"
                  class="px-4 py-2 border border-white/20 rounded-lg text-sm font-medium text-white/80 hover:bg-white/10 transition-all flex items-center gap-2"
                  :class="{ 'flex-row-reverse': isRTL }"
                >
                  <span>←</span>
                  <span>{{ isRTL ? 'الكتالوج' : 'Catalogue' }}</span>
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
            <h3 class="text-xl font-semibold text-white mb-2">{{ isRTL ? 'جاري تحميل السلة' : 'Chargement du panier' }}</h3>
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

          <!-- Panier avec articles -->
          <div v-if="cart && cart.items && cart.items.length && !loading" class="grid lg:grid-cols-3 gap-6">
            <!-- Liste des articles -->
            <div class="lg:col-span-2 space-y-4">
              <div v-for="it in cart.items" :key="it.id" class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
                <!-- En-tête article -->
                <div class="flex items-start justify-between gap-3 mb-4" :class="{ 'flex-row-reverse': isRTL }">
                  <div>
                    <div class="font-semibold text-white text-lg">
                      {{ it.product_name || it.product?.name || (isRTL ? 'منتج' : 'Produit') }}
                    </div>
                    <div class="text-xs text-white/60 mt-1">
                      {{ isRTL ? 'السعر' : 'Prix' }}: {{ money(it.unit_price) }}
                    </div>
                  </div>

                  <button @click="remove(it)" class="text-sm text-red-300 hover:text-red-200 bg-red-500/10 hover:bg-red-500/20 px-3 py-1 rounded-full transition-colors">
                    {{ isRTL ? 'حذف' : 'Supprimer' }}
                  </button>
                </div>

                <!-- Contrôles de quantité -->
                <div class="flex items-center justify-between" :class="{ 'flex-row-reverse': isRTL }">
                  <div class="flex items-center gap-3">
                    <button 
                      @click="dec(it)" 
                      class="w-10 h-10 rounded-lg bg-white/10 border border-white/20 text-white hover:bg-white/20 transition-all text-xl font-bold"
                      :disabled="updating[it.id]"
                    >−</button>
                    <span class="font-semibold text-white text-lg min-w-[2rem] text-center">{{ it.qty }}</span>
                    <button 
                      @click="inc(it)" 
                      class="w-10 h-10 rounded-lg bg-white/10 border border-white/20 text-white hover:bg-white/20 transition-all text-xl font-bold"
                      :disabled="updating[it.id]"
                    >+</button>
                  </div>

                  <div class="text-lg font-bold text-white">
                    {{ money(Number(it.unit_price) * Number(it.qty)) }}
                  </div>
                </div>

                <!-- Indicateur de mise à jour -->
                <div v-if="updating[it.id]" class="text-xs text-amber-300 mt-2 text-center">
                  {{ isRTL ? 'جاري التحديث...' : 'Mise à jour...' }}
                </div>
              </div>
            </div>

            <!-- Résumé de la commande -->
            <div class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20 h-fit">
              <div class="flex items-center gap-3 mb-6" :class="{ 'flex-row-reverse': isRTL }">
                <div class="p-2 bg-gradient-to-r from-amber-500/20 to-amber-400/20 rounded-lg">
                  <span class="text-amber-300 text-xl">📌</span>
                </div>
                <div>
                  <h3 class="text-xl font-semibold text-white">{{ isRTL ? 'ملخص الطلب' : 'Résumé' }}</h3>
                  <p class="text-sm text-white/70">{{ isRTL ? 'قبل التأكيد' : 'Avant confirmation' }}</p>
                </div>
              </div>

              <!-- Détails -->
              <div class="space-y-4">
                <div class="flex justify-between text-white/80 py-2 border-b border-white/10" :class="{ 'flex-row-reverse': isRTL }">
                  <span>{{ isRTL ? 'المنتجات' : 'Articles' }}</span>
                  <span class="font-bold text-white">{{ totalItems }}</span>
                </div>
                
                <div class="flex justify-between text-white/80 py-2 border-b border-white/10" :class="{ 'flex-row-reverse': isRTL }">
                  <span>{{ isRTL ? 'المجموع' : 'Total' }}</span>
                  <span class="font-bold text-white text-xl">{{ money(cart.total_amount) }}</span>
                </div>

                <!-- Bouton de confirmation -->
                <button
                  @click="confirm"
                  :disabled="confirming"
                  class="w-full mt-4 px-4 py-3 bg-gradient-to-r from-agri-green to-agri-green-dark hover:from-agri-green-dark hover:to-agri-green text-white rounded-xl font-medium shadow-lg shadow-agri-green/20 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  <span class="flex items-center justify-center gap-2" :class="{ 'flex-row-reverse': isRTL }">
                    <span v-if="confirming" class="animate-spin">⟳</span>
                    <span v-else>✅</span>
                    {{ confirming ? (isRTL ? 'جاري...' : '...') : (isRTL ? 'تأكيد الطلب' : 'Confirmer commande') }}
                  </span>
                </button>

                <!-- Messages -->
                <div v-if="ok" class="p-3 bg-green-500/20 border border-green-400/30 rounded-lg">
                  <p class="text-sm text-green-200 text-center">{{ ok }}</p>
                </div>
                <div v-if="error2" class="p-3 bg-red-500/20 border border-red-400/30 rounded-lg">
                  <p class="text-sm text-red-200 text-center">{{ error2 }}</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Panier vide -->
          <div
            v-else-if="!loading && !error && (!cart || !cart.items || cart.items.length === 0)"
            class="agri-card p-12 text-center bg-white/10 backdrop-blur-lg border border-white/20"
          >
            <div class="text-6xl mb-6 opacity-50">🧺</div>
            <h3 class="text-2xl font-bold text-white mb-3">
              {{ isRTL ? 'السلة فارغة' : 'Panier vide' }}
            </h3>
            <p class="text-white/80 mb-8 max-w-md mx-auto">
              {{ isRTL ? 'أضف منتجات من الكتالوج.' : 'Ajoute des produits depuis le catalogue.' }}
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
import { computed, onMounted, reactive, ref } from "vue";
import { useAuthStore } from "../../store/auth";
import { useI18n } from "vue-i18n";
import { getMyCart, updateCartItem, removeCartItem, checkoutOrder } from "../../api/exports";

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

const cart = ref(null);
const loading = ref(false);
const confirming = ref(false);

const error = ref("");
const error2 = ref("");
const ok = ref("");

const updating = reactive({});

function money(v) {
  const n = Number(v || 0);
  return new Intl.NumberFormat(lang.value === 'ar' ? 'ar-TN' : 'fr-TN', {
    style: 'currency',
    currency: 'TND',
    minimumFractionDigits: 2
  }).format(n);
}

const totalItems = computed(() => {
  const items = cart.value?.items || [];
  return items.reduce((s, it) => s + Number(it.qty || 0), 0);
});

async function load() {
  loading.value = true;
  error.value = "";
  try {
    const res = await getMyCart();
    cart.value = res.data;
  } catch (e) {
    error.value = isRTL.value ? "تعذر تحميل السلة." : "Impossible de charger le panier.";
  } finally {
    loading.value = false;
  }
}

async function inc(it) {
  if (!cart.value) return;
  updating[it.id] = true;
  try {
    const nextQty = Number(it.qty || 0) + 1;
    await updateCartItem(cart.value.id, it.id, { qty: nextQty });
    await load();
  } finally {
    updating[it.id] = false;
  }
}

async function dec(it) {
  if (!cart.value) return;
  updating[it.id] = true;
  try {
    const nextQty = Number(it.qty || 0) - 1;
    if (nextQty <= 0) {
      await removeCartItem(cart.value.id, it.id);
    } else {
      await updateCartItem(cart.value.id, it.id, { qty: nextQty });
    }
    await load();
  } finally {
    updating[it.id] = false;
  }
}

async function remove(it) {
  if (!cart.value) return;
  updating[it.id] = true;
  try {
    await removeCartItem(cart.value.id, it.id);
    await load();
  } finally {
    updating[it.id] = false;
  }
}

async function confirm() {
  ok.value = "";
  error2.value = "";
  confirming.value = true;
  try {
    await checkoutOrder(cart.value.id);
    ok.value = isRTL.value ? "تم تأكيد الطلب ✅" : "Commande confirmée ✅";
    await load();
  } catch (e) {
    error2.value = isRTL.value ? "خطأ في تأكيد الطلب." : "Erreur confirmation commande.";
  } finally {
    confirming.value = false;
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

  .lg\:grid-cols-3 {
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