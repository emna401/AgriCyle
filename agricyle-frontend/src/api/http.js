import axios from "axios";
import { useAuthStore } from "../store/auth";

const API_BASE =
  import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000/api";

const http = axios.create({
  baseURL: API_BASE,
  timeout: 20000,
});

let isRefreshing = false;
let failedQueue = [];

function processQueue(error, token = null) {
  failedQueue.forEach((prom) => {
    if (error) prom.reject(error);
    else prom.resolve(token);
  });
  failedQueue = [];
}

http.interceptors.request.use((config) => {
  const auth = useAuthStore();
  if (auth.accessToken) {
    config.headers.Authorization = `Bearer ${auth.accessToken}`;
  }
  return config;
});

http.interceptors.response.use(
  (res) => res,
  async (err) => {
    const auth = useAuthStore();
    const originalRequest = err.config;

    if (err?.response?.status !== 401) return Promise.reject(err);

    if (originalRequest._retry) {
      auth.logout();
      return Promise.reject(err);
    }

    if (!auth.refreshToken) {
      auth.logout();
      return Promise.reject(err);
    }

    if (isRefreshing) {
      return new Promise((resolve, reject) => {
        failedQueue.push({
          resolve: (token) => {
            originalRequest.headers.Authorization = `Bearer ${token}`;
            resolve(http(originalRequest));
          },
          reject,
        });
      });
    }

    originalRequest._retry = true;
    isRefreshing = true;

    try {
      const refreshRes = await axios.post(`${API_BASE}/token/refresh/`, {
        refresh: auth.refreshToken,
      });

      const newAccess = refreshRes.data.access;
      auth.setTokens({ access: newAccess, refresh: auth.refreshToken });

      processQueue(null, newAccess);

      originalRequest.headers.Authorization = `Bearer ${newAccess}`;
      return http(originalRequest);
    } catch (refreshErr) {
      processQueue(refreshErr, null);
      auth.logout();
      return Promise.reject(refreshErr);
    } finally {
      isRefreshing = false;
    }
  }
);

export default http;
