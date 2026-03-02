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
    
    <div class="relative z-10">
      <!-- SIDEBAR -->
      <aside :class="sidebarClasses">
        <div class="agri-card p-4 mb-4 bg-white/10 backdrop-blur-lg border border-white/20">
          <div class="flex items-center gap-3" :class="{ 'flex-row-reverse': isRTL }">
            <div class="w-12 h-12 rounded-xl2 bg-gradient-to-r from-agri-green/30 to-agri-blue/30 border border-white/20 flex items-center justify-center shadow-lg flex-shrink-0">
              <span class="text-2xl text-white">🛡️</span>
            </div>
            <div class="min-w-0 flex-1">
              <div class="font-semibold text-white truncate">{{ isRTL ? 'الإدارة' : 'Administration' }}</div>
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
          
          <router-link class="nav-item" to="/app/admin">
            <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300" :class="{ 'flex-row-reverse': isRTL }">
              <div class="w-10 h-10 rounded-lg bg-gradient-to-r from-agri-green/30 to-agri-blue/30 border border-white/20 flex items-center justify-center flex-shrink-0">
                <span class="text-white text-xl">📊</span>
              </div>
              <div class="min-w-0 flex-1">
                <div class="text-white font-medium truncate">{{ isRTL ? 'لوحة القيادة' : 'Tableau de Bord' }}</div>
                <div class="text-xs text-white/60 truncate">{{ isRTL ? 'نظرة عامة' : 'Vue d\'ensemble' }}</div>
              </div>
            </div>
          </router-link>

          <router-link class="nav-item" to="/app/admin/declarations">
            <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300" :class="{ 'flex-row-reverse': isRTL }">
              <div class="w-10 h-10 rounded-lg bg-emerald-500/30 border border-emerald-400/20 flex items-center justify-center flex-shrink-0">
                <span class="text-emerald-300 text-xl">♻️</span>
              </div>
              <div class="text-white font-medium truncate">{{ isRTL ? 'التصاريح' : 'Déclarations' }}</div>
            </div>
          </router-link>

          <router-link class="nav-item" to="/app/admin/products">
            <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300" :class="{ 'flex-row-reverse': isRTL }">
              <div class="w-10 h-10 rounded-lg bg-sky-500/30 border border-sky-400/20 flex items-center justify-center flex-shrink-0">
                <span class="text-sky-300 text-xl">📦</span>
              </div>
              <div class="text-white font-medium truncate">{{ isRTL ? 'المنتجات' : 'Produits' }}</div>
            </div>
          </router-link>

          <router-link class="nav-item" to="/app/admin/orders">
            <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300" :class="{ 'flex-row-reverse': isRTL }">
              <div class="w-10 h-10 rounded-lg bg-amber-500/30 border border-amber-400/20 flex items-center justify-center flex-shrink-0">
                <span class="text-amber-300 text-xl">🧾</span>
              </div>
              <div class="text-white font-medium truncate">{{ isRTL ? 'الطلبات' : 'Commandes' }}</div>
            </div>
          </router-link>

          <router-link class="nav-item" to="/app/admin/users">
            <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300" :class="{ 'flex-row-reverse': isRTL }">
              <div class="w-10 h-10 rounded-lg bg-indigo-500/30 border border-indigo-400/20 flex items-center justify-center flex-shrink-0">
                <span class="text-indigo-300 text-xl">👥</span>
              </div>
              <div class="text-white font-medium truncate">{{ isRTL ? 'المستخدمين' : 'Utilisateurs' }}</div>
            </div>
          </router-link>
        </div>
      </aside>

      <!-- Contenu principal -->
      
        <!-- Header -->
        <div >
          <div class="flex items-center justify-between mb-6 flex-wrap gap-4" :class="{ 'flex-row-reverse': isRTL }">
            <div class="flex items-center gap-4" :class="{ 'flex-row-reverse': isRTL }">
              <div class="p-3 bg-white/20 backdrop-blur-sm rounded-xl border border-white/30 flex-shrink-0">
                <span class="text-2xl text-white">👥</span>
              </div>
              <div>
                <h1 class="text-3xl md:text-4xl font-bold text-white">
                  {{ isRTL ? 'إدارة المستخدمين' : 'Gestion des Utilisateurs' }}
                </h1>
                <p class="text-white/90 mt-2">
                  {{ isRTL ? 'إدارة وتحديث معلومات المستخدمين' : 'Gérer et mettre à jour les informations des utilisateurs' }}
                </p>
              </div>
            </div>
            
            <div class="flex items-center gap-3" :class="{ 'flex-row-reverse': isRTL }">
              <!-- Bouton d'export Excel -->
              <button 
                @click="handleExportExcel"
                :disabled="loading || filteredUsers.length === 0 || exportingExcel"
                class="agri-btn-export px-4 py-2 text-sm flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
                :class="{ 'flex-row-reverse': isRTL }"
              >
                <span v-if="exportingExcel" class="inline-block animate-spin">⟳</span>
                <span v-else>📊</span>
                <span>{{ exportingExcel ? (isRTL ? 'جاري...' : 'Export...') : (isRTL ? 'إكسل' : 'Excel') }}</span>
              </button>
              
              <div class="px-4 py-2 bg-white/10 backdrop-blur-sm rounded-full border border-white/20">
                <span class="text-sm text-white/80">
                  {{ isRTL ? 'متصل:' : 'Connecté:' }} {{ auth.user?.username }} ({{ auth.user?.role }})
                </span>
              </div>
            </div>
          </div>
        </div>

        <!-- Loading State -->
        <div v-if="loading" class="agri-card p-12 text-center hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
          <div class="inline-block animate-spin text-4xl mb-4 text-white/80">⟳</div>
          <h3 class="text-xl font-semibold text-white mb-2">{{ isRTL ? 'جاري تحميل المستخدمين' : 'Chargement des utilisateurs' }}</h3>
          <p class="text-white/80">{{ isRTL ? 'يرجى الانتظار...' : 'Veuillez patienter...' }}</p>
        </div>

        <!-- Error State -->
        <div v-if="error" class="agri-card p-6 bg-gradient-to-r from-red-500/10 to-red-500/5 border border-red-500/20">
          <div class="flex items-center gap-4" :class="{ 'flex-row-reverse': isRTL }">
            <div class="p-2 bg-red-500/20 rounded-lg flex-shrink-0">
              <span class="text-red-300 text-xl">❌</span>
            </div>
            <div class="flex-1">
              <h4 class="font-medium text-red-200">{{ isRTL ? 'خطأ في التحميل' : 'Erreur de chargement' }}</h4>
              <p class="text-sm text-red-200/90 mt-1">{{ error }}</p>
            </div>
            <button @click="loadUsers" class="px-4 py-2 bg-red-500/20 hover:bg-red-500/30 text-red-300 rounded-lg transition-colors">
              {{ isRTL ? 'إعادة المحاولة' : 'Réessayer' }}
            </button>
          </div>
        </div>

        <!-- Statistiques rapides -->
        <div v-if="users.length && !loading" class="grid grid-cols-2 md:grid-cols-5 gap-4 mb-6">
          <div class="agri-card p-3 text-center bg-white/5 backdrop-blur-sm border border-white/10">
            <div class="text-2xl font-bold text-blue-300">{{ stats.active }}</div>
            <div class="text-xs text-white/80 mt-1">✅ {{ isRTL ? 'نشط' : 'ACTIF' }}</div>
          </div>
          <div class="agri-card p-3 text-center bg-white/5 backdrop-blur-sm border border-white/10">
            <div class="text-2xl font-bold text-emerald-300">{{ stats.farmers }}</div>
            <div class="text-xs text-white/80 mt-1">👨‍🌾 FARMER</div>
          </div>
          <div class="agri-card p-3 text-center bg-white/5 backdrop-blur-sm border border-white/10">
            <div class="text-2xl font-bold text-purple-300">{{ stats.beneficiaries }}</div>
            <div class="text-xs text-white/80 mt-1">🏭 BENEFICIARY</div>
          </div>
          <div class="agri-card p-3 text-center bg-white/5 backdrop-blur-sm border border-white/10">
            <div class="text-2xl font-bold text-amber-300">{{ stats.dual }}</div>
            <div class="text-xs text-white/80 mt-1">👥 DUAL</div>
          </div>
          <div class="agri-card p-3 text-center bg-white/5 backdrop-blur-sm border border-white/10">
            <div class="text-2xl font-bold text-red-300">{{ stats.admins }}</div>
            <div class="text-xs text-white/80 mt-1">👑 ADMIN</div>
          </div>
        </div>

        <!-- Filtres et recherche -->
        <div v-if="!loading" class="agri-card p-4 mb-6 bg-white/10 backdrop-blur-lg border border-white/20">
          <div class="grid grid-cols-1 md:grid-cols-5 gap-4">
            <!-- Recherche -->
            <div>
              <label class="block text-sm font-medium text-white/80 mb-1">
                🔍 {{ isRTL ? 'بحث' : 'Rechercher' }}
              </label>
              <input
                v-model="searchQuery"
                @input="debouncedSearch"
                type="text"
                :placeholder="isRTL ? 'الاسم، البريد، الهاتف...' : 'Nom, email, téléphone...'"
                class="agri-input w-full px-3 py-2 bg-white/10 border border-white/20 rounded-md focus:outline-none focus:ring-2 focus:ring-agri-green text-white placeholder-white/50"
              >
            </div>
            
            <!-- Filtre Rôle -->
            <div>
              <label class="block text-sm font-medium text-white/80 mb-1">
                👤 {{ isRTL ? 'الدور' : 'Rôle' }}
              </label>
              <select
                v-model="roleFilter"
                class="agri-select w-full px-3 py-2 bg-white/10 border border-white/20 rounded-md focus:outline-none focus:ring-2 focus:ring-agri-green text-white"
              >
                <option value="" class="bg-gray-800 text-white">{{ isRTL ? 'جميع الأدوار' : 'Tous les rôles' }}</option>
                <option value="FARMER" class="bg-gray-800 text-white">👨‍🌾 Farmer</option>
                <option value="BENEFICIARY" class="bg-gray-800 text-white">🏭 Beneficiary</option>
                <option value="DUAL" class="bg-gray-800 text-white">👥 Dual</option>
                <option value="ADMIN" class="bg-gray-800 text-white">👑 Admin</option>
              </select>
            </div>
            
            <!-- Filtre Statut -->
            <div>
              <label class="block text-sm font-medium text-white/80 mb-1">
                📊 {{ isRTL ? 'الحالة' : 'Statut' }}
              </label>
              <select
                v-model="statusFilter"
                class="agri-select w-full px-3 py-2 bg-white/10 border border-white/20 rounded-md focus:outline-none focus:ring-2 focus:ring-agri-green text-white"
              >
                <option value="" class="bg-gray-800 text-white">{{ isRTL ? 'جميع الحالات' : 'Tous les statuts' }}</option>
                <option value="ACTIVE" class="bg-gray-800 text-white">✅ {{ isRTL ? 'نشط' : 'Actif' }}</option>
                <option value="SUSPENDED" class="bg-gray-800 text-white">⚠️ {{ isRTL ? 'موقوف' : 'Suspendu' }}</option>
                <option value="PENDING" class="bg-gray-800 text-white">⏳ {{ isRTL ? 'قيد الانتظار' : 'En attente' }}</option>
                <option value="BLOCKED" class="bg-gray-800 text-white">❌ {{ isRTL ? 'محظور' : 'Bloqué' }}</option>
              </select>
            </div>
            
            <!-- Filtre Ville -->
            <div>
              <label class="block text-sm font-medium text-white/80 mb-1">
                🏙️ {{ isRTL ? 'المدينة' : 'Ville' }}
              </label>
              <select
                v-model="cityFilter"
                class="agri-select w-full px-3 py-2 bg-white/10 border border-white/20 rounded-md focus:outline-none focus:ring-2 focus:ring-agri-green text-white"
              >
                <option value="" class="bg-gray-800 text-white">{{ isRTL ? 'جميع المدن' : 'Toutes les villes' }}</option>
                <option v-for="city in tunisianCities" :key="city" :value="city" class="bg-gray-800 text-white">{{ city }}</option>
              </select>
            </div>
            
            <!-- Filtre Délégation -->
            <div>
              <label class="block text-sm font-medium text-white/80 mb-1">
                📍 {{ isRTL ? 'المعتمدية' : 'Délégation' }}
              </label>
              <input
                v-model="delegationFilter"
                type="text"
                :placeholder="isRTL ? 'اسم المعتمدية...' : 'Nom de la délégation...'"
                class="agri-input w-full px-3 py-2 bg-white/10 border border-white/20 rounded-md focus:outline-none focus:ring-2 focus:ring-agri-green text-white placeholder-white/50"
              >
            </div>
          </div>
          
          <!-- Boutons d'action des filtres -->
          <div class="flex justify-between items-center mt-4 flex-wrap gap-2" :class="{ 'flex-row-reverse': isRTL }">
            <div class="flex flex-wrap gap-2" :class="{ 'flex-row-reverse': isRTL }">
              <span class="text-sm font-medium text-white/80">{{ isRTL ? 'الإحصائيات :' : 'Statistiques :' }}</span>
              <span class="text-xs bg-blue-500/30 text-blue-200 px-2 py-1 rounded-full border border-blue-400/20">
                {{ isRTL ? 'المجموع' : 'Total' }}: {{ filteredUsers.length }}
              </span>
              <span class="text-xs bg-green-500/30 text-green-200 px-2 py-1 rounded-full border border-green-400/20">
                ✅ {{ isRTL ? 'نشط' : 'Actifs' }}: {{ stats.active }}
              </span>
              <span class="text-xs bg-emerald-500/30 text-emerald-200 px-2 py-1 rounded-full border border-emerald-400/20">
                👨‍🌾 Farmers: {{ stats.farmers }}
              </span>
              <span class="text-xs bg-purple-500/30 text-purple-200 px-2 py-1 rounded-full border border-purple-400/20">
                🏭 Bénéficiaires: {{ stats.beneficiaries }}
              </span>
              <span class="text-xs bg-amber-500/30 text-amber-200 px-2 py-1 rounded-full border border-amber-400/20">
                👑 Admins: {{ stats.admins }}
              </span>
            </div>
            <button
              @click="resetFilters"
              class="px-3 py-2 text-sm text-white/80 hover:text-white bg-white/10 hover:bg-white/20 rounded-lg transition-all flex items-center gap-2"
              :class="{ 'flex-row-reverse': isRTL }"
            >
              <span>❌</span>
              <span>{{ isRTL ? 'إعادة تعيين' : 'Réinitialiser' }}</span>
            </button>
          </div>
        </div>

        <!-- Tableau des utilisateurs -->
        <div v-if="users.length && !loading">
          <div class="mb-4 flex items-center justify-between" :class="{ 'flex-row-reverse': isRTL }">
            <h3 class="text-lg font-semibold text-white">
              {{ filteredUsers.length }} {{ isRTL ? 'مستخدم' : 'utilisateur' }}{{ filteredUsers.length > 1 ? (isRTL ? '' : 's') : '' }}
            </h3>
            <div class="flex items-center gap-2" :class="{ 'flex-row-reverse': isRTL }">
              <span class="text-sm text-white/60">{{ isRTL ? 'عرض :' : 'Afficher :' }}</span>
              <select 
                v-model="pageSize" 
                @change="currentPage = 1"
                class="agri-select text-sm bg-white/10 border border-white/20 rounded px-2 py-1 text-white"
              >
                <option value="10" class="bg-gray-800">10</option>
                <option value="15" class="bg-gray-800">15</option>
                <option value="25" class="bg-gray-800">25</option>
                <option value="50" class="bg-gray-800">50</option>
                <option value="100" class="bg-gray-800">100</option>
              </select>
            </div>
          </div>

          <!-- Tableau -->
          <div class="agri-card overflow-hidden bg-white/10 backdrop-blur-lg border border-white/20">
            <div class="overflow-x-auto">
              <table class="min-w-full divide-y divide-white/20">
                <thead class="bg-white/5">
                  <tr>
                    <th class="px-6 py-3 text-left text-xs font-medium text-white/70 uppercase tracking-wider cursor-pointer hover:bg-white/10" @click="sortBy('username')">
                      <div class="flex items-center gap-1" :class="{ 'flex-row-reverse': isRTL }">
                        <span>{{ isRTL ? 'المستخدم' : 'Utilisateur' }}</span>
                        <span v-if="sortField === 'username'" class="text-white/70">
                          {{ sortDirection === 'asc' ? '↑' : '↓' }}
                        </span>
                      </div>
                    </th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-white/70 uppercase tracking-wider">
                      {{ isRTL ? 'جهة الاتصال' : 'Contact' }}
                    </th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-white/70 uppercase tracking-wider cursor-pointer hover:bg-white/10" @click="sortBy('role')">
                      <div class="flex items-center gap-1" :class="{ 'flex-row-reverse': isRTL }">
                        <span>{{ isRTL ? 'الدور والحالة' : 'Rôle & Statut' }}</span>
                        <span v-if="sortField === 'role'" class="text-white/70">
                          {{ sortDirection === 'asc' ? '↑' : '↓' }}
                        </span>
                      </div>
                    </th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-white/70 uppercase tracking-wider cursor-pointer hover:bg-white/10" @click="sortBy('city')">
                      <div class="flex items-center gap-1" :class="{ 'flex-row-reverse': isRTL }">
                        <span>{{ isRTL ? 'المدينة' : 'Ville' }}</span>
                        <span v-if="sortField === 'city'" class="text-white/70">
                          {{ sortDirection === 'asc' ? '↑' : '↓' }}
                        </span>
                      </div>
                    </th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-white/70 uppercase tracking-wider">
                      {{ isRTL ? 'الموقع' : 'Localisation' }}
                    </th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-white/70 uppercase tracking-wider cursor-pointer hover:bg-white/10" @click="sortBy('date_joined')">
                      <div class="flex items-center gap-1" :class="{ 'flex-row-reverse': isRTL }">
                        <span>{{ isRTL ? 'تاريخ التسجيل' : 'Inscription' }}</span>
                        <span v-if="sortField === 'date_joined'" class="text-white/70">
                          {{ sortDirection === 'asc' ? '↑' : '↓' }}
                        </span>
                      </div>
                    </th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-white/70 uppercase tracking-wider">
                      {{ isRTL ? 'الإجراءات' : 'Actions' }}
                    </th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-white/20">
                  <!-- Empty state -->
                  <tr v-if="paginatedUsers.length === 0">
                    <td colspan="7" class="px-6 py-12 text-center">
                      <div class="text-white/50 mb-2 text-4xl">👤</div>
                      <p class="text-white/70">{{ isRTL ? 'لم يتم العثور على مستخدمين' : 'Aucun utilisateur trouvé' }}</p>
                      <p class="text-sm text-white/50 mt-1">{{ isRTL ? 'حاول تعديل معايير البحث' : 'Essayez de modifier vos filtres' }}</p>
                    </td>
                  </tr>
                  
                  <!-- Users list -->
                  <tr v-for="user in paginatedUsers" :key="user.id" class="hover:bg-white/5 transition-colors">
                    <!-- Colonne Utilisateur -->
                    <td class="px-6 py-4 whitespace-nowrap">
                      <div class="flex items-center" :class="{ 'flex-row-reverse': isRTL }">
                        <div class="flex-shrink-0 h-10 w-10 bg-gradient-to-r from-agri-green/30 to-agri-blue/30 rounded-full flex items-center justify-center border border-white/20">
                          <span class="text-white font-semibold">
                            {{ getUserInitials(user.username) }}
                          </span>
                        </div>
                        <div :class="isRTL ? 'mr-4' : 'ml-4'">
                          <div class="text-sm font-medium text-white flex items-center gap-2" :class="{ 'flex-row-reverse': isRTL }">
                            <span>{{ user.username }}</span>
                            <span v-if="user.farm_name" class="text-xs text-white/60">
                              ({{ user.farm_name }})
                            </span>
                          </div>
                          <div v-if="user.delegation" class="text-xs text-white/60">
                            {{ user.delegation }}
                          </div>
                        </div>
                      </div>
                    </td>

                    <!-- Colonne Contact -->
                    <td class="px-6 py-4 whitespace-nowrap">
                      <div class="text-sm text-white">{{ user.email }}</div>
                      <div v-if="user.phone" class="text-sm text-white/60">
                        📱 {{ user.phone }}
                      </div>
                      <div v-else class="text-xs text-white/40">
                        {{ isRTL ? 'لا يوجد هاتف' : 'Pas de téléphone' }}
                      </div>
                    </td>

                    <!-- Colonne Rôle & Statut -->
                    <td class="px-6 py-4 whitespace-nowrap">
                      <div class="flex flex-col gap-1">
                        <span :class="getRoleBadgeClass(user.role)" class="inline-flex text-xs px-2 py-1 rounded-full font-medium">
                          {{ getRoleLabel(user.role) }}
                        </span>
                        <span :class="getStatusBadgeClass(user.status)" class="inline-flex text-xs px-2 py-1 rounded-full font-medium">
                          {{ getStatusLabel(user.status) }}
                        </span>
                      </div>
                    </td>

                    <!-- Colonne Ville -->
                    <td class="px-6 py-4 whitespace-nowrap">
                      <div class="flex flex-col gap-1">
                        <span v-if="user.city" class="inline-flex items-center gap-1">
                          <span class="text-xs bg-blue-500/20 text-blue-200 px-2 py-1 rounded-full font-medium border border-blue-400/20">
                            🏙️ {{ user.city }}
                          </span>
                        </span>
                        <span v-else class="text-xs text-white/40 italic">
                          {{ isRTL ? 'غير محدد' : 'Non spécifiée' }}
                        </span>
                      </div>
                    </td>

                    <!-- Colonne Localisation -->
                    <td class="px-6 py-4">
                      <div class="space-y-1">
                        <div v-if="user.farm_address" class="text-sm text-white">
                          🏠 {{ truncateText(user.farm_address, 25) }}
                        </div>
                        <div v-if="user.delegation" class="text-xs text-white/60">
                          📍 {{ user.delegation }}
                        </div>
                        <div v-if="user.farm_lat && user.farm_lng" class="text-xs text-white/50">
                          📍 {{ parseFloat(user.farm_lat).toFixed(6) }}, {{ parseFloat(user.farm_lng).toFixed(6) }}
                        </div>
                        <div v-else class="text-xs text-white/40">
                          {{ isRTL ? 'لا يوجد موقع' : 'Pas de localisation' }}
                        </div>
                        <div class="flex gap-2 mt-1" :class="{ 'flex-row-reverse': isRTL }">
                          <button 
                            v-if="user.farm_lat && user.farm_lng"
                            @click="viewOnMap(user)"
                            class="text-xs text-agri-green hover:text-agri-green-light hover:underline flex items-center gap-1"
                            :class="{ 'flex-row-reverse': isRTL }"
                          >
                            <span>🗺️</span>
                            <span>{{ isRTL ? 'عرض الخريطة' : 'Voir carte' }}</span>
                          </button>
                          <button 
                            v-if="user.farm_address"
                            @click="copyAddress(user.farm_address)"
                            class="text-xs text-blue-400 hover:text-blue-300 hover:underline flex items-center gap-1"
                            :class="{ 'flex-row-reverse': isRTL }"
                            :title="isRTL ? 'نسخ العنوان' : 'Copier l\'adresse'"
                          >
                            <span>📋</span>
                            <span>{{ isRTL ? 'نسخ' : 'Copier' }}</span>
                          </button>
                        </div>
                      </div>
                    </td>

                    <!-- Colonne Inscription -->
                    <td class="px-6 py-4 whitespace-nowrap">
                      <div class="text-sm text-white">
                        {{ formatDate(user.date_joined) }}
                      </div>
                      <div class="text-xs text-white/60">
                        {{ getDaysAgo(user.date_joined) }}
                      </div>
                      <div v-if="user.last_login" class="text-xs text-white/40">
                        {{ isRTL ? 'آخر اتصال' : 'Dernière connexion' }}: {{ formatDate(user.last_login) }}
                      </div>
                    </td>

                    <!-- Colonne Actions -->
                    <td class="px-6 py-4 whitespace-nowrap">
                      <div class="flex flex-col gap-2">
                        <div class="flex gap-1" :class="{ 'flex-row-reverse': isRTL }">
                          <button
                            @click="openEditModal(user)"
                            class="p-1.5 text-agri-green hover:bg-white/10 rounded transition-all"
                            :title="isRTL ? 'تعديل' : 'Modifier'"
                          >
                            ✏️
                          </button>
                          <button
                            v-if="user.status === 'ACTIVE'"
                            @click="suspendUser(user.id)"
                            class="p-1.5 text-yellow-400 hover:bg-white/10 rounded transition-all"
                            :title="isRTL ? 'تعليق' : 'Suspendre'"
                          >
                            ⚠️
                          </button>
                          <button
                            v-if="user.status === 'SUSPENDED'"
                            @click="activateUser(user.id)"
                            class="p-1.5 text-green-400 hover:bg-white/10 rounded transition-all"
                            :title="isRTL ? 'تفعيل' : 'Activer'"
                          >
                            ✅
                          </button>
                        </div>
                        <div class="flex gap-1" :class="{ 'flex-row-reverse': isRTL }">
                          <button
                            @click="openResetPasswordModal(user)"
                            class="p-1.5 text-blue-400 hover:bg-white/10 rounded transition-all"
                            :title="isRTL ? 'إعادة تعيين كلمة المرور' : 'Réinitialiser mot de passe'"
                          >
                            🔑
                          </button>
                          <button
                            @click="deleteUser(user.id)"
                            class="p-1.5 text-red-400 hover:bg-white/10 rounded transition-all"
                            :title="isRTL ? 'حذف' : 'Supprimer'"
                            :disabled="user.role === 'ADMIN' || user.role === 'SUPERADMIN'"
                            :class="{'opacity-50 cursor-not-allowed': user.role === 'ADMIN' || user.role === 'SUPERADMIN'}"
                          >
                            🗑️
                          </button>
                        </div>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>

            <!-- Pagination -->
            <div v-if="totalPages > 1" class="px-6 py-3 flex flex-col sm:flex-row sm:items-center justify-between border-t border-white/20 bg-white/5">
              <div class="text-sm text-white/80 mb-2 sm:mb-0">
                {{ isRTL ? 'عرض' : 'Affichage' }} 
                <span class="font-medium text-white">{{ startIndex + 1 }}</span> 
                {{ isRTL ? 'إلى' : 'à' }} 
                <span class="font-medium text-white">{{ Math.min(endIndex, filteredUsers.length) }}</span> 
                {{ isRTL ? 'من' : 'sur' }} 
                <span class="font-medium text-white">{{ filteredUsers.length }}</span> 
                {{ isRTL ? 'مستخدم' : 'utilisateurs' }}
              </div>
              <div class="flex items-center gap-2" :class="{ 'flex-row-reverse': isRTL }">
                <button
                  @click="prevPage"
                  :disabled="currentPage === 1"
                  class="px-3 py-1.5 rounded-md text-sm font-medium disabled:opacity-50 disabled:cursor-not-allowed text-white/80 hover:bg-white/10"
                >
                  <span v-if="isRTL">→</span>
                  <span v-else>←</span>
                  {{ isRTL ? 'السابق' : 'Précédent' }}
                </button>
                
                <div class="flex gap-1" :class="{ 'flex-row-reverse': isRTL }">
                  <button
                    v-for="page in visiblePages"
                    :key="page"
                    @click="goToPage(page)"
                    class="w-8 h-8 rounded-md text-sm font-medium"
                    :class="currentPage === page ? 'bg-agri-green text-white' : 'text-white/80 hover:bg-white/10'"
                  >
                    {{ page }}
                  </button>
                </div>
                
                <button
                  @click="nextPage"
                  :disabled="currentPage === totalPages"
                  class="px-3 py-1.5 rounded-md text-sm font-medium disabled:opacity-50 disabled:cursor-not-allowed text-white/80 hover:bg-white/10"
                >
                  {{ isRTL ? 'التالي' : 'Suivant' }}
                  <span v-if="isRTL">←</span>
                  <span v-else>→</span>
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Empty State -->
        <div 
          v-else-if="!loading && !error && users.length === 0" 
          class="agri-card p-12 text-center hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20"
        >
          <div class="text-6xl mb-6 opacity-50">👥</div>
          <h3 class="text-2xl font-bold text-white mb-3">
            {{ isRTL ? 'لا يوجد مستخدمين' : 'Aucun utilisateur trouvé' }}
          </h3>
          <p class="text-white/80 mb-8 max-w-md mx-auto">
            {{ isRTL ? 'لا يوجد مستخدمين في النظام حالياً' : 'Aucun utilisateur disponible pour le moment' }}
          </p>
          <button 
            @click="loadUsers" 
            class="px-6 py-3 agri-btn-export hover:scale-[1.02] transition-all duration-300"
          >
            {{ isRTL ? 'تحديث القائمة' : 'Actualiser la liste' }}
          </button>
        </div>
      
    </div>

    <!-- Modal d'édition -->
    <div v-if="isEditModalOpen" class="fixed inset-0 z-50 overflow-y-auto bg-black/70 backdrop-blur-sm">
      <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center">
        <div class="inline-block align-bottom bg-gray-900/95 rounded-xl text-left overflow-hidden shadow-2xl transform transition-all sm:my-8 sm:align-middle sm:max-w-2xl sm:w-full border border-white/20">
          <!-- Header -->
          <div class="px-6 pt-6 pb-4 border-b border-white/20">
            <div class="flex items-start justify-between" :class="{ 'flex-row-reverse': isRTL }">
              <div>
                <h3 class="text-xl font-semibold text-white">
                  ✏️ {{ isRTL ? 'تعديل' : 'Modifier' }} {{ editingUser?.username }}
                </h3>
                <p class="text-sm text-white/60 mt-1">ID: {{ editingUser?.id }}</p>
              </div>
              <button 
                @click="closeEditModal" 
                class="text-white/60 hover:text-white/80 p-1 hover:bg-white/10 rounded"
              >
                ✕
              </button>
            </div>
          </div>

          <!-- Formulaire -->
          <form @submit.prevent="saveUser" class="px-6 pb-6">
            <div class="space-y-6">
              <!-- Informations de base -->
              <div class="space-y-4">
                <h4 class="text-lg font-medium text-white">{{ isRTL ? 'المعلومات الأساسية' : 'Informations de base' }}</h4>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label class="block text-sm font-medium text-white/80 mb-1">
                      {{ isRTL ? 'اسم المستخدم' : "Nom d'utilisateur" }} *
                    </label>
                    <input
                      v-model="editForm.username"
                      type="text"
                      required
                      class="w-full px-3 py-2.5 bg-white/10 border border-white/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-agri-green text-white placeholder-white/50"
                    >
                  </div>
                  
                  <div>
                    <label class="block text-sm font-medium text-white/80 mb-1">
                      Email *
                    </label>
                    <input
                      v-model="editForm.email"
                      type="email"
                      required
                      class="w-full px-3 py-2.5 bg-white/10 border border-white/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-agri-green text-white placeholder-white/50"
                    >
                  </div>
                </div>
                
                <div>
                  <label class="block text-sm font-medium text-white/80 mb-1">
                    {{ isRTL ? 'رقم الهاتف' : 'Téléphone' }}
                  </label>
                  <input
                    v-model="editForm.phone"
                    type="tel"
                    :placeholder="isRTL ? '+216 XX XXX XXX' : '+216 XX XXX XXX'"
                    class="w-full px-3 py-2.5 bg-white/10 border border-white/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-agri-green text-white placeholder-white/50"
                  >
                </div>
              </div>

              <!-- Rôle et Statut -->
              <div class="space-y-4">
                <h4 class="text-lg font-medium text-white">{{ isRTL ? 'الصلاحيات' : 'Permissions' }}</h4>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label class="block text-sm font-medium text-white/80 mb-1">
                      {{ isRTL ? 'الدور' : 'Rôle' }} *
                    </label>
                    <select
                      v-model="editForm.role"
                      required
                      class="w-full px-3 py-2.5 bg-white/10 border border-white/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-agri-green text-white"
                    >
                      <option value="FARMER" class="bg-gray-800">👨‍🌾 Farmer</option>
                      <option value="BENEFICIARY" class="bg-gray-800">🏭 Beneficiary</option>
                      <option value="DUAL" class="bg-gray-800">👥 Dual</option>
                      <option value="ADMIN" class="bg-gray-800">👑 Admin</option>
                    </select>
                  </div>
                  
                  <div>
                    <label class="block text-sm font-medium text-white/80 mb-1">
                      {{ isRTL ? 'الحالة' : 'Statut' }} *
                    </label>
                    <select
                      v-model="editForm.status"
                      required
                      class="w-full px-3 py-2.5 bg-white/10 border border-white/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-agri-green text-white"
                    >
                      <option value="ACTIVE" class="bg-gray-800">✅ {{ isRTL ? 'نشط' : 'Actif' }}</option>
                      <option value="SUSPENDED" class="bg-gray-800">⚠️ {{ isRTL ? 'موقوف' : 'Suspendu' }}</option>
                      <option value="PENDING" class="bg-gray-800">⏳ {{ isRTL ? 'قيد الانتظار' : 'En attente' }}</option>
                      <option value="BLOCKED" class="bg-gray-800">❌ {{ isRTL ? 'محظور' : 'Bloqué' }}</option>
                    </select>
                  </div>
                </div>
              </div>

              <!-- Localisation -->
              <div class="space-y-4">
                <h4 class="text-lg font-medium text-white">📍 {{ isRTL ? 'الموقع' : 'Localisation' }}</h4>
                
                <div>
                  <label class="block text-sm font-medium text-white/80 mb-1">
                    {{ isRTL ? 'المدينة' : 'Ville' }} *
                  </label>
                  <select
                    v-model="editForm.city"
                    required
                    class="w-full px-3 py-2.5 bg-white/10 border border-white/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-agri-green text-white"
                  >
                    <option value="" disabled class="bg-gray-800">{{ isRTL ? 'اختر مدينة' : 'Choisir une ville' }}</option>
                    <option v-for="city in tunisianCities" :key="city" :value="city" class="bg-gray-800">{{ city }}</option>
                  </select>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label class="block text-sm font-medium text-white/80 mb-1">
                      {{ isRTL ? 'المعتمدية' : 'Délégation' }}
                    </label>
                    <input
                      v-model="editForm.delegation"
                      type="text"
                      :placeholder="isRTL ? 'مثال: وسط المدينة...' : 'ex: Centre ville...'"
                      class="w-full px-3 py-2.5 bg-white/10 border border-white/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-agri-green text-white placeholder-white/50"
                    >
                  </div>
                  
                  <div>
                    <label class="block text-sm font-medium text-white/80 mb-1">
                      {{ isRTL ? 'اسم المزرعة' : 'Nom de la ferme' }}
                    </label>
                    <input
                      v-model="editForm.farm_name"
                      type="text"
                      :placeholder="isRTL ? 'مثال: مزرعة أحمد' : 'ex: Ferme Ahmed'"
                      class="w-full px-3 py-2.5 bg-white/10 border border-white/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-agri-green text-white placeholder-white/50"
                    >
                  </div>
                </div>
                
                <div>
                  <label class="block text-sm font-medium text-white/80 mb-1">
                    {{ isRTL ? 'عنوان المزرعة' : 'Adresse de la ferme' }}
                  </label>
                  <input
                    v-model="editForm.farm_address"
                    type="text"
                    :placeholder="isRTL ? 'العنوان الكامل...' : 'Adresse complète...'"
                    class="w-full px-3 py-2.5 bg-white/10 border border-white/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-agri-green text-white placeholder-white/50"
                  >
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label class="block text-sm font-medium text-white/80 mb-1">
                      Latitude
                    </label>
                    <input
                      v-model="editForm.farm_lat"
                      type="number"
                      step="any"
                      placeholder="ex: 36.806389"
                      class="w-full px-3 py-2.5 bg-white/10 border border-white/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-agri-green text-white placeholder-white/50"
                    >
                  </div>
                  
                  <div>
                    <label class="block text-sm font-medium text-white/80 mb-1">
                      Longitude
                    </label>
                    <input
                      v-model="editForm.farm_lng"
                      type="number"
                      step="any"
                      placeholder="ex: 10.181667"
                      class="w-full px-3 py-2.5 bg-white/10 border border-white/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-agri-green text-white placeholder-white/50"
                    >
                  </div>
                </div>
              </div>

              <!-- Actions -->
              <div class="flex justify-end gap-3 pt-4 border-t border-white/20" :class="{ 'flex-row-reverse': isRTL }">
                <button
                  type="button"
                  @click="closeEditModal"
                  class="px-5 py-2.5 border border-white/20 rounded-lg text-sm font-medium text-white/80 hover:bg-white/10 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-agri-green"
                >
                  {{ isRTL ? 'إلغاء' : 'Annuler' }}
                </button>
                <button
                  type="submit"
                  :disabled="editLoading"
                  class="px-5 py-2.5 bg-agri-green border border-transparent rounded-lg text-sm font-medium text-white hover:bg-agri-green-dark focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-agri-green disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  <span v-if="editLoading">
                    <span class="inline-block animate-spin mr-2">⟳</span>
                    {{ isRTL ? 'جاري الحفظ...' : 'Enregistrement...' }}
                  </span>
                  <span v-else>
                    💾 {{ isRTL ? 'حفظ' : 'Enregistrer' }}
                  </span>
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>

    <!-- Modal Carte -->
    <div v-if="isMapModalOpen" class="fixed inset-0 z-50 overflow-y-auto bg-black/70 backdrop-blur-sm">
      <div class="flex items-center justify-center min-h-screen p-4">
        <div class="inline-block align-bottom bg-gray-900/95 rounded-xl text-left overflow-hidden shadow-2xl transform transition-all w-full max-w-4xl border border-white/20">
          <!-- Header -->
          <div class="px-6 pt-6 pb-4 border-b border-white/20">
            <div class="flex items-start justify-between" :class="{ 'flex-row-reverse': isRTL }">
              <div>
                <h3 class="text-xl font-semibold text-white">🗺️ {{ isRTL ? 'موقع' : 'Localisation de' }} {{ selectedUser?.username }}</h3>
                <p class="text-sm text-white/60 mt-1">
                  {{ selectedUser?.farm_address || (isRTL ? 'لا يوجد عنوان' : 'Pas d\'adresse') }}
                </p>
              </div>
              <button 
                @click="closeMapModal" 
                class="text-white/60 hover:text-white/80 p-1 hover:bg-white/10 rounded"
              >
                ✕
              </button>
            </div>
          </div>
          
          <!-- Carte -->
          <div class="px-6 pb-6">
            <div class="h-96 bg-gray-800 rounded-lg flex items-center justify-center border border-white/20">
              <div class="text-center">
                <div class="text-4xl mb-4 text-white/50">🗺️</div>
                <p class="text-white/70">{{ isRTL ? 'خريطة الموقع' : 'Carte de localisation' }}</p>
                <p class="text-sm text-white/50 mt-2">
                  {{ isRTL ? 'خط العرض' : 'Lat' }}: {{ selectedUser?.farm_lat ? parseFloat(selectedUser.farm_lat).toFixed(6) : 'N/A' }}, 
                  {{ isRTL ? 'خط الطول' : 'Lng' }}: {{ selectedUser?.farm_lng ? parseFloat(selectedUser.farm_lng).toFixed(6) : 'N/A' }}
                </p>
                <div class="mt-4 space-y-2">
                  <button
                    @click="openGoogleMaps(selectedUser)"
                    class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 text-sm font-medium"
                  >
                    📍 {{ isRTL ? 'فتح في خرائط Google' : 'Ouvrir dans Google Maps' }}
                  </button>
                  <button
                    @click="copyCoordinates(selectedUser)"
                    class="px-4 py-2 bg-white/10 text-white/80 rounded-lg hover:bg-white/20 text-sm font-medium"
                  >
                    📋 {{ isRTL ? 'نسخ الإحداثيات' : 'Copier les coordonnées' }}
                  </button>
                </div>
              </div>
            </div>
            
            <!-- Informations -->
            <div class="mt-4 grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="p-4 bg-white/5 rounded-lg border border-white/20">
                <h4 class="font-medium text-white mb-2">📍 {{ isRTL ? 'إحداثيات GPS' : 'Coordonnées GPS' }}</h4>
                <div class="space-y-1">
                  <div class="flex justify-between" :class="{ 'flex-row-reverse': isRTL }">
                    <span class="text-sm text-white/60">{{ isRTL ? 'خط العرض:' : 'Latitude:' }}</span>
                    <span class="text-sm font-mono text-white">{{ selectedUser?.farm_lat ? parseFloat(selectedUser.farm_lat).toFixed(6) : 'N/A' }}</span>
                  </div>
                  <div class="flex justify-between" :class="{ 'flex-row-reverse': isRTL }">
                    <span class="text-sm text-white/60">{{ isRTL ? 'خط الطول:' : 'Longitude:' }}</span>
                    <span class="text-sm font-mono text-white">{{ selectedUser?.farm_lng ? parseFloat(selectedUser.farm_lng).toFixed(6) : 'N/A' }}</span>
                  </div>
                </div>
              </div>
              
              <div class="p-4 bg-white/5 rounded-lg border border-white/20">
                <h4 class="font-medium text-white mb-2">🏠 {{ isRTL ? 'الموقع' : 'Localisation' }}</h4>
                <p class="text-sm text-white/80">{{ selectedUser?.farm_address || (isRTL ? 'لا يوجد عنوان' : 'Pas d\'adresse') }}</p>
                <p v-if="selectedUser?.city" class="text-sm text-white/60 mt-1">
                  {{ isRTL ? 'المدينة' : 'Ville' }}: {{ selectedUser.city }}
                </p>
                <p v-if="selectedUser?.delegation" class="text-sm text-white/60">
                  {{ isRTL ? 'المعتمدية' : 'Délégation' }}: {{ selectedUser.delegation }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal Réinitialisation mot de passe -->
    <div v-if="isResetPasswordModalOpen" class="fixed inset-0 z-50 overflow-y-auto bg-black/70 backdrop-blur-sm">
      <div class="flex items-center justify-center min-h-screen p-4">
        <div class="inline-block align-bottom bg-gray-900/95 rounded-xl text-left overflow-hidden shadow-2xl transform transition-all w-full max-w-md border border-white/20">
          <div class="px-6 pt-6 pb-4 border-b border-white/20">
            <div class="flex items-start justify-between" :class="{ 'flex-row-reverse': isRTL }">
              <div>
                <h3 class="text-xl font-semibold text-white">🔑 {{ isRTL ? 'إعادة تعيين كلمة المرور' : 'Réinitialiser mot de passe' }}</h3>
                <p class="text-sm text-white/60 mt-1">{{ selectedUser?.username }}</p>
              </div>
              <button @click="closeResetPasswordModal" class="text-white/60 hover:text-white/80 p-1 hover:bg-white/10 rounded">
                ✕
              </button>
            </div>
          </div>
          
          <div class="px-6 pb-6">
            <div class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-white/80 mb-1">
                  {{ isRTL ? 'كلمة المرور الجديدة' : 'Nouveau mot de passe' }} *
                </label>
                <input
                  v-model="newPassword"
                  type="password"
                  required
                  class="w-full px-3 py-2.5 bg-white/10 border border-white/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-agri-green text-white placeholder-white/50"
                  :placeholder="isRTL ? '8 أحرف على الأقل' : 'Minimum 8 caractères'"
                >
                <p class="text-xs text-white/50 mt-1">
                  {{ isRTL ? 'يجب أن يحتوي على أحرف كبيرة وصغيرة وأرقام ورموز خاصة' : 'Inclure majuscules, minuscules, chiffres et caractères spéciaux' }}
                </p>
              </div>
              
              <div>
                <label class="block text-sm font-medium text-white/80 mb-1">
                  {{ isRTL ? 'تأكيد كلمة المرور' : 'Confirmer le mot de passe' }} *
                </label>
                <input
                  v-model="confirmPassword"
                  type="password"
                  required
                  class="w-full px-3 py-2.5 bg-white/10 border border-white/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-agri-green text-white"
                >
              </div>
              
              <div v-if="passwordError" class="p-3 bg-red-900/30 border border-red-400/20 rounded-lg">
                <p class="text-sm text-red-300">{{ passwordError }}</p>
              </div>
              
              <div class="flex justify-end gap-3 pt-4 border-t border-white/20" :class="{ 'flex-row-reverse': isRTL }">
                <button
                  type="button"
                  @click="closeResetPasswordModal"
                  class="px-5 py-2.5 border border-white/20 rounded-lg text-sm font-medium text-white/80 hover:bg-white/10"
                >
                  {{ isRTL ? 'إلغاء' : 'Annuler' }}
                </button>
                <button
                  type="button"
                  @click="resetPassword"
                  :disabled="resetLoading"
                  class="px-5 py-2.5 bg-blue-600 border border-transparent rounded-lg text-sm font-medium text-white hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  <span v-if="resetLoading">
                    <span class="inline-block animate-spin mr-2">⟳</span>
                    {{ isRTL ? 'جاري...' : 'Réinitialisation...' }}
                  </span>
                  <span v-else>
                    🔑 {{ isRTL ? 'إعادة تعيين' : 'Réinitialiser' }}
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, reactive, onMounted, watch } from 'vue';
import { useAuthStore } from '../../store/auth';
import { useI18n } from 'vue-i18n';
import { 
  getUsers, 
  updateUser, 
  deleteUser as deleteUserAPI,
  suspendUser as suspendUserAPI,
  activateUser as activateUserAPI,
  resetUserPassword,
  exportUsersExcel as exportUsersExcelAPI
} from '../../api/exports';

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

