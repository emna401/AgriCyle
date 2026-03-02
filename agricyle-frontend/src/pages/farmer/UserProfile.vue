<template>
  <div class="relative min-h-screen" :dir="lang">
    <!-- Image d'arrière-plan fixe -->
    <div
      class="fixed inset-0 bg-cover bg-center bg-no-repeat"
      style="background-image: url('https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80')"
    >
      <div class="absolute inset-0 bg-black/40"></div>
    </div>

    <!-- Contenu par-dessus l'image -->
    <div class="relative z-10">
      <!-- SIDEBAR DYNAMIQUE SELON LE RÔLE -->
      <aside :class="sidebarClasses">
        <!-- En-tête sidebar avec icône dynamique -->
        <div class="agri-card p-4 mb-4 bg-white/10 backdrop-blur-lg border border-white/20">
          <div class="flex items-center gap-3" :class="{ 'flex-row-reverse': isRTL }">
            <div class="w-12 h-12 rounded-xl2 bg-gradient-to-r from-agri-green/30 to-agri-blue/30 border border-white/20 flex items-center justify-center shadow-lg flex-shrink-0">
              <span class="text-2xl text-white">{{ getRoleIcon }}</span>
            </div>
            <div class="min-w-0 flex-1">
              <div class="font-semibold text-white truncate">{{ getRoleLabel }}</div>
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

          <!-- Navigation pour FARMER -->
          <template v-if="auth.user?.role === 'FARMER'">
            <!-- Dashboard Farmer -->
            <router-link class="nav-item" to="/app/farmer">
              <div class="flex items-center gap-3 p-3 rounded-xl transition-all duration-300" 
                   :class="{ 
                     'flex-row-reverse': isRTL,
                     'bg-indigo-500/30 border border-indigo-400/30': $route.path === '/app/farmer',
                     'hover:bg-white/10': $route.path !== '/app/farmer'
                   }">
                <div class="w-10 h-10 rounded-lg bg-gradient-to-r from-agri-green/30 to-agri-blue/30 border border-white/20 flex items-center justify-center flex-shrink-0">
                  <span class="text-white text-xl">📊</span>
                </div>
                <div class="min-w-0 flex-1">
                  <div class="text-white font-medium truncate">{{ isRTL ? 'لوحة القيادة' : 'Dashboard' }}</div>
                  <div class="text-xs text-white/60 truncate">{{ isRTL ? 'نظرة عامة' : 'Vue d\'ensemble' }}</div>
                </div>
              </div>
            </router-link>

            <!-- Mes Déclarations -->
            <router-link class="nav-item" to="/app/farmer/declarations">
              <div class="flex items-center gap-3 p-3 rounded-xl transition-all duration-300" 
                   :class="{ 
                     'flex-row-reverse': isRTL,
                     'bg-emerald-500/30 border border-emerald-400/30': $route.path === '/app/farmer/declarations',
                     'hover:bg-white/10': $route.path !== '/app/farmer/declarations'
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
          </template>

          <!-- Navigation pour BENEFICIARY -->
          <template v-else-if="auth.user?.role === 'BENEFICIARY'">
            <!-- Dashboard Beneficiary -->
            <router-link class="nav-item" to="/app/beneficiary">
              <div class="flex items-center gap-3 p-3 rounded-xl transition-all duration-300" 
                   :class="{ 
                     'flex-row-reverse': isRTL,
                     'bg-indigo-500/30 border border-indigo-400/30': $route.path === '/app/beneficiary',
                     'hover:bg-white/10': $route.path !== '/app/beneficiary'
                   }">
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
          </template>

          <!-- Navigation pour DUAL -->
          <template v-else-if="auth.user?.role === 'DUAL'">
            <!-- Dashboard Dual -->
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
                  <div class="text-xs text-white/60 truncate">{{ isRTL ? 'نظرة عامة' : 'Vue d\'ensemble' }}</div>
                </div>
              </div>
            </router-link>

            <!-- Mes Déclarations (Farmer part) -->
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

            <!-- Catalogue (Beneficiary part) -->
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

            <!-- Panier (Beneficiary part) -->
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

            <!-- Mes commandes (Beneficiary part) -->
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
          </template>

          <!-- Profil (actif) - commun à tous -->
          <router-link class="nav-item" to="/app/profile">
            <div class="flex items-center gap-3 p-3 rounded-xl transition-all duration-300" 
                 :class="{ 
                   'flex-row-reverse': isRTL,
                   'bg-indigo-500/30 border border-indigo-400/30': $route.path === '/app/profile',
                   'hover:bg-white/10': $route.path !== '/app/profile'
                 }">
              <div class="w-10 h-10 rounded-lg bg-indigo-500/40 border border-indigo-400/30 flex items-center justify-center flex-shrink-0">
                <span class="text-indigo-200 text-xl">👤</span>
              </div>
              <div class="min-w-0 flex-1">
                <div class="text-white font-medium truncate">{{ isRTL ? 'الملف الشخصي' : 'Profil' }}</div>
                <div class="text-xs text-white/80 truncate">{{ isRTL ? 'معلوماتي' : 'Mes informations' }}</div>
              </div>
            </div>
          </router-link>
        </div>
      </aside>

      <!-- Main Content -->
      <main :class="contentContainerClasses">
        <div class="space-y-6">
          <!-- Header avec bouton retour dynamique -->
          <div class="mb-8">
            <div class="flex items-center justify-between mb-6 flex-wrap gap-4" :class="{ 'flex-row-reverse': isRTL }">
              <div class="flex items-center gap-4" :class="{ 'flex-row-reverse': isRTL }">
                <div class="p-3 bg-white/20 backdrop-blur-sm rounded-xl border border-white/30 flex-shrink-0">
                  <span class="text-2xl text-white">{{ getRoleIcon }}</span>
                </div>
                <div>
                  <h1 class="text-3xl md:text-4xl font-bold text-white">
                    {{ isRTL ? 'الملف الشخصي' : 'Profil' }}
                  </h1>
                  <p class="text-white/90 mt-2">
                    {{ isRTL ? 'المعلومات الشخصية' : 'Informations personnelles' }}
                  </p>
                </div>
              </div>

              <div class="flex items-center gap-3" :class="{ 'flex-row-reverse': isRTL }">
                <!-- Bouton retour dynamique selon le rôle -->
                <router-link
                  :to="dashboardLink"
                  class="px-4 py-2 border border-white/20 rounded-lg text-sm font-medium text-white/80 hover:bg-white/10 transition-all flex items-center gap-2"
                  :class="{ 'flex-row-reverse': isRTL }"
                >
                  <span>←</span>
                  <span>{{ isRTL ? 'لوحة القيادة' : 'Dashboard' }}</span>
                </router-link>

                <div class="px-4 py-2 bg-white/10 backdrop-blur-sm rounded-full border border-white/20">
                  <span class="text-sm text-white/80">
                    {{ isRTL ? 'متصل:' : 'Connecté:' }} {{ auth.user?.username }} ({{ auth.user?.role }})
                  </span>
                </div>
              </div>
            </div>
          </div>

          <!-- Contenu principal -->
          <div class="grid lg:grid-cols-2 gap-6">
            <!-- Carte Informations -->
            <div class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
              <div class="flex items-center gap-3 mb-6" :class="{ 'flex-row-reverse': isRTL }">
                <div class="p-2 bg-gradient-to-r from-indigo-500/20 to-indigo-400/20 rounded-lg">
                  <span class="text-indigo-300 text-xl">🧾</span>
                </div>
                <div>
                  <h2 class="text-xl font-semibold text-white">{{ isRTL ? 'المعلومات الشخصية' : 'Informations personnelles' }}</h2>
                  <p class="text-sm text-white/70">{{ isRTL ? 'تحديث معلوماتك' : 'Mettre à jour tes infos' }}</p>
                </div>
              </div>

              <form class="space-y-4" @submit.prevent="save">
                <!-- Nom d'utilisateur (readonly) -->
                <div>
                  <label class="block text-sm font-medium text-white/80 mb-1">
                    {{ isRTL ? 'اسم المستخدم' : "Nom d'utilisateur" }}
                  </label>
                  <input
                    :value="auth.user?.username"
                    type="text"
                    readonly
                    class="w-full px-4 py-2.5 bg-white/5 border border-white/10 rounded-xl text-white/60 cursor-not-allowed"
                  />
                </div>

                <!-- Email (readonly) -->
                <div>
                  <label class="block text-sm font-medium text-white/80 mb-1">
                    {{ isRTL ? 'البريد الإلكتروني' : 'Email' }}
                  </label>
                  <input
                    :value="auth.user?.email"
                    type="email"
                    readonly
                    class="w-full px-4 py-2.5 bg-white/5 border border-white/10 rounded-xl text-white/60 cursor-not-allowed"
                  />
                </div>

                <!-- Rôle (readonly) -->
                <div>
                  <label class="block text-sm font-medium text-white/80 mb-1">
                    {{ isRTL ? 'الدور' : 'Rôle' }}
                  </label>
                  <input
                    :value="auth.user?.role"
                    type="text"
                    readonly
                    class="w-full px-4 py-2.5 bg-white/5 border border-white/10 rounded-xl text-white/60 cursor-not-allowed"
                  />
                </div>

                <!-- Champs spécifiques à la ferme (pour FARMER et DUAL) -->
                <template v-if="isFarmerOrDual">
                  <div class="border-t border-white/10 my-4 pt-4">
                    <h3 class="text-lg font-semibold text-white mb-4">{{ isRTL ? 'معلومات المزرعة' : 'Informations ferme' }}</h3>
                  </div>

                  <!-- Nom ferme -->
                  <div>
                    <label class="block text-sm font-medium text-white/80 mb-1">
                      {{ isRTL ? 'اسم المزرعة (اختياري)' : 'Nom ferme (optionnel)' }}
                    </label>
                    <input
                      v-model="form.farm_name"
                      type="text"
                      :placeholder="isRTL ? 'مزرعة أحمد' : 'Ferme Ahmed'"
                      class="w-full px-4 py-2.5 bg-white/10 border border-white/20 rounded-xl text-white placeholder-white/40 focus:outline-none focus:border-white/40 focus:bg-white/15 transition-all"
                    />
                  </div>

                  <!-- Adresse -->
                  <div>
                    <label class="block text-sm font-medium text-white/80 mb-1">
                      {{ isRTL ? 'عنوان المزرعة' : 'Adresse ferme' }}
                    </label>
                    <input
                      v-model="form.farm_address"
                      type="text"
                      :placeholder="isRTL ? 'سليانة...' : 'Siliana...'"
                      class="w-full px-4 py-2.5 bg-white/10 border border-white/20 rounded-xl text-white placeholder-white/40 focus:outline-none focus:border-white/40 focus:bg-white/15 transition-all"
                    />
                  </div>

                  <!-- Gouvernorat -->
                  <div>
                    <label class="block text-sm font-medium text-white/80 mb-1">
                      {{ isRTL ? 'الولاية' : 'Gouvernorat' }}
                    </label>
                    <input
                      v-model="form.governorate"
                      type="text"
                      :placeholder="isRTL ? 'سليانة' : 'Siliana'"
                      class="w-full px-4 py-2.5 bg-white/10 border border-white/20 rounded-xl text-white placeholder-white/40 focus:outline-none focus:border-white/40 focus:bg-white/15 transition-all"
                    />
                  </div>

                  <!-- Délégation -->
                  <div>
                    <label class="block text-sm font-medium text-white/80 mb-1">
                      {{ isRTL ? 'المعتمدية' : 'Délégation' }}
                    </label>
                    <input
                      v-model="form.delegation"
                      type="text"
                      :placeholder="isRTL ? '...' : '...'"
                      class="w-full px-4 py-2.5 bg-white/10 border border-white/20 rounded-xl text-white placeholder-white/40 focus:outline-none focus:border-white/40 focus:bg-white/15 transition-all"
                    />
                  </div>

                  <!-- Latitude/Longitude -->
                  <div class="grid grid-cols-2 gap-3">
                    <div>
                      <label class="block text-sm font-medium text-white/80 mb-1">
                        {{ isRTL ? 'خط العرض' : 'Latitude' }}
                      </label>
                      <input
                        v-model="form.farm_lat"
                        type="text"
                        placeholder="34.123456"
                        class="w-full px-4 py-2.5 bg-white/10 border border-white/20 rounded-xl text-white placeholder-white/40 focus:outline-none focus:border-white/40 focus:bg-white/15 transition-all"
                      />
                    </div>
                    <div>
                      <label class="block text-sm font-medium text-white/80 mb-1">
                        {{ isRTL ? 'خط الطول' : 'Longitude' }}
                      </label>
                      <input
                        v-model="form.farm_lng"
                        type="text"
                        placeholder="9.123456"
                        class="w-full px-4 py-2.5 bg-white/10 border border-white/20 rounded-xl text-white placeholder-white/40 focus:outline-none focus:border-white/40 focus:bg-white/15 transition-all"
                      />
                    </div>
                  </div>

                  <!-- Boutons d'action pour FARMER et DUAL -->
                  <div class="flex gap-3 pt-2" :class="{ 'flex-row-reverse': isRTL }">
                    <button
                      type="button"
                      @click="useGps"
                      :disabled="gpsLoading"
                      class="flex-1 px-4 py-2.5 bg-gradient-to-r from-indigo-500/20 to-indigo-600/20 hover:from-indigo-500/30 hover:to-indigo-600/30 text-indigo-200 border border-indigo-400/30 rounded-xl font-medium transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                    >
                      <span class="flex items-center justify-center gap-2" :class="{ 'flex-row-reverse': isRTL }">
                        <span v-if="gpsLoading" class="animate-spin">⟳</span>
                        <span v-else>📍</span>
                        {{ gpsLoading ? (isRTL ? 'جاري...' : '...') : (isRTL ? 'استخدام GPS' : 'Utiliser GPS') }}
                      </span>
                    </button>
                    <button
                      type="submit"
                      :disabled="loading"
                      class="flex-1 px-4 py-2.5 bg-gradient-to-r from-agri-green to-agri-green-dark hover:from-agri-green-dark hover:to-agri-green text-white rounded-xl font-medium shadow-lg shadow-agri-green/20 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                    >
                      <span class="flex items-center justify-center gap-2" :class="{ 'flex-row-reverse': isRTL }">
                        <span v-if="loading" class="animate-spin">⟳</span>
                        {{ loading ? (isRTL ? 'جاري...' : '...') : (isRTL ? 'حفظ' : 'Enregistrer') }}
                      </span>
                    </button>
                  </div>
                </template>

                <!-- Bouton Enregistrer pour BENEFICIARY (sans champs ferme) -->
                <div v-else class="flex gap-3 pt-4" :class="{ 'flex-row-reverse': isRTL }">
                  <button
                    type="submit"
                    :disabled="loading"
                    class="flex-1 px-4 py-2.5 bg-gradient-to-r from-agri-green to-agri-green-dark hover:from-agri-green-dark hover:to-agri-green text-white rounded-xl font-medium shadow-lg shadow-agri-green/20 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    <span class="flex items-center justify-center gap-2" :class="{ 'flex-row-reverse': isRTL }">
                      <span v-if="loading" class="animate-spin">⟳</span>
                      {{ loading ? (isRTL ? 'جاري...' : '...') : (isRTL ? 'حفظ' : 'Enregistrer') }}
                    </span>
                  </button>
                </div>

                <!-- Messages -->
                <div v-if="error" class="p-3 bg-red-500/20 border border-red-400/30 rounded-xl">
                  <p class="text-sm text-red-200 flex items-center gap-2" :class="{ 'flex-row-reverse': isRTL }">
                    <span>❌</span> {{ error }}
                  </p>
                </div>
                <div v-if="ok" class="p-3 bg-green-500/20 border border-green-400/30 rounded-xl">
                  <p class="text-sm text-green-200 flex items-center gap-2" :class="{ 'flex-row-reverse': isRTL }">
                    <span>✅</span> {{ ok }}
                  </p>
                </div>

                <!-- Astuce pour FARMER et DUAL -->
                <div v-if="isFarmerOrDual" class="p-4 bg-white/5 rounded-xl border border-white/10">
                  <p class="text-xs text-white/60 flex items-start gap-2" :class="{ 'flex-row-reverse': isRTL }">
                    <span>💡</span>
                    <span>
                      {{ isRTL ? 'GPS قد يكون غير دقيق → انقر على الخريطة للتصحيح.' : 'GPS peut être imprécis → clique sur la carte pour corriger.' }}
                    </span>
                  </p>
                </div>
              </form>
            </div>

            <!-- Colonne droite -->
            <div class="space-y-6">
              <!-- Carte pour TOUS LES RÔLES -->
              <div class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
                <div class="flex items-center gap-3 mb-4" :class="{ 'flex-row-reverse': isRTL }">
                  <div class="p-2 bg-gradient-to-r from-emerald-500/20 to-emerald-400/20 rounded-lg">
                    <span class="text-emerald-300 text-xl">🗺️</span>
                  </div>
                  <div>
                    <h2 class="text-xl font-semibold text-white">{{ isRTL ? 'الموقع' : 'Localisation' }}</h2>
                    <p class="text-sm text-white/70">
                      {{ isRTL ? 'انقر على الخريطة لضبط الموقع' : 'Clique sur la carte pour ajuster' }}
                    </p>
                  </div>
                </div>

                <MapView
                  :lat="toNum(form.farm_lat)"
                  :lng="toNum(form.farm_lng)"
                  :readOnly="false"
                  @update:latlng="onMapPick"
                  class="rounded-xl overflow-hidden border border-white/20"
                />
                
                <!-- Instructions supplémentaires -->
                <p class="text-xs text-white/60 mt-2 text-center">
                  {{ isRTL ? '🗺️ انقر على الخريطة لوضع علامة الموقع' : '🗺️ Clique pour placer le marqueur' }}
                </p>
              </div>

              <!-- Carte Sécurité (pour tous) -->
              <div class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
                <div class="flex items-center gap-3 mb-4" :class="{ 'flex-row-reverse': isRTL }">
                  <div class="p-2 bg-gradient-to-r from-blue-500/20 to-blue-400/20 rounded-lg">
                    <span class="text-blue-300 text-xl">🔒</span>
                  </div>
                  <div>
                    <h2 class="text-xl font-semibold text-white">{{ isRTL ? 'الخصوصية' : 'Confidentialité' }}</h2>
                    <p class="text-sm text-white/70">{{ isRTL ? 'بيانات خاصة' : 'Données privées' }}</p>
                  </div>
                </div>

                <div class="p-4 bg-white/5 rounded-xl border border-white/10">
                  <p class="text-sm text-white/80 leading-relaxed">
                    {{ isRTL 
                      ? 'معلوماتك الشخصية مرئية فقط لك وللمسؤول.' 
                      : 'Tes informations personnelles sont visibles uniquement par toi et l\'admin.' 
                    }}
                  </p>
                </div>

                <!-- Informations supplémentaires -->
                <div class="mt-4 pt-4 border-t border-white/10">
                  <div class="flex items-center justify-between text-sm" :class="{ 'flex-row-reverse': isRTL }">
                    <span class="text-white/60">{{ isRTL ? 'آخر تحديث' : 'Dernière mise à jour' }}</span>
                    <span class="text-white/90">{{ fmt(new Date()) }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { onMounted, reactive, ref, computed } from "vue";
import { useRoute } from "vue-router";
import { useAuthStore } from "../../store/auth";
import { useI18n } from "vue-i18n";
import { getMe, updateMe } from "../../api/exports";
import MapView from "../../components/shared/MapView.vue";

const route = useRoute();
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

// Computed properties pour le rôle
const isFarmerOrDual = computed(() => {
  const role = auth.user?.role;
  return role === 'FARMER' || role === 'DUAL';
});

const getRoleIcon = computed(() => {
  const role = auth.user?.role;
  if (role === 'FARMER') return '👨‍🌾';
  if (role === 'BENEFICIARY') return '👤';
  if (role === 'DUAL') return '👥';
  return '👤';
});

const getRoleLabel = computed(() => {
  const role = auth.user?.role;
  if (role === 'FARMER') return isRTL.value ? 'المزارع' : 'Agriculteur';
  if (role === 'BENEFICIARY') return isRTL.value ? 'المستفيد' : 'Bénéficiaire';
  if (role === 'DUAL') return isRTL.value ? 'مزدوج' : 'Dual';
  return isRTL.value ? 'مستخدم' : 'Utilisateur';
});

const dashboardLink = computed(() => {
  const role = auth.user?.role;
  if (role === 'FARMER') return '/app/farmer';
  if (role === 'BENEFICIARY') return '/app/beneficiary';
  if (role === 'DUAL') return '/app/dual';
  return '/app';
});

const loading = ref(false);
const gpsLoading = ref(false);
const error = ref("");
const ok = ref("");

const form = reactive({
  farm_name: "",
  farm_address: "",
  governorate: "",
  delegation: "",
  farm_lat: "",
  farm_lng: ""
});

function toNum(v) {
  if (v === null || v === undefined || v === "") return null;
  const n = Number(v);
  return Number.isFinite(n) ? n : null;
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

function onMapPick({ lat, lng }) {
  form.farm_lat = lat ?? "";
  form.farm_lng = lng ?? "";
}

async function useGps() {
  error.value = "";
  ok.value = "";

  if (!navigator.geolocation) {
    error.value = isRTL.value ? "GPS غير مدعوم في هذا المتصفح." : "GPS non supporté sur ce navigateur.";
    return;
  }

  gpsLoading.value = true;

  navigator.geolocation.getCurrentPosition(
    (pos) => {
      const lat = Number(pos.coords.latitude.toFixed(6));
      const lng = Number(pos.coords.longitude.toFixed(6));
      form.farm_lat = lat;
      form.farm_lng = lng;
      ok.value = isRTL.value ? "تم تحديد الموقع ✅ (صحح على الخريطة إن لزم)" : "GPS récupéré ✅ (corrige sur la carte si besoin)";
      gpsLoading.value = false;
    },
    () => {
      error.value = isRTL.value ? "تعذر تحديد الموقع." : "Impossible de récupérer la position GPS.";
      gpsLoading.value = false;
    },
    { enableHighAccuracy: true, timeout: 8000 }
  );
}

async function save() {
  loading.value = true;
  error.value = "";
  ok.value = "";

  try {
    // Ne préparer les champs ferme que si l'utilisateur est FARMER ou DUAL
    const payload = {};
    
    if (isFarmerOrDual.value) {
      payload.farm_name = form.farm_name || null;
      payload.farm_address = form.farm_address || null;
      payload.governorate = form.governorate || null;
      payload.delegation = form.delegation || null;
      payload.farm_lat = form.farm_lat === "" ? null : Number(form.farm_lat);
      payload.farm_lng = form.farm_lng === "" ? null : Number(form.farm_lng);
    }

    const res = await updateMe(payload);
    auth.user = res.data;
    ok.value = isRTL.value ? "تم تحديث الملف ✅" : "Profil mis à jour ✅";
  } catch (e) {
    error.value = isRTL.value ? "خطأ في حفظ الملف." : "Erreur sauvegarde profil.";
  } finally {
    loading.value = false;
  }
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

  const res = await getMe();
  auth.user = res.data;

  form.farm_name = res.data.farm_name || "";
  form.farm_address = res.data.farm_address || "";
  form.governorate = res.data.governorate || "";
  form.delegation = res.data.delegation || "";
  form.farm_lat = res.data.farm_lat || "";
  form.farm_lng = res.data.farm_lng || "";
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

/* Input style */
input {
  backdrop-filter: blur(5px);
}

input:focus {
  box-shadow: 0 0 0 2px rgba(255, 255, 255, 0.1);
}

input:read-only {
  background: rgba(255, 255, 255, 0.05);
  border-color: rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.6);
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

  .lg\:grid-cols-2 {
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