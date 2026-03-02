<script setup>
import { onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useAuthStore } from './store/auth'

const auth = useAuthStore()
const route = useRoute()

onMounted(() => {
  if (import.meta.env.VITE_DEMO_MODE === 'true' && !auth.user) {
    // Permet de choisir le rôle via l'URL: ?role=FARMER
    const urlRole = route.query.role
    const roles = ['FARMER', 'BENEFICIARY', 'DUAL']
    const role = roles.includes(urlRole) ? urlRole : 'DUAL'
    
    console.log(`🔧 Mode démo activé avec rôle: ${role}`)
    auth.demoLogin(role)
  }
})
</script>