// Données principales
const users = ref([]);
const loading = ref(true);
const error = ref('');

// Filtres
const searchQuery = ref('');
const roleFilter = ref('');
const statusFilter = ref('');
const cityFilter = ref('');
const delegationFilter = ref('');

// Tri
const sortField = ref('date_joined');
const sortDirection = ref('desc');

// Pagination
const currentPage = ref(1);
const pageSize = ref(15);

// Modals
const isEditModalOpen = ref(false);
const isMapModalOpen = ref(false);
const isResetPasswordModalOpen = ref(false);
const selectedUser = ref(null);
const editingUser = ref(null);

// Formulaire d'édition
const editForm = reactive({
  username: '',
  email: '',
  phone: '',
  role: 'FARMER',
  status: 'ACTIVE',
  city: '',
  delegation: '',
  farm_name: '',
  farm_address: '',
  farm_lat: '',
  farm_lng: ''
});

// Réinitialisation mot de passe
const newPassword = ref('');
const confirmPassword = ref('');
const passwordError = ref('');
const resetLoading = ref(false);
const editLoading = ref(false);

// Export Excel
const exportingExcel = ref(false);

// Liste des 24 villes de Tunisie
const tunisianCities = [
  "Tunis", "Sfax", "Sousse", "Ariana", "Bizerte", "Gabès", "Kairouan", "Kasserine",
  "Kebili", "Mahdia", "Manouba", "Medenine", "Monastir", "Nabeul", "Tataouine", 
  "Tozeur", "Zaghouan", "Jendouba", "Beja", "Gafsa", "Siliana", "Sidi Bouzid", 
  "Ben Arous", "El Kef"
];

