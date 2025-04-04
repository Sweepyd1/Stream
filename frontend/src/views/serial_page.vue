<script setup lang="ts">
import Header from '@/components/header.vue';
import cover_card from '@/components/cover_card.vue';
import { ref } from 'vue';
import  Rating  from 'primevue/rating';
const rating = ref(4); 
</script>

<template>
<div class="container">
    <Header />

    <div class="videoplayer">
        <img src="@/assets/test_photo/test3.webp" alt="Video Player">
    </div>

    <div class="serial_section">
        <div class="name_serial">
            <span>Тетрадь смерти</span>
        </div>
        <div class="about">
            <div class="cover">
                <img src="@/assets/test_photo/cover.jpg" alt="Cover Image">
            </div>
            <div class="info">
                <Rating v-model="rating" :cancel="false" :stars="5" />
                <h2>Информация об аниме</h2>
                <p><strong>Год выпуска:</strong> 2006</p>
                <p><strong>Автор:</strong> Tsugumi Ohba</p>
                <p><strong>Количество сезонов:</strong> 1</p>
                <p><strong>Жанр:</strong> Мистика, Психологический триллер, Суперестественное</p>
                <p><strong>Описание:</strong> Тетрадь смерти — это история о школьнике по имени Лайт Ягами, который находит таинственную тетрадь, позволяющую убивать людей, просто написав их имя в ней.</p>
            </div>
        </div>
        <div class="choose_season">
            <div class="season">
                <span>сезон 1</span>
            </div>
            <div class="season">
                <span>сезон 2</span>

            </div>
        </div>
        <div class="cover_grid">
            <cover_card></cover_card>
            <cover_card></cover_card>
            <cover_card></cover_card>
            <cover_card></cover_card>
            <cover_card></cover_card>

            <cover_card></cover_card>
            <cover_card></cover_card>
            <cover_card></cover_card>
            <cover_card></cover_card>
            <cover_card></cover_card>

            <cover_card></cover_card>
            <cover_card></cover_card>
            <cover_card></cover_card>
            <cover_card></cover_card>
            <cover_card></cover_card>

        </div>

        <div class="comments">
    <div class="comments-header">
        <h3>25 комментариев</h3>
    </div>
    
    <div class="comment-list">
        <!-- Пример комментария -->
        <div class="comment-item">
            <div class="avatar">
                <img src="@/assets/test_photo/avatar.jpg" alt="User Avatar">
            </div>
            <div class="comment-content">
                <div class="comment-header">
                    <span class="username">Sweepyd1</span>
                    <span class="comment-time">2 часа назад</span>
                </div>
                <p class="comment-text">Это просто шедевр! Пересматриваю уже в третий раз, и каждый раз нахожу новые детали.</p>
                <div class="comment-actions">
                    <button class="like-btn">
                        <svg class="icon" viewBox="0 0 24 24">
                            <path fill="currentColor" d="M23,10C23,8.89 22.1,8 21,8H14.68L15.64,3.43C15.66,3.33 15.67,3.22 15.67,3.11C15.67,2.7 15.5,2.32 15.23,2.05L14.17,1L7.59,7.58C7.22,7.95 7,8.45 7,9V19C7,20.1 7.9,21 9,21H18C18.83,21 19.54,20.5 19.84,19.78L22.86,12.73C22.95,12.5 23,12.26 23,12V10M1,21H5V9H1V21Z"/>
                        </svg>
                        42
                    </button>
                    <span class="answer">Ответить</span>
                </div>
            </div>
        </div>

        <!-- Еще один пример -->
        <div class="comment-item">
            <div class="avatar">
                <div class="avatar-placeholder">A</div>
            </div>
            <div class="comment-content">
                <div class="comment-header">
                    <span class="username">AnimeFan2024</span>
                    <span class="comment-time">5 часов назад</span>
                </div>
                <p class="comment-text">Лучшее аниме всех времен! Финал просто взорвал мозг 🤯</p>
                <div class="comment-actions">
                    <button class="like-btn">
                        <svg class="icon" viewBox="0 0 24 24">
                            <path fill="currentColor" d="M23,10C23,8.89 22.1,8 21,8H14.68L15.64,3.43C15.66,3.33 15.67,3.22 15.67,3.11C15.67,2.7 15.5,2.32 15.23,2.05L14.17,1L7.59,7.58C7.22,7.95 7,8.45 7,9V19C7,20.1 7.9,21 9,21H18C18.83,21 19.54,20.5 19.84,19.78L22.86,12.73C22.95,12.5 23,12.26 23,12V10M1,21H5V9H1V21Z"/>
                        </svg>
                        28
                    </button>
                    <span class="answer">Ответить</span>
                </div>
            </div>
        </div>
    </div>

    <div class="comment-form">
        <div class="avatar">
            <!-- <img src="@/assets/test_photo/avatar.jpg" alt="Your Avatar"> -->
        </div>
        <div class="input-wrapper">
            <input 
                type="text" 
                placeholder="Напишите комментарий..."
                class="comment-input"
            >
            <button class="send-btn">
                <svg class="icon" viewBox="0 0 24 24">
                    <path fill="currentColor" d="M2,21L23,12L2,3V10L17,12L2,14V21Z"/>
                </svg>
            </button>
        </div>
    </div>
</div>
    </div>
</div>
</template>

<style scoped lang="scss">

