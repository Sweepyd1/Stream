<template>
    <div class="custom-player">
      <video 
        ref="videoPlayer"
        class="video-element"
        @timeupdate="updateProgress"
        @loadedmetadata="updateDuration"
        autoplay
      >
        <source src="https://cache.libria.fun/videos/media/ts/9000/1/1080/7f3c1729ebd24b93d4e0918510004606.m3u8" type="application/x-mpegURL">
      </video>
  
      <div class="controls-container">
       
        <div class="progress-bar" @click="seekVideo">
          <div 
            class="progress" 
            :style="{ width: progress + '%' }"
          ></div>
        </div>
  
       
        <div class="main-controls">
          <button class="control-btn" @click="togglePlay">
            <svg v-if="!isPlaying" class="icon">
              <path d="M8 5v14l11-7z"/>
            </svg>
            <svg v-else class="icon">
              <path d="M6 4h4v16H6zm8 0h4v16h-4z"/>
            </svg>
          </button>
  
          <div class="time-display">
            {{ formatTime(currentTime) }} / {{ formatTime(duration) }}
          </div>
  
          <div class="volume-control">
            <button class="control-btn" @click="toggleMute">
              <svg v-if="isMuted" class="icon">
                <path d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51C20.63 14.91 21 13.5 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3L3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06c1.38-.31 2.63-.95 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4L9.91 6.09 12 8.18V4z"/>
              </svg>
              <svg v-else class="icon">
                <path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/>
              </svg>
            </button>
            <input
              type="range"
              class="volume-slider"
              min="0"
              max="1"
              step="0.1"
              v-model="volume"
              @input="updateVolume"
            >
          </div>
  
          <button class="control-btn" @click="toggleFullscreen">
            <svg class="icon">
              <path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  
  const videoPlayer = ref(null);
  const isPlaying = ref(false);
  const currentTime = ref(0);
  const duration = ref(0);
  const progress = ref(0);
  const volume = ref(1);
  const isMuted = ref(false);
  
  const props = defineProps({
    videoSource: {
      type: String,
      required: true
    }
  });
  
  const togglePlay = () => {
    if (videoPlayer.value.paused) {
      videoPlayer.value.play();
      isPlaying.value = true;
    } else {
      videoPlayer.value.pause();
      isPlaying.value = false;
    }
  };
  
  const updateProgress = () => {
    currentTime.value = videoPlayer.value.currentTime;
    progress.value = (currentTime.value / duration.value) * 100;
  };
  
  const updateDuration = () => {
    duration.value = videoPlayer.value.duration;
  };
  
  const seekVideo = (e) => {
    const rect = e.target.getBoundingClientRect();
    const pos = (e.clientX - rect.left) / rect.width;
    videoPlayer.value.currentTime = pos * duration.value;
  };
  
  const updateVolume = () => {
    videoPlayer.value.volume = volume.value;
    isMuted.value = volume.value === 0;
  };
  
  const toggleMute = () => {
    isMuted.value = !isMuted.value;
    videoPlayer.value.muted = isMuted.value;
    volume.value = isMuted.value ? 0 : 1;
  };
  
  const formatTime = (seconds) => {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = Math.floor(seconds % 60);
    return `${String(minutes).padStart(2, '0')}:${String(remainingSeconds).padStart(2, '0')}`;
  };
  
  const toggleFullscreen = () => {
    if (!document.fullscreenElement) {
      videoPlayer.value.requestFullscreen();
    } else {
      document.exitFullscreen();
    }
  };
  
  onMounted(() => {
    videoPlayer.value.volume = volume.value;
  });
  </script>
  
  <style scoped lang="scss">
  .custom-player {
    position: relative;
    max-width: 1800px;
    // min-height: 1000px;
    margin: 20px auto;
    background: #1a1625;
    border-radius: 12px;
    overflow: hidden;
  
    .video-element {
      width: 100%;
      height: 450px;
      object-fit: cover;
    }
  
    .controls-container {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      padding: 15px;
      background: linear-gradient(transparent, rgba(0, 0, 0, 0.8));
      color: white;
    }
  
    .progress-bar {
      height: 5px;
      background: rgba(255, 255, 255, 0.2);
      border-radius: 3px;
      cursor: pointer;
      margin-bottom: 10px;
  
      .progress {
        height: 100%;
        background: #8e60f4;
        border-radius: 3px;
        transition: width 0.1s linear;
      }
    }
  
    .main-controls {
      display: flex;
      align-items: center;
      gap: 20px;
  
      .control-btn {
        background: none;
        border: none;
        padding: 8px;
        cursor: pointer;
        color: white;
        transition: all 0.2s ease;
  
        &:hover {
          color: #8e60f4;
          transform: scale(1.1);
        }
  
        .icon {
          width: 24px;
          height: 24px;
          fill: currentColor;
        }
      }
  
      .time-display {
        font-size: 0.9rem;
        color: #cbd5e1;
        margin-right: auto;
      }
  
      .volume-control {
        display: flex;
        align-items: center;
        gap: 10px;
  
        .volume-slider {
          width: 100px;
          height: 4px;
          -webkit-appearance: none;
          background: rgba(255, 255, 255, 0.2);
          border-radius: 2px;
          outline: none;
  
          &::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 12px;
            height: 12px;
            background: #8e60f4;
            border-radius: 50%;
            cursor: pointer;
          }
        }
      }
    }
  }
  
  @media (max-width: 768px) {
    .custom-player {
      .video-element {
        height: 300px;
      }
  
      .main-controls {
        gap: 10px;
  
        .volume-control {
          .volume-slider {
            width: 80px;
          }
        }
      }
    }
  }
  </style> 
