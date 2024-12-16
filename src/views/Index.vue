<template>
  <el-menu
    :default-active="activeIndex"
    class="el-menu--horizontal"
    mode="horizontal"
    :ellipsis="false"
    @select="handleSelect"
  >
  
    <el-menu-item index="0" class="menu_item_logo">
      <img
        style="width: 100px"
        src="../assets/sims.png"
        alt="Hospital Sterilization IMS logo"
      />
    </el-menu-item>
    <div class="menu_item_search">
      <el-input
        v-model="input1" 
        style="width: 180px; margin-top: 14px;"
        placeholder="Search..."
        :suffix-icon="Search"
      />
    </div>
    <el-sub-menu index="2" class="menu_item_link">
      <template #title>Workspace</template>
      <el-menu-item index="2-1">item one</el-menu-item>
      <el-menu-item index="2-2">item two</el-menu-item>
      <el-menu-item index="2-3">item three</el-menu-item>
    </el-sub-menu>
    <div class="menu_item_custom">
      <span @click="isCollapse = !isCollapse">
      <el-icon  :size="30"><icon-menu /></el-icon>
    </span>
    </div>
  </el-menu>

  <!-- Side menu -->
  <div class="side_nav">
    <div class="side_menu">
      <el-menu
        default-active="1"
        class="el-menu-vertical-demo"
        :collapse="isCollapse"
        @open="handleOpen"
        @close="handleClose"
      >
        <el-sub-menu index="1">
          <template #title>
            <el-icon><PieChart /></el-icon>
            <span>Facility</span>
          </template>
          <el-menu-item-group>
            <template #title><span>Group One</span></template>
            <el-menu-item index="departments">setting</el-menu-item>
            <el-menu-item index="1-2">departments</el-menu-item>
            <el-menu-item index="1-3">Employee</el-menu-item>
          </el-menu-item-group>
          <el-menu-item-group title="Group Two">
            <el-menu-item index="1-4">item three</el-menu-item>
          </el-menu-item-group>
          <el-sub-menu index="1-5">
            <template #title><span>item four</span></template>
            <el-menu-item index="1-5-1">item one</el-menu-item>
          </el-sub-menu>
        </el-sub-menu>
        <el-menu-item index="2" disabled>
          <el-icon><document /></el-icon>
          <template #title>Navigator Three</template>
        </el-menu-item>
        <el-menu-item index="3" @click="logout">
          <el-icon><setting /></el-icon>
          <template #title>Logout</template>
        </el-menu-item>
      </el-menu>
    </div>
    <div class="container">
      <router-view name="index"></router-view>
    </div>
  </div>

</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router';
//import { useStore } from 'vuex'; 

const router = useRouter();
//const store = useStore()

import {
  Document,
  Menu as IconMenu,
  PieChart,
  Setting,
  Search,
} from '@element-plus/icons-vue'

const isCollapse = ref(true)
const handleOpen = (key, keyPath) => {
  console.log(key, keyPath)
}
const handleClose = (key, keyPath) => {
  console.log(key, keyPath)
}

const activeIndex = ref('1')
const handleSelect = (key, keyPath) => {
  console.log(key, keyPath)
}

const logout = () => {
  localStorage.removeItem('authToken');
  router.push({ name: 'SignIn' })
}
</script>


<style scoped>
.el-menu--horizontal {
  position: fixed; width: 100%;
  z-index: 1000;
}

.el-menu--horizontal .menu_item_custom {
  padding: 16px 10px 0 10px; 
  cursor: pointer;
}
.el-menu--horizontal .menu_item_custom:hover {
  color: var(--el-menu-active-color);
  transition: 0.3s;
}

.el-menu--horizontal > .el-menu-item:nth-child(1) {
  margin-right: auto;
}

.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}

.side_nav {
  display: flex;
  margin-top: 60px;
  position: absolute;
}

.side_nav .side_menu {
  position: fixed;
  z-index: 1000;
} 

.side_nav .container {
  margin-left: 70px;
  position: relative;
} 

@media (max-width: 477px) {

  .el-menu--horizontal>.menu_item_link,
  .el-menu--horizontal>.menu_item_search {
    display: none;
  }
}

</style>

