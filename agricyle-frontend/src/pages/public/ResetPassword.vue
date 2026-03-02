<template>
  <!-- Image d'arrière-plan fixe (même que la page d'accueil) -->
  <div 
    class="fixed inset-0 bg-cover bg-center bg-no-repeat"
    style="background-image: url('https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80')"
  >
    <!-- Overlay sombre pour améliorer la lisibilité -->
    <div class="absolute inset-0 bg-black/40"></div>
  </div>
  
  <!-- Contenu par-dessus l'image -->
  <div class="relative z-10 min-h-screen flex flex-col">
    <div class="flex-1 flex items-center justify-center p-4">
      <div class="agri-card bg-white/10 backdrop-blur-lg p-8 rounded-2xl shadow-2xl border border-white/20 w-full max-w-md">
        
        <!-- En-tête -->
        <div class="text-center mb-8">
          <h2 class="text-3xl font-bold text-white mb-2">Réinitialisation du mot de passe</h2>
          <p class="text-white/80">Entrez le code OTP reçu par email et votre nouveau mot de passe</p>
        </div>
        
        <!-- Formulaire -->
        <form @submit.prevent="handleReset" class="space-y-5">
          <!-- Email (pré-rempli depuis l'URL) -->
          <div>
            <label class="block text-sm font-medium text-white/90 mb-2">Email</label>
            <div class="relative">
              <span class="absolute left-3 top-1/2 -translate-y-1/2 text-white/60">📧</span>
              <input
                v-model="email"
                type="email"
                required
                readonly
                class="w-full pl-10 pr-4 py-3 bg-white/10 backdrop-blur-sm border-2 border-white/20 rounded-xl text-white/80 focus:outline-none cursor-not-allowed"
              />
            </div>
          </div>
          
          <!-- Code OTP -->
          <div>
            <label class="block text-sm font-medium text-white/90 mb-2">Code OTP (6 chiffres)</label>
            <div class="relative">
              <span class="absolute left-3 top-1/2 -translate-y-1/2 text-white/60">🔑</span>
              <input
                v-model="otp"
                type="text"
                maxlength="6"
                required
                placeholder="123456"
                class="w-full pl-10 pr-4 py-3 bg-white/10 backdrop-blur-sm border-2 rounded-xl text-white placeholder-white/50 text-center text-2xl tracking-widest focus:outline-none focus:ring-2 focus:ring-agri-green-light focus:border-transparent transition-all"
                :class="{ 'border-red-400': errors.otp, 'border-white/20': !errors.otp }"
              />
            </div>
            <p v-if="errors.otp" class="text-red-400 text-xs mt-1">{{ errors.otp }}</p>
            <p class="text-xs text-white/60 mt-1">Code valable 15 minutes</p>
          </div>
          
          <!-- Nouveau mot de passe -->
          <div>
            <label class="block text-sm font-medium text-white/90 mb-2">Nouveau mot de passe</label>
            <div class="relative">
              <span class="absolute left-3 top-1/2 -translate-y-1/2 text-white/60">🔒</span>
              <input
                :type="showPassword ? 'text' : 'password'"
                v-model="newPassword"
                required
                minlength="8"
                placeholder="Minimum 8 caractères"
                class="w-full pl-10 pr-12 py-3 bg-white/10 backdrop-blur-sm border-2 rounded-xl text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-agri-green-light focus:border-transparent transition-all"
                :class="{ 'border-red-400': errors.password, 'border-white/20': !errors.password }"
              />
              <button
                type="button"
                @click="showPassword = !showPassword"
                class="absolute right-3 top-1/2 transform -translate-y-1/2 text-white/60 hover:text-white transition-colors"
              >
                {{ showPassword ? '🙈' : '👁️' }}
              </button>
            </div>
            <p v-if="errors.password" class="text-red-400 text-xs mt-1">{{ errors.password }}</p>
          </div>
          
          <!-- Confirmation mot de passe -->
          <div>
            <label class="block text-sm font-medium text-white/90 mb-2">Confirmer le mot de passe</label>
            <div class="relative">
              <span class="absolute left-3 top-1/2 -translate-y-1/2 text-white/60">🔒</span>
              <input
                :type="showConfirmPassword ? 'text' : 'password'"
                v-model="confirmPassword"
                required
                placeholder="Retapez votre mot de passe"
                class="w-full pl-10 pr-12 py-3 bg-white/10 backdrop-blur-sm border-2 rounded-xl text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-agri-green-light focus:border-transparent transition-all"
                :class="{ 'border-red-400': errors.confirmPassword, 'border-white/20': !errors.confirmPassword }"
              />
              <button
                type="button"
                @click="showConfirmPassword = !showConfirmPassword"
                class="absolute right-3 top-1/2 transform -translate-y-1/2 text-white/60 hover:text-white transition-colors"
              >
                {{ showConfirmPassword ? '🙈' : '👁️' }}
              </button>
            </div>
            <p v-if="errors.confirmPassword" class="text-red-400 text-xs mt-1">{{ errors.confirmPassword }}</p>
          </div>
          
          <!-- Force du mot de passe -->
          <div v-if="newPassword" class="p-4 bg-white/10 backdrop-blur-sm border border-white/20 rounded-xl">
            <div class="text-xs text-white/80 mb-2">Force du mot de passe :</div>
            <div class="flex gap-1">
              <div 
                v-for="n in 4" 
                :key="n"
                class="h-1.5 flex-1 rounded-full transition-all duration-300"
                :class="getPasswordStrengthClass(n)"
              ></div>
            </div>
            <div class="text-xs text-white/80 mt-2">
              {{ getPasswordStrengthText() }}
            </div>
          </div>
          
          <button
            type="submit"
            :disabled="loading || !isFormValid"
            class="agri-btn w-full py-3 px-4 text-lg font-semibold disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:transform-none"
          >
            <span v-if="loading" class="flex items-center justify-center gap-2">
              <svg class="animate-spin h-5 w-5" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              <span>Traitement en cours...</span>
            </span>
            <span v-else class="flex items-center justify-center gap-2">
              <span>🔄</span>
              <span>Réinitialiser le mot de passe</span>
            </span>
          </button>
        </form>
        
        <!-- Message de succès -->
        <div v-if="msg" class="mt-6 p-4 bg-agri-green/20 backdrop-blur-sm border border-agri-green/30 rounded-xl animate-fadeIn">
          <div class="flex items-start gap-3">
            <span class="text-2xl text-agri-green-light">✅</span>
            <div>
              <p class="font-medium text-white">{{ msg }}</p>
              <p class="text-sm mt-1 text-white/80">Redirection vers la page de connexion...</p>
            </div>
          </div>
          <!-- Barre de progression -->
          <div class="mt-3 h-1 bg-white/10 rounded-full overflow-hidden">
            <div class="h-full bg-agri-green-light animate-progress"></div>
          </div>
        </div>
        
        <!-- Message d'erreur -->
        <div v-if="error" class="mt-6 p-4 bg-red-500/20 backdrop-blur-sm border border-red-400/30 rounded-xl animate-fadeIn">
          <div class="flex items-start gap-3">
            <span class="text-2xl">❌</span>
            <p class="text-white/90">{{ error }}</p>
          </div>
        </div>
        
        <!-- Lien retour -->
        <div class="mt-8 text-center">
          <router-link 
            to="/login" 
            class="inline-flex items-center gap-2 text-white/80 hover:text-white transition-colors group"
          >
            <svg class="w-5 h-5 transform group-hover:-translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
            </svg>
            <span>Retour à la connexion</span>
          </router-link>
        </div>
      </div>
    </div>

    <!-- Footer avec style verre -->
    <footer class="relative z-10 py-6 px-4 mt-auto">
      <div class="max-w-6xl mx-auto px-4">
        <div class="flex flex-col md:flex-row justify-between items-center">
          <div class="text-white/80 text-sm mb-4 md:mb-0">
            © {{ new Date().getFullYear() }} AgriCycle — Agriculture durable ♻️🌱
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { resetPassword } from '../../api/exports';

const route = useRoute();
const router = useRouter();

// State
const email = ref('');
const otp = ref('');
const newPassword = ref('');
const confirmPassword = ref('');
const showPassword = ref(false);
const showConfirmPassword = ref(false);
const loading = ref(false);
const msg = ref('');
const error = ref('');
const errors = ref({
  otp: '',
  password: '',
  confirmPassword: ''
});

// Computed
const isFormValid = computed(() => {
  return email.value && 
         otp.value.length === 6 && 
         newPassword.value.length >= 8 && 
         newPassword.value === confirmPassword.value;
});

// Lifecycle
onMounted(() => {
  email.value = route.query.email || '';
  if (!email.value) {
    error.value = 'Email manquant. Veuillez refaire une demande de réinitialisation.';
  }
});

// Password strength functions
function getPasswordStrength() {
  const password = newPassword.value;
  if (!password) return 0;
  
  let strength = 0;
  if (password.length >= 8) strength++;
  if (/[A-Z]/.test(password)) strength++;
  if (/[0-9]/.test(password)) strength++;
  if (/[^A-Za-z0-9]/.test(password)) strength++;
  
  return strength;
}

function getPasswordStrengthClass(level) {
  const strength = getPasswordStrength();
  if (strength >= level) {
    if (strength === 4) return 'bg-green-500';
    if (strength === 3) return 'bg-yellow-500';
    if (strength === 2) return 'bg-orange-500';
    return 'bg-red-500';
  }
  return 'bg-white/20';
}

function getPasswordStrengthText() {
  const strength = getPasswordStrength();
  const texts = [
    'Très faible',
    'Faible',
    'Moyen',
    'Fort',
    'Très fort'
  ];
  return texts[strength];
}

// Main reset function
async function handleReset() {
  console.log('🔄 Début de handleReset');
  
  // Reset messages
  msg.value = '';
  error.value = '';
  errors.value = {
    otp: '',
    password: '',
    confirmPassword: ''
  };
  loading.value = true;
  
  // Validation
  let hasErrors = false;
  
  if (!email.value) {
    error.value = 'Email requis';
    hasErrors = true;
  }
  
  if (otp.value.length !== 6) {
    errors.value.otp = 'Le code OTP doit contenir 6 chiffres';
    hasErrors = true;
  }
  
  if (newPassword.value.length < 8) {
    errors.value.password = 'Le mot de passe doit contenir au moins 8 caractères';
    hasErrors = true;
  }
  
  if (newPassword.value !== confirmPassword.value) {
    errors.value.confirmPassword = 'Les mots de passe ne correspondent pas';
    hasErrors = true;
  }
  
  if (hasErrors) {
    loading.value = false;
    return;
  }
  
  try {
    console.log('📤 Appel de resetPassword API avec:', { 
      email: email.value, 
      otp: otp.value 
    });
    
    const response = await resetPassword({
      email: email.value,
      otp: otp.value,
      new_password: newPassword.value
    });
    
    console.log('✅ Réponse API:', response.data);
    
    msg.value = response.data.message || 'Mot de passe réinitialisé avec succès !';
    
    // Redirection après 3 secondes
    setTimeout(() => {
      router.push('/login');
    }, 3000);
    
  } catch (err) {
    console.error('❌ Erreur:', err);
    
    if (err.response) {
      error.value = err.response.data?.detail || 
                   err.response.data?.error || 
                   'Erreur lors de la réinitialisation';
      console.log('📊 Détails erreur:', err.response.data);
      
      // Gestion spécifique des erreurs
      if (err.response.data?.detail?.includes('OTP') || 
          err.response.data?.detail?.includes('code')) {
        errors.value.otp = 'Code OTP incorrect ou expiré';
      }
    } else if (err.request) {
      error.value = 'Serveur injoignable. Vérifiez votre connexion.';
    } else {
      error.value = 'Erreur: ' + err.message;
    }
    
  } finally {
    loading.value = false;
    console.log('🏁 Fin de handleReset');
  }
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

/* Structure flex pour le footer en bas */
.flex-col {
  display: flex;
  flex-direction: column;
}

.flex-1 {
  flex: 1;
}

.min-h-screen {
  min-height: 100vh;
}

/* Couleurs personnalisées */
.text-agri-green-light {
  color: #68d391;
}

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

/* Styles pour les boutons (copiés de la page d'accueil) */
.agri-btn {
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

.agri-btn:hover:not(:disabled) {
  transform: translateY(-3px);
  box-shadow: 0 15px 35px rgba(72, 187, 120, 0.4);
  background: linear-gradient(135deg, #5cc489 0%, #3a9a6b 100%);
}

/* Styles pour les cartes avec effet de verre (copiés de la page d'accueil) */
.agri-card {
  transition: transform 0.4s ease, box-shadow 0.4s ease;
  border: 1px solid rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

.agri-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
  background: rgba(255, 255, 255, 0.15) !important;
}

/* Effet de texte avec ombre pour mieux ressortir */
.text-white {
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.font-bold {
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
}

/* Style du footer */
footer {
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  background: rgba(0, 0, 0, 0.2);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

/* Animation spinner */
@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.animate-spin {
  animation: spin 1s linear infinite;
}

/* Animation fadeIn */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fadeIn {
  animation: fadeIn 0.5s ease-out;
}

/* Animation barre de progression */
@keyframes progress {
  from {
    width: 0%;
  }
  to {
    width: 100%;
  }
}

.animate-progress {
  animation: progress 3s linear forwards;
}

/* Style des inputs */
input {
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  transition: all 0.3s ease;
}

input:focus {
  background: rgba(255, 255, 255, 0.15);
}

input::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

input[readonly] {
  background: rgba(255, 255, 255, 0.05);
  color: rgba(255, 255, 255, 0.8);
  cursor: not-allowed;
}

/* Style des barres de force du mot de passe */
.bg-white\/20 {
  background-color: rgba(255, 255, 255, 0.2);
}

/* Pour les écrans mobiles */
@media (max-width: 768px) {
  .fixed {
    background-attachment: scroll;
  }
  
  .agri-card {
    padding: 1.5rem;
  }
  
  .text-3xl {
    font-size: 1.875rem;
  }
  
  footer {
    text-align: center;
    padding: 1.5rem 1rem;
  }
  
  footer .flex-col {
    gap: 1rem;
  }
}
</style>