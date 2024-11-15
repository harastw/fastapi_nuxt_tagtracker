<template>
  <div>
    <h2>Files</h2>
    <div v-for="item in files">
      <a @click.prevent="downloadFile(item)">{{ item }}</a>
    </div>
  </div>
</template>  

<script lang="ts" setup>
import { ref } from "vue";
import axios from "axios";

const URL = "http://localhost:8000/get_files/";

const files = ref([]);

const fetchFiles = async () => {
    try {
        const response = await axios.get(URL, {
            params: { offset: 0, limit: 10 }
        });

        files.value = response.data;
    } catch (error) {
        console.error(error);
    }
};
fetchFiles();

const downloadFile = (filePath: any) => {
    const downloadUrl = `http://localhost:8000/download?file_path=assets/${filePath}`;
    window.open(downloadUrl, '_blank');
};

const filesLinks = ref([]);

</script>

<style scoped>

h2 {
  color: #42b983;
}

</style>
