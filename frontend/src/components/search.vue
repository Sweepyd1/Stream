<script lang="ts" setup>
import search_card from './search_card.vue';

</script>

<template>
    <div class="container">
        <search_card></search_card>
        <search_card></search_card>
        <search_card></search_card>
        <search_card></search_card>
        <search_card></search_card>
        <search_card></search_card>
        
      
    </div>
</template>

<style scoped lang="scss">
.container {
    width: 500px;
    // min-height: 30vh;
    // max-height: 70vh;
    height: auto;
    background-color: rgba(16, 14, 23, 0.95);
    border: 1px solid #8e60f4;
    box-shadow: 0 0 12px 3px rgba(142, 96, 244, 0.25);
    border-radius: 12px;
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 20px;
    overflow-y: auto;

   
}
</style>