.container {
    background: #0a0a0e;
    color: white;
    font-family: 'Rubik', sans-serif;
    min-height: 100vh;

    .videoplayer {
        height: 60vh;
        width: 100%;

        img {
            width: 100%;
            height: 100%;
        }
    }
    .serial_section {
        margin-left: 5%;

        .name_serial {
            margin-top: 10px;
            span {
                font-size: 30px;
                font-weight: 600;
            }
        }
        .about {
            display: flex; 
            margin-top: 20px;

            .cover {
                position: relative;
            &::before {
                content: '';
                position: absolute;
                left: 0;
                top: 49%;
                transform: translateY(-50%);
                width: 4px;
                height: 98%;
                background: #8e60f4;
                border-radius: 2px;
            }
                img {
                    width: 200px;     
                    height:230px;     
                    object-fit: cover; 
                }
            }
            .info {
                margin-left: 20px;
                
                h2 {
                    font-size: 24px;
                    margin-bottom: 10px;
                }
                p {
                    font-size: 16px;
                    margin: 5px 0;
                }
            }
        }  
        .choose_season{
            display: flex;
            gap: 20px;
            margin-top: 20px;

            .season{
                width: 100px;
                height: 30px;
                border-radius: 20px;
                border: 1px solid rgb(33, 31, 41);;
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: pointer;
            
                &:hover {
                    background: rgba(142, 96, 244, 0.1);
                    color: #8e60f4;
                    box-shadow: 0 0 0 1px rgba(142, 96, 244, 0.2);
                    transition: all 0.3s ease;
        }

                span{
                    font-weight: 500;
                    font-size: 18px;
                }
            }
        }
        .cover_grid{
            width: 95%;
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 20px;
            margin-top: 20px;
        }

        .comments {
    margin-top: 40px;
    padding: 20px;
    background: #111016;
    border-radius: 12px;
    width: 95%;

    .comments-header {
        margin-bottom: 30px;
        
        h3 {
            font-size: 1.5rem;
            color: #fff;
            border-left: 4px solid #8e60f4;
            padding-left: 12px;
        }
    }

    .comment-list {
        display: flex;
        flex-direction: column;
        gap: 25px;
    }

    .comment-item {
        display: flex;
        gap: 15px;
        padding: 15px;
        background: #1a1625;
        border-radius: 8px;
        transition: transform 0.2s ease;

        &:hover {
            transform: translateX(5px);
        }

        .avatar {
            flex-shrink: 0;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            overflow: hidden;

            img {
                width: 100%;
                height: 100%;
                object-fit: cover;
            }

            .avatar-placeholder {
                width: 100%;
                height: 100%;
                background: linear-gradient(135deg, #8e60f4, #6d28d9);
                display: flex;
                align-items: center;
                justify-content: center;
                font-weight: 600;
                color: white;
            }
        }

        .comment-content {
            flex-grow: 1;

            .comment-header {
                display: flex;
                align-items: center;
                gap: 10px;
                margin-bottom: 8px;

                .username {
                    font-weight: 600;
                    color: #fff;
                }

                .comment-time {
                    font-size: 0.85rem;
                    color: #6b7280;
                }
            }

            .comment-text {
                color: #cbd5e1;
                line-height: 1.5;
                margin-bottom: 12px;
            }

            .comment-actions {
                display: flex;
                align-items: center;
                gap: 15px;

                .like-btn {
                    display: flex;
                    align-items: center;
                    gap: 6px;
                    background: none;
                    border: none;
                    color: #6b7280;
                    cursor: pointer;
                    padding: 4px 8px;
                    border-radius: 6px;
                    transition: all 0.2s ease;

                    &:hover {
                        color: #8e60f4;
                        background: rgba(142, 96, 244, 0.1);
                    }

                    .icon {
                        width: 18px;
                        height: 18px;
                    }

                 
                }
                span{
                    color: rgba(142, 96, 244, 0.5);
                    cursor: pointer;
                }
            }
        }
    }

    .comment-form {
        margin-top: 30px;
        display: flex;
        gap: 15px;
        align-items: center;

        .avatar {
            width: 50px;
            height: 50px;
        }

        .input-wrapper {
            flex-grow: 1;
            position: relative;

            .comment-input {
                width: 100%;
                padding: 12px 50px 12px 20px;
                background: #1a1625;
                border: 1px solid #2a2639;
                border-radius: 25px;
                color: white;
                font-size: 1rem;
                transition: all 0.3s ease;

                &:focus {
                    outline: none;
                    border-color: #8e60f4;
                    box-shadow: 0 0 0 3px rgba(142, 96, 244, 0.2);
                }
            }

            .send-btn {
                position: absolute;
                right: 10px;
                top: 50%;
                transform: translateY(-50%);
                background: none;
                border: none;
                padding: 8px;
                cursor: pointer;
                color: #6b7280;
                transition: all 0.2s ease;

                &:hover {
                    color: #8e60f4;
                }

                .icon {
                    width: 24px;
                    height: 24px;
                }
            }
        }
    }
}

@media (max-width: 768px) {
    .comments {
        padding: 15px;
        
        .comment-item {
            padding: 12px;
            
            .avatar {
                width: 35px;
                height: 35px;
            }
        }
        
        .comment-form .avatar {
            width: 40px;
            height: 40px;
        }
    }
}
    }
}
</style>
