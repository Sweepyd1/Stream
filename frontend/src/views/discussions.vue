<template>
    <div class="telegram-style">
      <div class="left-panel">
        <div class="header">
          <div class="search-container">
            <input 
              v-model="searchQuery"
              type="text" 
              class="search-input"
              placeholder="Поиск"
            >
            
          </div>
        </div>
  
        <div class="chats-list">
          <div 
            v-for="chat in filteredChats"
            :key="chat.id"
            class="chat-item"
            :class="{ 'active': activeChat?.id === chat.id }"
            @click="selectChat(chat)"
>
            <div class="avatar">
              <img :src="chat.avatar" alt="avatar">
              <span v-if="chat.unread" class="unread">{{ chat.unread }}</span>
            </div>
            
            <div class="chat-info">
              <div class="top-row">
                <h3 class="chat-title">{{ chat.title }}</h3>
                <span class="time">{{ chat.lastMessage.time }}</span>
              </div>
              
              <div class="bottom-row">
                <p class="last-message">{{ chat.lastMessage.text }}</p>
                <span v-if="chat.isOnline" class="online-indicator">●</span>
              </div>
            </div>
          </div>
        </div>
      </div>
  
      <div class="right-panel">
        <div class="chat-header">
          <button v-if="isMobile" class="back-button" @click="activeChat = null">
            ←
          </button>
          <div class="chat-info">
            <h2 class="chat-title">{{ activeChat?.title }}</h2>
            <p class="members-count">{{ activeChat?.members }} участников</p>
          </div>
        </div>
  
        <div class="chat-messages">
          <div 
            v-for="message in activeChat?.messages"
            :key="message.id"
            class="message"
            :class="{ 'outgoing': message.isOutgoing }"
          >
            <div class="message-content">
              <div class="message-header">
                <span class="sender">{{ message.sender }}</span>
                <span class="time">{{ message.time }}</span>
              </div>
              <p class="text">{{ message.text }}</p>
            </div>
          </div>
        </div>
  
        <div class="message-input-container">
          <input 
            v-model="newMessage"
            type="text" 
            class="message-input"
            placeholder="Введите сообщение..."
            @keyup.enter="sendMessage"
          >
          <button class="send-button" @click="sendMessage">
            <svg><!-- Иконка отправки --></svg>
          </button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue'
  
  const activeChat = ref(null)
  const searchQuery = ref('')
  const newMessage = ref('')
  
  const chats = ref([
    {
      id: 1,
      title: 'Наруто: Последний сезон',
      avatar: 'naruto-avatar.jpg',
      members: 2450,
      unread: 3,
      isOnline: true,
      lastMessage: {
        text: 'Обсуждаем 256 серию...',
        time: '12:30'
      },
      messages: [
        {
          id: 1,
          sender: 'Саске',
          text: 'Как вам последний бой?',
          time: '12:25',
          isOutgoing: false
        }
      ]
    },
    // ... другие чаты
  ])
  
  const filteredChats = computed(() => {
  return chats.value.filter(chat => 
    chat.title.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
})
  
  function selectChat(chat) {
    activeChat.value = chat
  }
  
  function sendMessage() {
    if (newMessage.value.trim()) {
      activeChat.value.messages.push({
        id: Date.now(),
        sender: 'Вы',
        text: newMessage.value,
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        isOutgoing: true
      })
      newMessage.value = ''
    }
  }
  
  function openNewChannel() {
    // Логика создания нового канала
  }
  </script>
  
  <style scoped>
  .telegram-style {
    --primary: #6d28d9;
    --secondary: #8e60f4;
    --background: rgba(16, 14, 23, 0.9);
    --accent: rgba(142, 96, 244, 0.1);
    --text-primary: #e5e5e5;
    --text-secondary: #a5a5a5;
    
    display: flex;
    height: 100vh;
    background: var(--background);
    color: var(--text-primary);
    font-family: 'Segoe UI', sans-serif;
  }
  
  .left-panel {
    width: 360px;
    border-right: 1px solid var(--primary);
    background: rgba(16, 14, 23, 0.95);
  }
  
  .search-container {
    padding: 12px;
    display: flex;
    gap: 8px;
    border-bottom: 1px solid var(--primary);
  }
  
  .search-input {
    flex-grow: 1;
    padding: 10px 16px;
    border-radius: 8px;
    background: var(--accent);
    border: none;
    color: var(--text-primary);
  }
  
  .chats-list {
    overflow-y: auto;
    height: calc(100vh - 60px);
  }
  
  .chat-item {
    display: flex;
    align-items: center;
    padding: 12px;
    gap: 15px;
    cursor: pointer;
    transition: background 0.2s;
  }
  
  .chat-item:hover {
    background: var(--accent);
  }
  
  .chat-item.active {
    background: var(--primary);
  }
  
  .avatar {
    position: relative;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    overflow: hidden;
  }
  
  .avatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  .unread {
    position: absolute;
    top: -5px;
    right: -5px;
    background: #ef4444;
    color: white;
    padding: 3px 8px;
    border-radius: 20px;
    font-size: 12px;
  }
  
  .chat-info {
    flex-grow: 1;
    min-width: 0;
  }
  
  .top-row {
    display: flex;
    justify-content: space-between;
    margin-bottom: 4px;
  }
  
  .chat-title {
    font-weight: 500;
    margin: 0;
    font-size: 16px;
  }
  
  .time {
    font-size: 12px;
    color: var(--text-secondary);
  }
  
  .last-message {
    margin: 0;
    font-size: 14px;
    color: var(--text-secondary);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  
  .online-indicator {
    color: #00c853;
    font-size: 14px;
  }
  
  .right-panel {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
  }
  
  .chat-header {
    display: flex;
    align-items: center;
    padding: 16px;
    border-bottom: 1px solid var(--primary);
    gap: 15px;
  }
  
  .chat-messages {
    flex-grow: 1;
    padding: 20px;
    overflow-y: auto;
    background: rgba(16, 14, 23, 0.9);
  }
  
  .message {
    display: flex;
    margin-bottom: 15px;
    max-width: 70%;
  }
  
  .message-content {
    padding: 12px 16px;
    border-radius: 12px;
    background: var(--accent);
  }
  
  .message.outgoing {
    margin-left: auto;
    background: var(--primary);
  }
  
  .message-header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 4px;
    font-size: 14px;
  }
  
  .sender {
    font-weight: 500;
  }
  
  .text {
    margin: 0;
    font-size: 15px;
  }
  
  .message-input-container {
    display: flex;
    padding: 16px;
    gap: 8px;
    border-top: 1px solid var(--primary);
  }
  
  .message-input {
    flex-grow: 1;
    padding: 12px 20px;
    border-radius: 25px;
    border: 1px solid var(--primary);
    background: var(--accent);
    color: var(--text-primary);
  }
  
  .send-button {
    padding: 12px;
    border-radius: 50%;
    background: var(--primary);
    border: none;
    color: white;
    cursor: pointer;
  }
  
  @media (max-width: 768px) {
    .left-panel {
      width: 100%;
      display: block;
    }
    
    .right-panel {
      display: none;
    }
    
    .right-panel.active {
      display: flex;
    }
  }
  </style>