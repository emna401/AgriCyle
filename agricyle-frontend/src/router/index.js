import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "../store/auth";
import ResetPassword from "../pages/public/ResetPassword.vue";
// Layouts
import PublicLayout from "../layouts/PublicLayout.vue";
import AppLayout from "../layouts/AppLayout.vue";

// Public Pages
import HomePage from "../pages/public/HomePage.vue";
import LanguageSelection from "../pages/public/LanguageSelection.vue";
import Login from "../pages/public/Login.vue";
import Register from "../pages/public/Register.vue";
import ForgotPassword from "../pages/public/ForgotPassword.vue";
import GoodPractices from "../pages/public/GoodPractices.vue";


// Farmer
import FarmerDashboard from "../pages/farmer/FarmerDashboard.vue";
import MyDeclarations from "../pages/farmer/MyDeclarations.vue";
import UserProfile from "../pages/farmer/UserProfile.vue";

// Beneficiary
import BeneficiaryDashboard from "../pages/beneficiary/BeneficiaryDashboard.vue";
import ProductCatalog from "../pages/beneficiary/ProductCatalog.vue";
import CartPage from "../pages/beneficiary/CartPage.vue";
import OrdersPage from "../pages/beneficiary/OrdersPage.vue";

// Dual
import DualDashboard from "../pages/dual/DualDashboard.vue";
// Admin
import AdminDashboard from "../pages/admin/AdminDashboard.vue";
import DeclarationsManagement from "../pages/admin/DeclarationsManagement.vue";
import ProductsManagement from "../pages/admin/ProductsManagement.vue";
import OrdersManagement from "../pages/admin/OrdersManagement.vue";
import GoodPracticesManagement from "../pages/admin/GoodPracticesManagement.vue";
import UserManagement from '../pages/admin/UserManagement.vue';
const routes = [
  {
    path: "/",
    component: PublicLayout,
    children: [
      { path: "", name: "home", component: HomePage },
      { path: "lang", name: "lang", component: LanguageSelection },
      { path: "login", name: "login", component: Login },
      { path: "register", name: "register", component: Register },
      { path: "forgot-password", name: "forgotPassword", component: ForgotPassword },
      { path: "good-practices", name: "goodPractices", component: GoodPractices },
      { path: "reset-password", name: "ResetPassword", component: ResetPassword,},
      
    ]
  },
  
  { path: "/app", component: AppLayout, meta: { requiresAuth: true },
    children: [
      // Farmer
      { path: "farmer", name: "farmerDashboard", component: FarmerDashboard, meta: { role: ["FARMER"] } },
      { path: "farmer/declarations", name: "farmerDeclarations", component: MyDeclarations, meta: { role: ["FARMER"] } },
      { path: "farmer/profile", name: "FarmerProfile",component: UserProfile, meta: { role: ["FARMER"] }
},
      // Beneficiary
      { path: "beneficiary", name: "beneficiaryDashboard", component: BeneficiaryDashboard, meta: { role: ["BENEFICIARY"] } },
      { path: "catalog", name: "catalog", component: ProductCatalog, meta: { role: ["BENEFICIARY", "DUAL"] } },
      { path: "cart", name: "cart", component: CartPage, meta: { role: ["BENEFICIARY", "DUAL"] } },
      { path: "orders", name: "orders", component: OrdersPage, meta: { role: ["BENEFICIARY", "DUAL"] } },
      
      // Dual
      { path: "dual", name: "dualDashboard", component: DualDashboard, meta: { role: ["DUAL"] } },
      { path: "dual/declarations", name: "dualDeclarations", component: MyDeclarations, meta: { role: ["DUAL"] } },



      // Profile (all non-admin users)
      { path: "profile", name: "profile", component: UserProfile, meta: { role: ["FARMER", "BENEFICIARY", "DUAL"] } },

      // Admin
      { path: "admin", name: "adminDashboard", component: AdminDashboard, meta: { role: ["ADMIN", "SUPERADMIN"] } },
      { path: "admin/declarations", name: "adminDeclarations", component: DeclarationsManagement, meta: { role: ["ADMIN", "SUPERADMIN"] } },
      { path: "admin/products", name: "adminProducts", component: ProductsManagement, meta: { role: ["ADMIN", "SUPERADMIN"] } },
      { path: "admin/orders", name: "adminOrders", component: OrdersManagement, meta: { role: ["ADMIN", "SUPERADMIN"] } },
      { path: "admin/good-practices", name: "adminGoodPractices", component: GoodPracticesManagement, meta: { role: ["ADMIN", "SUPERADMIN"] } },
      { path: "admin/users", name: "UserManagement", component: UserManagement, meta: { role: ["ADMIN", "SUPERADMIN"] } },
    ]
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach(async (to) => {
  const auth = useAuthStore();

  // 1) route protégée
  if (to.meta.requiresAuth && !auth.isLoggedIn) {
    return { name: "login" };
  }

  // 2) si logged mais user pas chargé -> fetchMe
  if (auth.isLoggedIn && !auth.user) {
    try {
      await auth.fetchMe();
    } catch (e) {
      auth.logout();
      return { name: "login" };
    }
  }

  // 3) contrôle rôle
  const roles = to.meta.role;
  if (roles && auth.user && !roles.includes(auth.user.role)) {
    return { name: "home" };
  }

  return true;
});

export default router;
