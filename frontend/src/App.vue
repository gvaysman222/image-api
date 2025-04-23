<template>
  <div style="max-width:600px;margin:40px auto;">
    <h2>Загрузка</h2>
    <form @submit.prevent="uploadImage" style="margin-bottom:24px;">
      <input type="file" @change="onFileChange" required />
      <input v-model="description" placeholder="Описание" required style="margin: 0 8px;" />
      <button type="submit">Отправить</button>
    </form>

    <h2>Галерея</h2>
    <div style="display:flex; flex-wrap:wrap; gap:20px;">
      <div
        v-for="item in images"
        :key="item.id"
        style="display:flex; flex-direction:column; align-items:center; width:220px;"
      >
        <div
          style="
            width:200px;
            height:200px;
            overflow:hidden;
            background:#f0f0f0;
            display:flex;
            align-items:center;
            justify-content:center;
          "
        >
          <img
            :src="item.image"
            alt="preview"
            style="width:100%; height:100%; object-fit:cover;"
          />
        </div>
        <p style="margin:8px 0; text-align:center;">{{ item.description }}</p>
        <button @click="deleteImage(item.id)">Удалить</button>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const images = ref([])
const file = ref(null)
const description = ref('')

const onFileChange = e => {
  file.value = e.target.files[0]
}

const getImages = async () => {
  const res = await axios.get('/api/images/')
  // res.data[i].image уже = "data:image/...;base64,XXX"
  images.value = res.data
}

const uploadImage = async () => {
  if (!file.value) return
  const reader = new FileReader()
  reader.onload = async () => {
    await axios.post('/api/images/', {
      image: reader.result,
      description: description.value
    })
    description.value = ''
    file.value = null
    getImages()
  }
  reader.readAsDataURL(file.value)
}

const deleteImage = async id => {
  await axios.delete(`/api/images/${id}/`)
  getImages()
}

onMounted(getImages)
</script>
