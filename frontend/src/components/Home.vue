<template>
  <div class="container">
    <h1>Добро пожаловать</h1>
    <button class="google-btn" @click="loginWithGoogle">
      <img src="../assets/google.webp" width="32"/>
      Войти через Google
    </button>
  </div>
</template>

<script>
export default {
  methods: {
    loginWithGoogle() {
      window.location.href = 'http://127.0.0.1:8000/auth/google/url';
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: #f5f5f5;
  text-align: center;
}

h1 {
  margin-bottom: 20px;
  font-family: sans-serif;
  color: #333;
}

.google-btn {
  display: flex;
  align-items: center;
  gap: 10px;
  background-color: #ffffff;
  color: #555;
  border: 1px solid #ddd;
  border-radius: 50px;
  padding: 12px 20px;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: all 0.3s ease;
}

.google-btn:hover {
  box-shadow: 0 4px 10px rgba(0,0,0,0.2);
  transform: translateY(-2px);
}

.google-icon {
  width: 20px;
  height: 20px;
}
</style>