// Computed properties
const filteredUsers = computed(() => {
  let filtered = [...users.value];
  
  if (searchQuery.value) {
    const term = searchQuery.value.toLowerCase();
    filtered = filtered.filter(user => 
      user.username.toLowerCase().includes(term) ||
      user.email.toLowerCase().includes(term) ||
      (user.phone && user.phone.toLowerCase().includes(term)) ||
      (user.farm_name && user.farm_name.toLowerCase().includes(term)) ||
      (user.farm_address && user.farm_address.toLowerCase().includes(term)) ||
      (user.city && user.city.toLowerCase().includes(term)) ||
      (user.delegation && user.delegation.toLowerCase().includes(term))
    );
  }
  
  if (roleFilter.value) {
    filtered = filtered.filter(user => user.role === roleFilter.value);
  }
  
  if (statusFilter.value) {
    filtered = filtered.filter(user => user.status === statusFilter.value);
  }
  
  if (cityFilter.value) {
    filtered = filtered.filter(user => user.city === cityFilter.value);
  }
  
  if (delegationFilter.value) {
    const term = delegationFilter.value.toLowerCase();
    filtered = filtered.filter(user => 
      user.delegation && user.delegation.toLowerCase().includes(term)
    );
  }
  
  // Tri
  filtered.sort((a, b) => {
    let aVal = a[sortField.value];
    let bVal = b[sortField.value];
    
    if (sortField.value === 'date_joined' || sortField.value === 'last_login' || sortField.value === 'updated_at') {
      aVal = aVal ? new Date(aVal) : new Date(0);
      bVal = bVal ? new Date(bVal) : new Date(0);
    }
    
    if (aVal === null || aVal === undefined) aVal = '';
    if (bVal === null || bVal === undefined) bVal = '';
    
    if (typeof aVal === 'string') aVal = aVal.toLowerCase();
    if (typeof bVal === 'string') bVal = bVal.toLowerCase();
    
    if (aVal < bVal) return sortDirection.value === 'asc' ? -1 : 1;
    if (aVal > bVal) return sortDirection.value === 'asc' ? 1 : -1;
    return 0;
  });
  
  return filtered;
});

