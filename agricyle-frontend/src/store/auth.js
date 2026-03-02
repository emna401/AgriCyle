import { defineStore } from "pinia";
import { getMe, refreshToken as apiRefreshToken } from "../api/exports";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    accessToken: localStorage.getItem("accessToken") || "",
    refreshToken: localStorage.getItem("refreshToken") || "",
    user: null,
    loadingMe: false,
  }),

  getters: {
    isLoggedIn: (s) => !!s.accessToken,
    role: (s) => s.user?.role || null,
  },

  actions: {
    setTokens({ access, refresh }) {
      this.accessToken = access || "";
      this.refreshToken = refresh || "";

      if (access) localStorage.setItem("accessToken", access);
      if (refresh) localStorage.setItem("refreshToken", refresh);
    },

    logout() {
      this.accessToken = "";
      this.refreshToken = "";
      this.user = null;

      localStorage.removeItem("accessToken");
      localStorage.removeItem("refreshToken");
    },

    async fetchMe() {
      if (!this.accessToken) return null;
      if (this.loadingMe) return this.user;

      this.loadingMe = true;
      try {
        const res = await getMe();
        this.user = res.data;
        return this.user;
      } catch (err) {
        // si access token expiré => essayer refresh
        const ok = await this.tryRefresh();
        if (!ok) {
          this.logout();
          throw err;
        }
        // re-try getMe après refresh
        const res2 = await getMe();
        this.user = res2.data;
        return this.user;
      } finally {
        this.loadingMe = false;
      }
    },

    async tryRefresh() {
      if (!this.refreshToken) return false;
      try {
        const res = await apiRefreshToken({ refresh: this.refreshToken });
        this.setTokens({ access: res.data.access, refresh: this.refreshToken });
        return true;
      } catch (e) {
        return false;
      }
    },
  },
});
