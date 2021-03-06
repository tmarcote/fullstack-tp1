
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: 'cart', component: () => import('pages/Cart.vue') },
      { path: 'success', component: () => import('pages/Success.vue') }
    ]
  },
  {
    path: '/login',
    component: () => import('layouts/LoginLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Login.vue') }
    ]
  },
  {
    path: '/admin',
    component: () => import('layouts/AdminLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Admin.vue') },
      { path: 'usuarios', component: () => import('pages/Usuarios.vue') },
      { path: 'productos', component: () => import('pages/Productos.vue') },
      { path: 'reportes/ventas', component: () => import('pages/ReporteVentas.vue') }
    ]
  },
  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
