import { Routes } from '@angular/router';

export const routes: Routes = [
  { path: '', loadComponent: () => import('./features/home/home').then(m => m.Home) },
  
  { path: 'auth/login', loadComponent: () => import('./features/auth/login/login').then(m => m.Login) },
  { path: 'auth/register', loadComponent: () => import('./features/auth/register/register').then(m => m.Register) },
  { path: 'auth/forgot', loadComponent: () => import('./features/auth/forget-passowrd/forget-passowrd').then(m => m.ForgetPassowrd) },

  { path: 'products', loadComponent: () => import('./features/products/product-detail/product-detail').then(m => m.ProductDetail) },
  { path: 'product/:id', loadComponent: () => import('./features/products/product-detail/product-detail').then(m => m.ProductDetail) },

  { path: 'cart', loadComponent: () => import("./features/cart/cart").then(m=>m.Cart) },

  { path: 'orders', loadComponent: () => import('./features/orders/order-detail/order-detail').then(m => m.OrderDetail) },
  { path: 'order/:id', loadComponent: () => import('./features/orders/order-detail/order-detail').then(m => m.OrderDetail) },

  { path: 'profile', loadComponent: () => import('./features/user-profile/user-profile').then(m => m.UserProfile) },

  { path: 'chatbot', loadComponent: () => import('./features/ai-chatbot/ai-chatbot').then(m => m.AiChatbot) },

  { path: '404', loadComponent: () => import('./shared/not-found/not-found').then(m => m.NotFound) },
  { path: 'access-denied', loadComponent: () => import('./shared/access-denied/access-denied').then(m => m.AccessDenied) },

  { path: '**', redirectTo: '404' }
];
