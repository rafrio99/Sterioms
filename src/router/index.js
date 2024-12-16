import { createRouter, createWebHistory } from 'vue-router';
import SignUp from '../views/signUp.vue';
import SignIn from '../views/signIn.vue';
import Index from '../views/Index.vue';
import NotFound from '../views/NotFound.vue';
import Facility from '../components/Facility.vue';
import Department from '../components/Department.vue';
import Employee from '../components/Employee.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/sign-up', name: 'SignUp', component: SignUp,  meta: { guest: true } },
    { path: '/sign-in', name: 'SignIn', component: SignIn,  meta: { guest: true } },
    {
      path: '/',
      name: 'Index',
      component: Index,
      meta: { requiresAuth: true },  // This route is protected for logged-in users only
      redirect: '/facility',
      children: [
        { path: 'facility', name: 'facility', components: {index: Facility} },
        { path: 'departments', name: 'departments', components: {index: Department} },
        { path: 'employee', name: 'employee', components: {index: Employee} },

      ]
    },

    { path: '/:pathMatch(.*)*', name: 'not-found', component: NotFound },

  ],
  scrollBehavior(to, from, savedPosition) {
    return { top: 0 };
  },
});


// Navigation guard to check for auth
router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('authToken'); // Vuex store to save user authToken
  if (to.meta.requiresAuth && !isAuthenticated) {
    next({ name: 'SignIn' }); // Redirect to login if not authenticated
  } else {
    next();
  }
});

export default router;
