<template>
    <div class="not_found_container">
      <div class="content">
        <div class="not_found">
          <h1>404</h1>
          <p>Oops! The page you're looking for cannot be found.</p>
          <router-link to="/">
            <el-button>Return to Home</el-button>
          </router-link>
        </div>
      </div>
    </div>
</template>

<style scoped>
.not_found_container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  background: linear-gradient(135deg, #74ebd5 0%, #ACB6E5 100%);

}

.content {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center; 
}

.not_found {
  max-width: 400px;
  border-radius: 5px;
  background-color: white;
  box-shadow: 1px 1px 10px 10px rgba(186,191,203,0.08);
  padding: 20px;

}

</style>
  