<template>
  <div>
    <header class="nav-header">
      <router-link to="/data">1D Solver</router-link>
      <router-link to="/images">2D Image Tools</router-link>
    </header>
    <router-view />
  </div>
</template>

<style>
.nav-header {
  padding: 2rem 1.5rem;
  display: flex;
  gap: 1rem;
  padding: 1rem;
  background: #333;
  color: white;
  justify-content: center;
}

.nav-header a {
  padding: 1.5rem;
  font-size: 1.6rem;
  color: white;
  text-decoration: none;
  font-weight: bold;
}

.nav-header a.router-link-exact-active {
  text-decoration: underline;
}
</style>
