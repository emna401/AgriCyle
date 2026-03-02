<template>
  <div class="relative min-h-screen">
    <!-- Image d'arrière-plan fixe -->
    <div 
      class="fixed inset-0 bg-cover bg-center bg-no-repeat"
      style="background-image: url('https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80')"
    >
      <div class="absolute inset-0 bg-black/40"></div>
    </div>
    
    <!-- Contenu par-dessus l'image -->
    <div class="relative z-10 min-h-screen flex items-center justify-center px-4 py-8">
      <div class="w-full max-w-md">
        <!-- Carte de connexion -->
        <div class="bg-white/10 backdrop-blur-xl p-8 rounded-3xl shadow-2xl border border-white/30">
          <!-- Titre et sous-titre -->
          <div class="text-center mb-8">
            <h1 class="text-3xl font-bold text-white mb-2">
              {{ isRTL ? 'تسجيل الدخول' : 'Connexion' }}
            </h1>
            <p class="text-white/90">
              {{ isRTL ? 'دخول آمن إلى مساحة AgriCycle الخاصة بك' : 'Accès sécurisé à votre espace AgriCycle' }}
            </p>
          </div>

          <!-- Navigation -->
          <div class="flex justify-between items-center mb-6">
            <button @click="goBack" class="text-sm text-white/80 hover:text-white hover:underline flex items-center">
              <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
              </svg>
              {{ isRTL ? 'رجوع' : 'Retour' }}
            </button>
            <router-link to="/register" class="text-sm text-white/80 hover:text-agri-green-light hover:underline">
              {{ isRTL ? 'إنشاء حساب' : 'Créer un compte' }}
            </router-link>
          </div>

          <!-- Formulaire de connexion -->
          <form @submit.prevent="handleLogin" class="space-y-6">
            <!-- Email -->
            <div>
              <label class="block text-white/90 text-sm font-medium mb-2">
                {{ isRTL ? 'البريد الإلكتروني' : 'Email' }} *
              </label>
              <input
                v-model="email"
                type="email"
                :placeholder="isRTL ? 'example@email.com' : 'email@example.com'"
                :class="['w-full px-4 py-3 bg-white/10 backdrop-blur-sm border rounded-lg text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-agri-green-light', 
                        error ? 'border-red-400' : 'border-white/20']"
                required
              />
            </div>

            <!-- Mot de passe -->
            <div>
              <div class="flex justify-between items-center mb-2">
                <label class="block text-white/90 text-sm font-medium">
                  {{ isRTL ? 'كلمة المرور' : 'Mot de passe' }} *
                </label>
                <router-link to="/forgot-password" class="text-xs text-white/80 hover:text-agri-green-light hover:underline">
                  {{ isRTL ? 'نسيت كلمة المرور؟' : 'Mot de passe oublié ?' }}
                </router-link>
              </div>
              <input
                v-model="password"
                type="password"
                placeholder="••••••••"
                :class="['w-full px-4 py-3 bg-white/10 backdrop-blur-sm border rounded-lg text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-agri-green-light', 
                        error ? 'border-red-400' : 'border-white/20']"
                required
              />
            </div>

            <!-- Message d'erreur -->
            <div v-if="error" class="p-4 bg-red-500/20 backdrop-blur-sm border border-red-400/30 rounded-lg">
              <p class="text-red-200 text-sm text-center">{{ error }}</p>
            </div>

            <!-- Message de succès -->
            <div v-if="success" class="p-4 bg-green-500/20 backdrop-blur-sm border border-green-400/30 rounded-lg">
              <p class="text-green-200 text-sm text-center">{{ success }}</p>
            </div>

            <!-- Bouton de connexion -->
            <button
              type="submit"
              :disabled="loading"
              :class="['w-full py-4 rounded-xl font-semibold text-lg transition-all duration-300',
                      loading 
                        ? 'bg-gray-400 cursor-not-allowed' 
                        : 'agri-btn-header hover:scale-[1.02]']"
            >
              <span v-if="loading" class="flex items-center justify-center">
                <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                {{ isRTL ? 'جاري الاتصال...' : 'Connexion...' }}
              </span>
              <span v-else>{{ isRTL ? 'تسجيل الدخول' : 'Se connecter' }}</span>
            </button>

            <!-- Séparateur -->
            <div class="relative flex items-center justify-center">
              <div class="flex-grow border-t border-white/20"></div>
              <span class="mx-4 text-white/60 text-sm">{{ isRTL ? 'أو' : 'Ou' }}</span>
              <div class="flex-grow border-t border-white/20"></div>
            </div>

            <!-- Options supplémentaires -->
            <div class="text-center">
              <p class="text-white/70 text-sm mb-4">
                {{ isRTL ? 'جديد في AgriCycle ؟' : 'Nouveau sur AgriCycle ?' }}
              </p>
              <router-link 
                to="/register" 
                class="inline-block w-full py-3 rounded-lg border-2 border-white text-white font-medium hover:bg-white hover:text-agri-green-dark transition-all duration-300"
              >
                {{ isRTL ? 'إنشاء حساب جديد' : 'Créer un nouveau compte' }}
              </router-link>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "../../store/auth";
import { supabase } from "../../lib/supabase";

const router = useRouter();
const auth = useAuthStore();

