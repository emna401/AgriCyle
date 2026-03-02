import http from "./http";


/* AUTH */
export const login = (payload) => http.post("/auth/token/", payload);
export const register = (payload) => http.post("/auth/register/", payload);

export const getMe = () => http.get("/me/me/");
export const updateMe = (payload) => http.patch("/me/update_profile/", payload);

export const refreshToken = (payload) => http.post("/token/refresh/", payload);

/* Forgot Password */
export const sendResetOtp = (payload) => http.post("/auth/reset/request/", payload);
export const resetPassword = (payload) => http.post("/auth/reset/confirm/", payload);

/* =========================
   GOOD PRACTICES (PUBLIC + ADMIN CRUD)
========================= */
export const getGoodPracticesPublic = () => http.get("/good-practices/");
export const listGoodPractices = () => http.get("/good-practices/");

export const adminCreateGoodPractice = (formData) =>
  http.post("/good-practices/", formData, {
    headers: { "Content-Type": "multipart/form-data" }
  });

export const adminUpdateGoodPractice = (id, formData) =>
  http.patch(`/good-practices/${id}/`, formData, {
    headers: { "Content-Type": "multipart/form-data" }
  });

export const adminDeleteGoodPractice = (id) =>
  http.delete(`/good-practices/${id}/`);


/* =========================
   FARMER - DECLARATIONS
========================= */
export const myDeclarations = () => http.get("/declarations/");
export const createDeclaration = (payload) => http.post("/declarations/", payload);

export const adminValidateDeclaration = (id) =>
  http.post(`/declarations/${id}/validate_declaration/`);

export const adminMarkDeclarationCollected = (id) =>
  http.post(`/declarations/${id}/mark_collected/`);

export const getMyDeclarations = () => http.get("/declarations/");

/* =========================
   PRODUCTS (PUBLIC + ADMIN CRUD)
========================= */
export const listProducts = () => http.get("/products/");
export const getProducts = () => http.get("/products/");

export const adminCreateProduct = (payload) => http.post("/products/", payload);
export const adminUpdateProduct = (id, payload) => http.patch(`/products/${id}/`, payload);
export const adminDeleteProduct = (id) => http.delete(`/products/${id}/`);

/* =========================
   ADMIN USER MANAGEMENT
========================= */
export const getUsers = () => http.get("/admin/users/");
export const updateUser = (id, data) => http.put(`/admin/users/${id}/`, data);
export const deleteUser = (id) => http.delete(`/admin/users/${id}/delete/`);
export const suspendUser = (id) => http.post(`/admin/users/${id}/suspend/`);
export const activateUser = (id) => http.post(`/admin/users/${id}/activate/`);
export const resetUserPassword = (id, data) => http.post(`/admin/users/${id}/reset-password/`, data);
export const exportUsersCSV = () => http.get("/admin/users/export-csv/", {
  responseType: 'blob'});
export const exportUsersExcel = (filters = {}) => {
  const params = new URLSearchParams();
  if (filters.role) params.append('role', filters.role);
  if (filters.status) params.append('status', filters.status);
  if (filters.governorate) params.append('governorate', filters.governorate);
  if (filters.delegation) params.append('delegation', filters.delegation);
  
  return http.get(`/admin/users/export-excel/?${params.toString()}`, {
    responseType: 'blob'
  });
};

/* =========================
   CART + ORDERS (match ton backend + tes pages)
========================= */
// backend: @action(detail=False) my_cart => GET /api/orders/my_cart/
export const getMyCart = () => http.get("/orders/my_cart/");


export const addToCart = (orderId, payload) =>
  http.post(`/orders/${orderId}/add_item/`, payload);


export const updateCartItem = (orderId, itemId, payload) =>
  http.patch(`/orders/${orderId}/items/${itemId}/`, payload);


export const removeCartItem = (orderId, itemId) =>
  http.delete(`/orders/${orderId}/items/${itemId}/`);


export const checkoutOrder = (orderId) =>
  http.post(`/orders/${orderId}/checkout/`);

// mes commandes: GET /api/orders/ (filtré buyer)
export const myOrders = () => http.get("/orders/");
export const getMyOrders = () => myOrders();
// admin set status: POST /api/orders/{id}/set_status/
export const adminSetOrderStatus = (id, payload) =>
  http.post(`/orders/${id}/set_status/`, payload);
// admin list all (même endpoint, backend filtre si admin)
export const adminOrders = () => http.get("/orders/");


/* =========================
   ALIASES POUR TES PAGES ACTUELLES (CartPage.vue)
   (tu peux garder ton code Vue sans le réécrire)
========================= */
// Ton CartPage.vue appelle confirmCart() => on map sur checkoutOrder(orderId)
export const confirmCart = (orderId) => checkoutOrder(orderId);

// Ton CartPage.vue appelle removeFromCart() mais ton backend n'a pas remove qty-1,
// il a remove item par itemId. Donc ton UI doit utiliser removeCartItem(orderId, itemId).
//Je mets un alias "removeFromCart" qui supprime l'item COMPLET si tu passes itemId.
export const removeFromCart = (orderId, itemId) => removeCartItem(orderId, itemId);


/* =========================
   STATS
========================= */
export const statsFarmer = () => http.get("/stats/farmer/");
export const statsBeneficiary = () => http.get("/stats/beneficiary/");
export const statsAdmin = () => http.get("/stats/admin/");


/* =========================
   EXPORTS (Admin)
========================= */
export const exportOrdersExcel = (params = {}) =>
  http.get("/exports/orders_report.xlsx", { params, responseType: "blob" });

export const exportOrdersPdf = (params = {}) =>
  http.get("/exports/orders_report.pdf", { params, responseType: "blob" });

// ===== ALIAS ADMIN EXPORTS =====
export const adminExportOrdersPdf = (params = {}) => exportOrdersPdf(params);
export const adminExportOrdersExcel = (params = {}) => exportOrdersExcel(params);
export const adminExportOrdersXlsx = (params = {}) => exportOrdersExcel(params);

// 1) stats admin
export const adminStats = () => http.get("/stats/admin/");

// 2) farms map (ton backend renvoie farmers_points dans stats_admin)
export const adminGetFarmersMap = async () => {
  const res = await http.get("/stats/admin/");
  return { data: res.data?.farmers_points || [] };
};

// 3) exports stats (⚠️ ton backend n'a PAS exports stats dédiés)
// => on les map sur les exports commandes (le report contient déjà Summary, Top, Trend…)
export const adminExportStatsXlsx = (params = {}) => exportOrdersExcel(params);
export const adminExportStatsPdf = (params = {}) => exportOrdersPdf(params);

export const adminListDeclarations = () => http.get("/declarations/");
// status attendu: "VALIDATED" | "COLLECTED"
export const adminUpdateDeclarationStatus = (id, status) => {
  if (status === "VALIDATED") {
    return http.post(`/declarations/${id}/validate_declaration/`);
  }
  if (status === "COLLECTED") {
    return http.post(`/declarations/${id}/mark_collected/`);
  }
  // si tu veux gérer PENDING/DRAFT côté admin, il faut ajouter un endpoint backend (patch)
  return Promise.reject(new Error("Status non supporté par le backend"));
};

/* =========================
   ADMIN - PRODUCTS
========================= */
export const adminListProducts = () => http.get("/products/");
export const adminListOrders = () => http.get("/orders/");

export const adminListGoodPractices = () => http.get("/good-practices/");