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
          
          <h2 class="text-3xl font-bold text-white mb-2">Mot de passe oublié</h2>
          <p class="text-white/80">Entrez votre email pour recevoir un code OTP</p>
        </div>
        
        <!-- Formulaire -->
        <form @submit.prevent="sendOtp" class="space-y-5">
          <div>
            <label class="block text-sm font-medium text-white/90 mb-2">Email</label>
            <div class="relative">
              <span class="absolute left-3 top-1/2 -translate-y-1/2 text-white/60">📧</span>
              <input
                v-model="email"
                type="email"
                required
                placeholder="votre@email.com"
                class="w-full pl-10 pr-4 py-3 bg-white/10 backdrop-blur-sm border-2 rounded-xl text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-agri-green-light focus:border-transparent transition-all"
                :class="{ 'border-red-400': error, 'border-white/20': !error }"
              />
            </div>
          </div>
          
          <button
            type="submit"
            :disabled="loading"
            class="agri-btn w-full py-3 px-4 text-lg font-semibold disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:transform-none"
          >
            <span v-if="loading" class="flex items-center justify-center gap-2">
              <svg class="animate-spin h-5 w-5" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              <span>Envoi en cours...</span>
            </span>
            <span v-else class="flex items-center justify-center gap-2">
              <span>📨</span>
              <span>Recevoir le code OTP</span>
            </span>
          </button>
        </form>
        
        <!-- Message de succès -->
        <div v-if="msg" class="mt-6 p-4 bg-agri-green/20 backdrop-blur-sm border border-agri-green/30 rounded-xl">
          <div class="flex items-start gap-3">
            <span class="text-2xl text-agri-green-light">✅</span>
            <div>
              <p class="font-medium text-white">{{ msg }}</p>
              <p class="text-sm mt-1 text-white/80">
                Si cet email existe, un code OTP de 6 chiffres a été envoyé.
                Vérifiez votre boîte de réception (et vos spams).
              </p>
            </div>
          </div>
          
          <!-- Lien pour aller à la page de réinitialisation -->
          <div v-if="email" class="mt-4 pt-4 border-t border-white/20">
            <router-link 
              :to="{ path: '/reset-password', query: { email: email } }"
              class="agri-btn-light inline-flex items-center justify-center gap-2 w-full py-3 px-4 text-base font-medium"
            >
              <span>📝</span>
              <span>J'ai reçu le code OTP</span>
            </router-link>
          </div>
        </div>
        
        <!-- Message d'erreur -->
        <div v-if="error" class="mt-6 p-4 bg-red-500/20 backdrop-blur-sm border border-red-400/30 rounded-xl">
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
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { sendResetOtp } from '../../api/exports';

const router = useRouter();
const email = ref('');
const loading = ref(false);
const msg = ref('');
const error = ref('');

const sendOtp = async () => {
  console.log('🔄 Début de sendOtp');
  
  // Reset
  msg.value = '';
  error.value = '';
  loading.value = true;
  
  // Validation
  if (!email.value.includes('@')) {
    error.value = 'Email invalide';
    loading.value = false;
    return;
  }
  
  try {
    console.log('📤 Appel de sendResetOtp avec:', email.value);
    
    const response = await sendResetOtp({
      email: email.value
    });
    
    console.log('✅ Réponse:', response.data);
    
    // Votre backend retourne toujours le même message pour la sécurité
    msg.value = response.data.message || 'Si cet email existe, un code OTP sera envoyé';
    
  } catch (err) {
    console.error('❌ Erreur:', err);
    
    if (err.response) {
      error.value = err.response.data?.detail || 'Erreur lors de l\'envoi';
      console.log('📊 Détails erreur:', err.response.data);
    } else if (err.request) {
      error.value = 'Serveur injoignable. Vérifiez que Django tourne.';
    } else {
      error.value = 'Erreur: ' + err.message;
    }
    
  } finally {
    loading.value = false;
    console.log('🏁 Fin de sendOtp');
  }
};
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

.agri-btn-light {
  border: 2px solid white;
  color: white;
  border-radius: 12px;
  transition: all 0.3s ease;
  background: transparent;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 8px 20px rgba(255, 255, 255, 0.1);
}

.agri-btn-light:hover {
  background: white;
  color: #2f855a;
  transform: translateY(-3px);
  box-shadow: 0 15px 35px rgba(255, 255, 255, 0.2);
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