const email = ref("");
const password = ref("");
const error = ref("");
const success = ref("");
const loading = ref(false);

// RTL support
const isRTL = computed(() => {
  return localStorage.getItem('lang') === 'ar';
});

function goBack() {
  router.push("/");
}

async function handleLogin() {
  error.value = "";
  success.value = "";
  loading.value = true;
  
  // Validation
  if (!email.value || !password.value) {
    error.value = isRTL.value ? "يرجى ملء جميع الحقول" : "Veuillez remplir tous les champs";
    loading.value = false;
    return;
  }

  try {
    // Connexion avec Supabase
    const { data, error: supabaseError } = await supabase.auth.signInWithPassword({
      email: email.value,
      password: password.value
    });
    
    if (supabaseError) throw supabaseError;
    
    if (data.user) {
      console.log("Login successful:", data);
      
      // Récupérer les métadonnées de l'utilisateur
      const userMetadata = data.user.user_metadata || {};
      const role = userMetadata.role || 'DUAL'; // Par défaut DUAL si non spécifié
      const username = userMetadata.username || email.value.split('@')[0];
      
      // Créer l'objet utilisateur pour votre store
      const userData = {
        id: data.user.id,
        email: data.user.email,
        role: role,
        username: username,
        farm_name: userMetadata.farm_name || '',
        farm_address: userMetadata.farm_address || '',
        governorate: userMetadata.governorate || '',
        delegation: userMetadata.delegation || ''
      };
      
      // Sauvegarder dans le store et localStorage
      auth.setUser(userData);
      localStorage.setItem('token', data.session.access_token);
      localStorage.setItem('supabase.auth.token', JSON.stringify(data.session));
      
      success.value = isRTL.value ? "تم تسجيل الدخول بنجاح!" : "Connexion réussie!";
      
      // Redirection selon le rôle
      setTimeout(() => {
        if (role === "FARMER") router.push("/app/farmer");
        else if (role === "BENEFICIARY") router.push("/app/beneficiary");
        else if (role === "DUAL") router.push("/app/dual");
        else if (role === "ADMIN" || role === "SUPERADMIN") router.push("/app/admin");
        else router.push("/app/profile");
      }, 1000);
    }
  } catch (e) {
    console.error("Login error:", e);
    
    // Gestion des erreurs Supabase
    if (e.message?.includes('Invalid login credentials')) {
      error.value = isRTL.value 
        ? "بريد إلكتروني أو كلمة مرور غير صحيحة" 
        : "Email ou mot de passe incorrect";
    } else if (e.message?.includes('Email not confirmed')) {
      error.value = isRTL.value 
        ? "يرجى تأكيد بريدك الإلكتروني أولاً" 
        : "Veuillez confirmer votre email d'abord";
    } else {
      error.value = isRTL.value 
        ? "خطأ في الاتصال. حاول مرة أخرى." 
        : e.message || "Erreur de connexion";
    }
  } finally {
    loading.value = false;
  }
}

// Pour le développement, vous pouvez ajouter un compte de test
if (import.meta.env.DEV) {
  // Remplir automatiquement pour les tests
  email.value = 'test@agricycle.com';
  password.value = 'password123';
}
</script>

<style scoped>
/* Assurer que l'image couvre toute la page */
.fixed {
  position: fixed;
}

.inset-0 {
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}

/* Centrage vertical et horizontal */
.min-h-screen {
  min-height: 100vh;
}

.flex.items-center.justify-center {
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Couleur verte claire */
.text-agri-green-light {
  color: #68d391;
}

.text-agri-green-dark {
  color: #2f855a;
}

/* Styles pour les boutons */
.agri-btn-header {
  background: linear-gradient(135deg, #48bb78 0%, #2f855a 100%);
  color: white;
  border-radius: 12px;
  transition: all 0.3s ease;
  border: none;
  cursor: pointer;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 10px 25px rgba(72, 187, 120, 0.3);
}

.agri-btn-header:hover:not(:disabled) {
  transform: translateY(-3px);
  box-shadow: 0 15px 35px rgba(72, 187, 120, 0.4);
  background: linear-gradient(135deg, #5cc489 0%, #3a9a6b 100%);
}

/* Animation de rotation */
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.animate-spin {
  animation: spin 1s linear infinite;
}

/* Effet de texte avec ombre */
.text-white {
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

/* Placeholder blanc */
::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

/* Focus styles */
input:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(104, 211, 145, 0.3);
}

/* Style pour le lien "Créer un compte" */
.border-white {
  border-color: rgba(255, 255, 255, 0.5);
}

.border-white:hover {
  background-color: white;
}

/* RTL Support */
[dir="rtl"] .flex {
  flex-direction: row-reverse;
}

[dir="rtl"] .mr-1 {
  margin-right: 0;
  margin-left: 0.25rem;
}

/* Responsive */
@media (max-width: 640px) {
  .max-w-md {
    max-width: 100%;
  }
  
  .p-8 {
    padding: 1.5rem;
  }
  
  .text-3xl {
    font-size: 1.75rem;
  }
  
  .space-y-6 > * + * {
    margin-top: 1rem;
  }
  
  .py-4 {
    padding-top: 1rem;
    padding-bottom: 1rem;
  }
  
  .py-3 {
    padding-top: 0.75rem;
    padding-bottom: 0.75rem;
  }
}
</style>