const stats = computed(() => {
  const filtered = filteredUsers.value;
  return {
    active: filtered.filter(u => u.status === 'ACTIVE').length,
    farmers: filtered.filter(u => u.role === 'FARMER').length,
    beneficiaries: filtered.filter(u => u.role === 'BENEFICIARY').length,
    dual: filtered.filter(u => u.role === 'DUAL').length,
    admins: filtered.filter(u => ['ADMIN', 'SUPERADMIN'].includes(u.role)).length
  };
});

const totalPages = computed(() => Math.ceil(filteredUsers.value.length / pageSize.value));
const paginatedUsers = computed(() => {
  const start = (currentPage.value - 1) * pageSize.value;
  const end = start + pageSize.value;
  return filteredUsers.value.slice(start, end);
});
const startIndex = computed(() => (currentPage.value - 1) * pageSize.value);
const endIndex = computed(() => Math.min(currentPage.value * pageSize.value, filteredUsers.value.length));
const visiblePages = computed(() => {
  const pages = [];
  const maxVisible = 5;
  let start = Math.max(1, currentPage.value - Math.floor(maxVisible / 2));
  let end = Math.min(totalPages.value, start + maxVisible - 1);
  
  if (end - start + 1 < maxVisible) {
    start = Math.max(1, end - maxVisible + 1);
  }
  
  for (let i = start; i <= end; i++) {
    pages.push(i);
  }
  return pages;
});

