<template>
  <div class="auth-page">
    <RouterLink to="/" class="back-link">← На главную</RouterLink>
    <div class="container">
      <h1 class="loading-text" v-if="!userName">Обработка авторизации...</h1>
      <div v-if="message" class="message">
        {{ message }}
      </div>
      <div v-if="userName" class="welcome">
        Добро пожаловать, <strong>{{ userName }}</strong>!
      </div>
      <img v-if="picUrl" :src="picUrl" class="avatar" />

      <div v-if="fileNames.length" class="files">
        <h2>Ваши файлы в Google Drive:</h2>
        <ul>
          <li v-for="file in fileNames" :key="file">{{ file }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: '',
      userName: '',
      picUrl: '',
      fileNames: [],
    };
  },
  mounted() {
    const queryParams = new URLSearchParams(window.location.search);
    const code = queryParams.get('code')
    const state = queryParams.get('state')

    if (code && state) {
      fetch('http://localhost:8000/auth/google/callback', {
        body: JSON.stringify({ code, state }),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
      })
        .then(res => {
          if (!res.ok) {
            throw new Error('Ошибка сервера')
          }
          return res.json()
        })
        .then(data => {
          this.picUrl = data.user.picture
          this.userName = data.user.name
          this.fileNames = data.files
        })
    } else {
      this.message = '⚠️ Нет параметра code';
    }
  },
};
</script>

<style scoped>
.auth-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: linear-gradient(135deg, #f0f4ff, #e0f7fa);
  font-family: 'Inter', sans-serif;
}

.back-link {
  margin: 20px;
  text-decoration: none;
  color: #3f51b5;
  font-size: 16px;
  font-weight: 500;
  transition: color 0.3s;
}

.back-link:hover {
  color: #1a237e;
}

.container {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 20px;
}

.loading-text {
  color: #333;
  font-size: 28px;
  font-weight: 600;
  margin-bottom: 25px;
  animation: fade 1.5s infinite;
}

@keyframes fade {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.6; }
}

.message {
  font-size: 18px;
  color: #616161;
  background-color: #ffffff;
  padding: 12px 20px;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  margin-bottom: 20px;
}

.welcome {
  background-color: #e8f5e9;
  color: #2e7d32;
  border-radius: 12px;
  padding: 15px 30px;
  font-size: 20px;
  font-weight: 500;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  margin-bottom: 20px;
}

.avatar {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  box-shadow: 0 4px 8px rgba(0,0,0,0.2);
  margin-top: 15px;
}

.files {
  margin-top: 30px;
  background-color: #ffffff;
  border-radius: 10px;
  padding: 15px 25px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  text-align: left;
  width: 100%;
  max-width: 500px;
}

.files h2 {
  font-size: 22px;
  margin-bottom: 10px;
  color: #3f51b5;
}

.files ul {
  list-style-type: disc;
  padding-left: 20px;
}

.files li {
  font-size: 16px;
  color: #333;
  margin-bottom: 5px;
}
</style>
