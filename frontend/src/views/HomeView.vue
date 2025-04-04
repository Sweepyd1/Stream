<script setup lang="ts">
import Header from '@/components/header.vue';
import anime_card from '@/components/anime_card.vue';
import {getDataOnMainPage} from "@/api/mainPage"
import { onMounted, ref } from 'vue';


const data = ref();
onMounted(async()=> {
    data.value = await getDataOnMainPage()
    console.log("ВЫПОЛНИЛ ЗАПРОС")
    console.log(data.value[0])
})

</script>

<template>
<div class="container">
    <Header></Header>
   

    <div class="hero-banner">
        <div class="hero-content">
            <h1>Откройте мир аниме</h1>
            <p>Тысячи сериалов в HD качестве с профессиональной озвучкой</p>
          
        </div>
    </div>

 
    <main class="main-content">
     
        <section class="content-section">
            <div class="section-header">
                <h2>Популярное сейчас</h2>
                <router-link to="/popular" class="see-all">
                    Смотреть все
                    <svg class="arrow" viewBox="0 0 24 24">
                        <path fill="currentColor" d="M8.59,16.58L13.17,12L8.59,7.41L10,6L16,12L10,18L8.59,16.58Z"/>
                    </svg>
                </router-link>
            </div>
            <div class="anime-grid">
                <anime_card v-for="n in 6" :key="n"/>
            </div>
        </section>

     
        <section class="content-section">
            <div class="section-header">
                <h2>Новинки сезона</h2>
                <div class="season-filter">
                    <span>Лето 2024</span>
                    <svg class="chevron" viewBox="0 0 24 24">
                        <path fill="currentColor" d="M7.41,8.58L12,13.17L16.59,8.58L18,10L12,16L6,10L7.41,8.58Z"/>
                    </svg>
                </div>
            </div>
            <div class="anime-carousel">
                <anime_card 
            v-for="anime in data" 
            :key="anime.video_url" 
            :title="anime.title" 
            :cover_url="anime.cover_url"
            :video_url="anime.video_url"
            :genres="anime.genres"
            class="carousel-item"
        />
            </div>
        </section>

   
        <section class="genres-section">
            <h2>Популярные жанры</h2>
            <div class="genre-grid">
                <div class="genre-card" v-for="genre in genres" :key="genre">
                    <div class="genre-icon">
                        <svg viewBox="0 0 24 24">
                            <path fill="currentColor" />
                        </svg>
                    </div>
                    <span>{{ genre }}</span>
                </div>
            </div>
        </section>
    </main>
</div>
</template>

<style scoped lang="scss">
.container {
    background: #0a0a0e;
    color: white;
    font-family: 'Rubik', sans-serif;
    min-height: 100vh;
}

.hero-banner {
    position: relative;
    height: 40vh;
    background: linear-gradient(135deg, rgba(16, 14, 23, 0.9) 0%, rgba(42, 38, 57, 0.8) 100%),
                url('@/assets/anime-bg.jpg');
    background-size: cover;
    background-position: center;
    display: flex;
    align-items: center;
    padding: 0 5%;
    margin-top: 60px;

    .hero-content {
        max-width: 800px;
        z-index: 2;

        h1 {
            font-size: 3.5rem;
            margin-bottom: 1.5rem;
            background: linear-gradient(45deg, #8e60f4, #6d28d9);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        p {
            font-size: 1.4rem;
            color: #cbd5e1;
            margin-bottom: 2.5rem;
        }
    }

    .search-bar {
        position: relative;
        max-width: 600px;

        input {
            width: 100%;
            padding: 1.2rem 2rem 1.2rem 4rem;
            background: rgba(255, 255, 255, 0.1);
            border: 2px solid #2a2639;
            border-radius: 50px;
            color: white;
            font-size: 1.1rem;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;

            &:focus {
                outline: none;
                border-color: #8e60f4;
                background: rgba(142, 96, 244, 0.1);
            }

            &::placeholder {
                color: #a0aec0;
            }
        }

        .search-icon {
            position: absolute;
            left: 1.5rem;
            top: 50%;
            transform: translateY(-50%);
            width: 24px;
            height: 24px;
            color: #8e60f4;
        }
    }
}

.main-content {
    padding: 4rem 5%;
}

.content-section {
    margin-bottom: 4rem;

    .section-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 2rem;

        h2 {
            font-size: 2rem;
            position: relative;
            padding-left: 1rem;

            &::before {
                content: '';
                position: absolute;
                left: 0;
                top: 50%;
                transform: translateY(-50%);
                width: 4px;
                height: 80%;
                background: #8e60f4;
                border-radius: 2px;
            }
        }

        .see-all {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: #8e60f4;
            text-decoration: none;
            transition: all 0.3s ease;

            &:hover {
                opacity: 0.8;
                transform: translateX(5px);
            }

            .arrow {
                width: 24px;
                height: 24px;
            }
        }

        .season-filter {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem 1rem;
            background: rgba(142, 96, 244, 0.1);
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;

            &:hover {
                background: rgba(142, 96, 244, 0.2);
            }

            .chevron {
                width: 20px;
                height: 20px;
            }
        }
    }
}