// Fonctions utilitaires
function getUserInitials(username) {
  return username ? username.substring(0, 2).toUpperCase() : '?';
}

function getRoleLabel(role) {
  const labels = {
    'FARMER': isRTL.value ? 'مزارع' : 'Agriculteur',
    'BENEFICIARY': isRTL.value ? 'مستفيد' : 'Bénéficiaire',
    'DUAL': 'Dual',
    'ADMIN': isRTL.value ? 'مدير' : 'Admin',
    'SUPERADMIN': isRTL.value ? 'مدير عام' : 'Super Admin'
  };
  return labels[role] || role;
}

function getStatusLabel(status) {
  const labels = {
    'ACTIVE': isRTL.value ? 'نشط' : 'Actif',
    'SUSPENDED': isRTL.value ? 'موقوف' : 'Suspendu',
    'PENDING': isRTL.value ? 'قيد الانتظار' : 'En attente',
    'BLOCKED': isRTL.value ? 'محظور' : 'Bloqué'
  };
  return labels[status] || status;
}

function getRoleBadgeClass(role) {
  const classes = {
    'FARMER': 'bg-green-500/20 text-green-200 border border-green-400/20',
    'BENEFICIARY': 'bg-blue-500/20 text-blue-200 border border-blue-400/20',
    'DUAL': 'bg-purple-500/20 text-purple-200 border border-purple-400/20',
    'ADMIN': 'bg-yellow-500/20 text-yellow-200 border border-yellow-400/20',
    'SUPERADMIN': 'bg-red-500/20 text-red-200 border border-red-400/20'
  };
  return classes[role] || 'bg-gray-500/20 text-gray-200 border border-gray-400/20';
}

