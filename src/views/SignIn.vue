<template>
  <div class="form_container">
    <div class="form_content">
      <div class="auth_form">
        <h3 style="text-align: center; margin-bottom: 20px;">Log In</h3>
        <el-alert v-if="loginResponse.status" :title="loginResponse.msg" :type="loginResponse.type" 
          :closable="false" show-icon style="background-color: transparent;" />
        <el-form
          ref="ruleFormRef"
          style="max-width: 400px; min-width: 300px;"
          :model="ruleForm"
          status-icon
          :rules="rules"
          label-width="auto"
          label-position="top"
          class="demo-ruleForm"
        >
          <el-form-item label="ID number" prop="id_number">
            <el-input v-model="ruleForm.id_number" type="text"/>
          </el-form-item>
          <el-form-item>If you are not member of a facility
              <RouterLink to="/sign-up">
                  <span style="color:cornflowerblue">, create facility!</span>
              </RouterLink>
          </el-form-item>
          <el-form-item>
            <div style="display: flex; justify-content: center; width: 100%;">
              <el-button type="primary" @click="submitForm(ruleFormRef)">
                Login
              </el-button>
            </div>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
  
</template>
  
<script lang="ts" setup>
import { reactive, ref } from 'vue'
import type { FormInstance, FormRules } from 'element-plus'
import { useRouter } from 'vue-router';
//import { useStore } from 'vuex'; 

const router = useRouter();
//const store = useStore()

const ruleFormRef = ref<FormInstance>()
const ruleForm = reactive({
  id_number: ''
})

const rules = reactive<FormRules<typeof ruleForm>>({
  id_number: [{ required: true, message: 'Please enter your id number', trigger: 'blur' }],
})

const loginResponse = reactive({status: false, type: 'success', msg: ""});

const login = async () => {
  // await store.dispatch('auth/loginUser', ruleForm)
  // .then((data) => {
  //   if (data.status==="success") {
  //     loginResponse.status = true;
  //     loginResponse.type = 'success';
  //     loginResponse.msg = data.message;
  //     router.push({ name: 'home' })
  //   } else {
  //     loginResponse.status = true;
  //     loginResponse.type = 'error';
  //     loginResponse.msg = data.message;
  //   }
  // }) 
  localStorage.setItem('authToken', 'defrgthyjukgi');
  router.push({ name: 'Index' })
};

const submitForm =  (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.validate((valid) => {
    if (valid) {
      login()
    } else {
      console.log('error submit!')
    }
  })
};

</script>