.anime-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 2rem;
}

.anime-carousel {
    display: flex;
    gap: 1.5rem;
    overflow-x: auto;
    padding-bottom: 1rem;

    &::-webkit-scrollbar {
        height: 8px;
    }

    &::-webkit-scrollbar-track {
        background: #1a1625;
    }

    &::-webkit-scrollbar-thumb {
        background: #8e60f4;
        border-radius: 4px;
    }

    .carousel-item {
        flex: 0 0 300px;
    }
}

.genres-section {
    margin-top: 4rem;

    h2 {
        font-size: 2rem;
        margin-bottom: 2rem;
    }

    .genre-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
        gap: 1.5rem;
    }

    .genre-card {
        background: #1a1625;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;

        &:hover {
            transform: translateY(-5px);
            background: #231f2e;
        }

        .genre-icon {
            width: 60px;
            height: 60px;
            background: rgba(142, 96, 244, 0.1);
            border-radius: 50%;
            margin: 0 auto 1rem;
            display: flex;
            align-items: center;
            justify-content: center;

            svg {
                width: 32px;
                height: 32px;
                color: #8e60f4;
            }
        }

        span {
            font-weight: 500;
            color: #cbd5e1;
        }
    }
}

@media (max-width: 768px) {
    .hero-banner {
        height: 50vh;
        padding: 0 1.5rem;

        .hero-content {
            h1 {
                font-size: 2.5rem;
            }

            p {
                font-size: 1.1rem;
            }
        }

        .search-bar input {
            padding: 1rem 1.5rem 1rem 3.5rem;
        }
    }

    .main-content {
        padding: 2rem 1.5rem;
    }

    .content-section .section-header h2 {
        font-size: 1.5rem;
    }

    .anime-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
    }

    .genre-grid {
        grid-template-columns: repeat(3, 1fr) !important;
    }
}
</style>