function getStatusBadgeClass(status) {
  const classes = {
    'ACTIVE': 'bg-green-500/20 text-green-200 border border-green-400/20',
    'SUSPENDED': 'bg-yellow-500/20 text-yellow-200 border border-yellow-400/20',
    'PENDING': 'bg-blue-500/20 text-blue-200 border border-blue-400/20',
    'BLOCKED': 'bg-red-500/20 text-red-200 border border-red-400/20'
  };
  return classes[status] || 'bg-gray-500/20 text-gray-200 border border-gray-400/20';
}

function formatDate(dateString) {
  if (!dateString) return 'N/A';
  try {
    return new Date(dateString).toLocaleDateString(lang.value === 'ar' ? 'ar-TN' : 'fr-FR', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  } catch {
    return dateString;
  }
}

function getDaysAgo(dateString) {
  if (!dateString) return '';
  try {
    const days = Math.floor((new Date() - new Date(dateString)) / (1000 * 60 * 60 * 24));
    if (days === 0) return isRTL.value ? "اليوم" : "Aujourd'hui";
    if (days === 1) return isRTL.value ? "أمس" : "Hier";
    if (days < 7) return isRTL.value ? `منذ ${days} أيام` : `Il y a ${days} jours`;
    if (days < 30) return isRTL.value ? `منذ ${Math.floor(days/7)} أسابيع` : `Il y a ${Math.floor(days/7)} semaines`;
    if (days < 365) return isRTL.value ? `منذ ${Math.floor(days/30)} أشهر` : `Il y a ${Math.floor(days/30)} mois`;
    return isRTL.value ? `منذ ${Math.floor(days/365)} سنوات` : `Il y a ${Math.floor(days/365)} ans`;
  } catch {
    return '';
  }
}

function truncateText(text, maxLength) {
  if (!text) return '';
  if (text.length <= maxLength) return text;
  return text.substring(0, maxLength) + '...';
}

// Tri
function sortBy(field) {
  if (sortField.value === field) {
    sortDirection.value = sortDirection.value === 'asc' ? 'desc' : 'asc';
  } else {
    sortField.value = field;
    sortDirection.value = 'desc';
  }
}

// Fonctions de pagination
function nextPage() {
  if (currentPage.value < totalPages.value) currentPage.value++;
}

function prevPage() {
  if (currentPage.value > 1) currentPage.value--;
}

function goToPage(page) {
  currentPage.value = page;
}

// Fonctions modales
function openEditModal(user) {
  editingUser.value = user;
  Object.keys(editForm).forEach(key => {
    editForm[key] = user[key] || '';
  });
  isEditModalOpen.value = true;
}

function closeEditModal() {
  isEditModalOpen.value = false;
  editingUser.value = null;
  Object.keys(editForm).forEach(key => {
    editForm[key] = '';
  });
  editForm.role = 'FARMER';
  editForm.status = 'ACTIVE';
}

async function saveUser() {
  editLoading.value = true;
  try {
    await updateUser(editingUser.value.id, editForm);
    await loadUsers();
    closeEditModal();
  } catch (error) {
    console.error('Erreur modification:', error);
    alert(isRTL.value ? 'خطأ في التعديل: ' + (error.response?.data?.detail || error.message) : 'Erreur lors de la modification: ' + (error.response?.data?.detail || error.message));
  } finally {
    editLoading.value = false;
  }
}

function viewOnMap(user) {
  selectedUser.value = user;
  isMapModalOpen.value = true;
}

function closeMapModal() {
  isMapModalOpen.value = false;
  selectedUser.value = null;
}

function openGoogleMaps(user) {
  if (user.farm_lat && user.farm_lng) {
    const url = `https://www.google.com/maps?q=${user.farm_lat},${user.farm_lng}`;
    window.open(url, '_blank');
  }
}

function copyCoordinates(user) {
  if (user.farm_lat && user.farm_lng) {
    const text = `${user.farm_lat}, ${user.farm_lng}`;
    navigator.clipboard.writeText(text);
    alert(isRTL.value ? 'تم نسخ الإحداثيات: ' + text : 'Coordonnées copiées: ' + text);
  }
}

function copyAddress(address) {
  navigator.clipboard.writeText(address);
  alert(isRTL.value ? 'تم نسخ العنوان: ' + address : 'Adresse copiée: ' + address);
}

function openResetPasswordModal(user) {
  selectedUser.value = user;
  isResetPasswordModalOpen.value = true;
}

function closeResetPasswordModal() {
  isResetPasswordModalOpen.value = false;
  selectedUser.value = null;
  newPassword.value = '';
  confirmPassword.value = '';
  passwordError.value = '';
}

async function resetPassword() {
  if (!newPassword.value || !confirmPassword.value) {
    passwordError.value = isRTL.value ? 'يرجى ملء جميع الحقول' : 'Veuillez remplir tous les champs';
    return;
  }
  
  if (newPassword.value !== confirmPassword.value) {
    passwordError.value = isRTL.value ? 'كلمات المرور غير متطابقة' : 'Les mots de passe ne correspondent pas';
    return;
  }
  
  if (newPassword.value.length < 8) {
    passwordError.value = isRTL.value ? 'يجب أن تحتوي كلمة المرور على 8 أحرف على الأقل' : 'Le mot de passe doit contenir au moins 8 caractères';
    return;
  }
  
  resetLoading.value = true;
  passwordError.value = '';
  
  try {
    await resetUserPassword(selectedUser.value.id, { new_password: newPassword.value });
    closeResetPasswordModal();
    alert(isRTL.value ? '✅ تم إعادة تعيين كلمة المرور بنجاح' : '✅ Mot de passe réinitialisé avec succès');
  } catch (error) {
    console.error('Erreur réinitialisation:', error);
    passwordError.value = (isRTL.value ? 'خطأ: ' : 'Erreur: ') + (error.response?.data?.detail || error.message);
  } finally {
    resetLoading.value = false;
  }
}

// Fonctions API
async function loadUsers() {
  loading.value = true;
  error.value = '';
  try {
    const response = await getUsers();
    users.value = response.data || [];
  } catch (error) {
    console.error('Erreur chargement utilisateurs:', error);
    error.value = isRTL.value ? 'غير قادر على تحميل المستخدمين.' : 'Impossible de charger les utilisateurs.';
  } finally {
    loading.value = false;
  }
}

async function suspendUser(userId) {
  if (!confirm(isRTL.value ? 'هل أنت متأكد من تعليق هذا المستخدم؟' : 'Êtes-vous sûr de vouloir suspendre cet utilisateur ?')) return;
  
  try {
    await suspendUserAPI(userId);
    await loadUsers();
    alert(isRTL.value ? '✅ تم تعليق المستخدم' : '✅ Utilisateur suspendu');
  } catch (error) {
    console.error('Erreur suspension:', error);
    alert(isRTL.value ? 'خطأ في تعليق المستخدم' : 'Erreur lors de la suspension');
  }
}

async function activateUser(userId) {
  try {
    await activateUserAPI(userId);
    await loadUsers();
    alert(isRTL.value ? '✅ تم تفعيل المستخدم' : '✅ Utilisateur activé');
  } catch (error) {
    console.error('Erreur activation:', error);
    alert(isRTL.value ? 'خطأ في تفعيل المستخدم' : 'Erreur lors de l\'activation');
  }
}

async function deleteUser(userId) {
  const user = users.value.find(u => u.id === userId);
  if (!user) return;
  
  if (user.role === 'ADMIN' || user.role === 'SUPERADMIN') {
    alert(isRTL.value ? '❌ لا يمكن حذف مسؤول' : '❌ Impossible de supprimer un administrateur');
    return;
  }
  
  if (!confirm(isRTL.value ? `هل أنت متأكد من حذف المستخدم "${user.username}"؟ هذا الإجراء لا يمكن التراجع عنه.` : `Êtes-vous sûr de vouloir supprimer l'utilisateur "${user.username}" ? Cette action est irréversible.`)) return;
  
  try {
    await deleteUserAPI(userId);
    await loadUsers();
    alert(isRTL.value ? '✅ تم حذف المستخدم' : '✅ Utilisateur supprimé');
  } catch (error) {
    console.error('Erreur suppression:', error);
    alert(isRTL.value ? 'خطأ في حذف المستخدم' : 'Erreur lors de la suppression');
  }
}

function resetFilters() {
  searchQuery.value = '';
  roleFilter.value = '';
  statusFilter.value = '';
  cityFilter.value = '';
  delegationFilter.value = '';
  sortField.value = 'date_joined';
  sortDirection.value = 'desc';
  currentPage.value = 1;
}

function debouncedSearch() {
  currentPage.value = 1;
}

async function handleExportExcel() {
  if (filteredUsers.value.length === 0) {
    alert(isRTL.value ? '⚠️ لا يوجد مستخدمين للتصدير' : '⚠️ Aucun utilisateur à exporter');
    return;
  }

  exportingExcel.value = true;
  try {
    const filters = {
      role: roleFilter.value || undefined,
      status: statusFilter.value || undefined,
      governorate: cityFilter.value || undefined,
      delegation: delegationFilter.value || undefined
    };

    const response = await exportUsersExcelAPI(filters);
    
    const url = window.URL.createObjectURL(response.data);
    const link = document.createElement('a');
    link.href = url;
    link.download = `utilisateurs_agricycle_${new Date().toISOString().split('T')[0]}.xlsx`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    window.URL.revokeObjectURL(url);
    
  } catch (error) {
    console.error('Erreur export Excel:', error);
    
    if (error.response?.status === 500) {
      alert(isRTL.value ? '❌ خطأ في الخادم أثناء إنشاء ملف Excel' : '❌ Erreur serveur lors de la génération du fichier Excel');
    } else {
      alert(isRTL.value ? '❌ خطأ في إنشاء ملف Excel' : '❌ Erreur lors de la génération du fichier Excel');
    }
  } finally {
    exportingExcel.value = false;
  }
}

// Watch pour réinitialiser la page quand les filtres changent
watch([searchQuery, roleFilter, statusFilter, cityFilter, delegationFilter], () => {
  currentPage.value = 1;
});

// Lifecycle
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
  
  loadUsers();
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
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
  background: rgba(255, 255, 255, 0.15);
  border-color: rgba(255, 255, 255, 0.3);
}