<script lang="ts">
export default {
    data() {
        return {
            genres: ['Сёнэн', 'Романтика', 'Фэнтези', 'Драма', 'Комедия', 'Мистика'],
            genreIcons: {
                'Сёнэн': 'M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M8.43,14.44L7.07,13.83C7.35,13.27 7.5,12.67 7.5,12.05C7.5,11.39 7.35,10.76 7.08,10.19L8.43,9.56C8.81,10.41 9,11.22 9,12.05C9,12.88 8.81,13.72 8.43,14.44M11.53,15.94L10.22,15.29C10.75,14.16 11,12.94 11,11.63C11,10.36 10.77,9.18 10.27,8.07L11.58,7.42C12.17,8.72 12.44,10.13 12.44,11.63C12.44,13.13 12.17,14.58 11.53,15.94M14.57,14.44C14.19,13.72 14,12.88 14,12.05C14,11.22 14.19,10.41 14.57,9.56L15.92,10.19C15.65,10.76 15.5,11.39 15.5,12.05C15.5,12.67 15.65,13.27 15.93,13.83L14.57,14.44M12.42,7.42L13.73,8.07C13.23,9.18 13,10.36 13,11.63C13,12.94 13.25,14.16 13.78,15.29L12.47,15.94C11.83,14.58 11.56,13.13 11.56,11.63C11.56,10.13 11.83,8.72 12.42,7.42Z',
                'Романтика': 'M12 18C12 14.9 14.69 13.37 17.5 13.37C20.31 13.37 23 14.9 23 18V20H12V18M17.5 12C15.57 12 14 10.43 14 8.5C14 6.57 15.57 5 17.5 5C19.43 5 21 6.57 21 8.5C21 10.43 19.43 12 17.5 12M10 18C10 14.9 12.68 13.38 15.5 13.38C15.74 13.38 15.97 13.39 16.2 13.41C15.5 13.73 15 14.35 15 15.06V15.5H4V18C4 19.11 4.89 20 6 20H10.54C10.02 19.42 10 18.74 10 18M15.5 12C13.57 12 12 10.43 12 8.5C12 6.57 13.57 5 15.5 5C17.43 5 19 6.57 19 8.5C19 10.43 17.43 12 15.5 12Z',
                'Фэнтези': 'M12,2C8,2 4.46,5.05 4.1,9H4V12C4,13.1 4.9,14 6,14H7V20H17V14H18C19.1,14 20,13.1 20,12V9H19.9C19.54,5.05 16,2 12,2M12,4C14.76,4 17,6.24 17,9C17,11.87 14.12,11.04 12,8.89C9.88,11.04 7,11.87 7,9C7,6.24 9.24,4 12,4M10,15V18H14V15H10Z',
                'Драма': 'M13,19C13.69,19 14.37,18.93 15,18.81C15,19.2 15,19.59 15,20C14.37,20 13.69,20 13,20C10.34,20 8,17.64 8,15C8,13.07 9.03,11.41 10.56,10.56L9.12,8.37C7.25,9.57 6,11.66 6,14C6,17.31 8.69,20 12,20V22L15,19L12,16V18C9.79,18 8,16.21 8,14C8,12.14 9.28,10.59 11,10.14V12.28C10.4,12.63 10,13.26 10,14C10,15.1 10.9,16 12,16C13.1,16 14,15.1 14,14C14,13.26 13.6,12.62 13,12.28V10.14C14.72,10.59 16,12.14 16,14C16,14.73 15.81,15.41 15.5,16.03C14.55,15.12 13.3,14.58 12,14.58C11.66,14.58 11.33,14.62 11,14.7C11,14.91 11,15.12 11,15.33C11.33,15.27 11.66,15.22 12,15.22C13.3,15.22 14.55,15.76 15.5,16.67C15.81,16.22 16,15.7 16,15.16C16,14.86 16,14.57 15.94,14.29C16.64,13.57 17,12.61 17,11.57C17,10.27 16.35,9.12 15.36,8.4L16.8,6.2C18.39,7.5 19.5,9.4 19.5,11.57C19.5,13.25 18.89,14.8 17.92,16C17.62,16 17.33,16 17.04,16C17.03,16 17,16 17,16C17,16 17,16 17.04,16C17.34,16 17.67,16 18,16V16Z',
                'Комедия': 'M12,2C6.48,2 2,6.48 2,12C2,17.52 6.48,22 12,22C17.52,22 22,17.52 22,12C22,6.48 17.52,2 12,2M8.5,11C7.67,11 7,10.33 7,9.5C7,8.67 7.67,8 8.5,8C9.33,8 10,8.67 10,9.5C10,10.33 9.33,11 8.5,11M15.5,11C14.67,11 14,10.33 14,9.5C14,8.67 14.67,8 15.5,8C16.33,8 17,8.67 17,9.5C17,10.33 16.33,11 15.5,11M12,17.75C14.86,17.75 17.25,15.36 17.25,12.5C17.25,11.67 16.58,11 15.75,11H8.25C7.42,11 6.75,11.67 6.75,12.5C6.75,15.36 9.14,17.75 12,17.75Z',
                'Мистика': 'M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2M12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20A8,8 0 0,0 20,12A8,8 0 0,0 12,4M12,6.5A1.5,1.5 0 0,1 13.5,8A1.5,1.5 0 0,1 12,9.5A1.5,1.5 0 0,1 10.5,8A1.5,1.5 0 0,1 12,6.5M12,14.5C13.66,14.5 15,15.34 15,16.5C15,17.66 13.66,18.5 12,18.5C10.34,18.5 9,17.66 9,16.5C9,15.34 10.34,14.5 12,14.5M6.5,10C7.33,10 8,10.67 8,11.5C8,12.33 7.33,13 6.5,13C5.67,13 5,12.33 5,11.5C5,10.67 5.67,10 6.5,10M17.5,10C18.33,10 19,10.67 19,11.5C19,12.33 18.33,13 17.5,13C16.67,13 16,12.33 16,11.5C16,10.67 16.67,10 17.5,10Z'
            }
        }
    }
}
</script>