/* Input style */
.agri-input, .agri-select {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  padding: 10px 16px;
  color: white;
  font-size: 14px;
  transition: all 0.3s ease;
  outline: none;
}

.agri-input:focus, .agri-select:focus {
  border-color: rgba(255, 255, 255, 0.5);
  box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.1);
}

.agri-input::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

.agri-select option {
  background: #1f2937;
  color: white;
}

/* Boutons d'export */
.agri-btn-export {
  background: linear-gradient(135deg, #48bb78 0%, #2f855a 100%);
  color: white;
  font-weight: 600;
  box-shadow: 0 4px 15px rgba(72, 187, 120, 0.3);
  border: none;
  border-radius: 10px;
  padding: 12px 24px;
  transition: all 0.3s ease;
}

.agri-btn-export:hover:not(:disabled) {
  box-shadow: 0 8px 25px rgba(72, 187, 120, 0.4);
  transform: translateY(-2px);
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

[dir="rtl"] .ml-4 {
  margin-left: 0;
  margin-right: 1rem;
}

[dir="rtl"] .mr-4 {
  margin-right: 0;
  margin-left: 1rem;
}

[dir="rtl"] .text-left {
  text-align: right !important;
}

[dir="rtl"] .text-right {
  text-align: left !important;
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
  
  table {
    font-size: 0.875rem;
  }
  
  .px-6 {
    padding-left: 1rem;
    padding-right: 1rem;
  }
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

/* Style pour bouton désactivé */
button:disabled {
  cursor: not-allowed;
  pointer-events: none;
  opacity: 0.5;
}

/* Table styles */
table {
  border-collapse: separate;
  border-spacing: 0;
}

th {
  font-weight: 600;
  letter-spacing: 0.05em;
}

td {
  vertical-align: middle;
}
</style>