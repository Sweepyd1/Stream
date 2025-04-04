<script lang="ts" setup>
import Header from '@/components/header.vue';
import anime_card from '@/components/anime_card.vue';

</script>
<template>
    <div class="container">
        
        <Header/>

        <div class="hero">
            <div class="hero-overlay"></div>
            <img src='@/assets/test_photo/test_norm.jpg' alt="Anime Banner" class="hero-image"/>
            
            <div class="hero-content">
                <h1>Добро пожаловать в Stream</h1>
                <p>Смотрите лучшие аниме и сериалы</p>
                <button class="cta-btn">
                    Перейти на главную страницу
                    <svg class="play-icon" viewBox="0 0 24 24">
                        <path fill="currentColor" d="M8,5.14V19.14L19,12.14L8,5.14Z"/>
                    </svg>
                </button>
            </div>
        </div>

  
        <div class="profile-section">
            <div class="avatar-container">
                <div class="avatar-frame">
                    <img src='@/assets/test_photo/avatar.jpg' alt="Аватар" class="avatar"/>
                    <div class="online-status"></div>
                </div>
                <button class="edit-btn">
                    <span>Редактировать</span>
                    <svg class="edit-icon" viewBox="0 0 24 24" >
                        <path fill="currentColor" d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z"/>
                    </svg>
                </button>
            </div>

            <div class="profile-info">
                <div class="user-main">
                    <h2 class="username">Sweepyd1</h2>
                    <div class="stats">
                        <div class="stat-item">
                            <span class="stat-value">0</span>
                            <span class="stat-label">Просмотрено</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-value">0</span>
                            <span class="stat-label">что-то</span>
                        </div>
                    </div>
                </div>
                
                <p class="bio">
                  люблю смотреть аниме и сериалы такое вот хобби:)
                </p>

                <div class="actions">
                    <button class="action-btn watchlist">
                        <svg class="icon" viewBox="0 0 24 24">
                            <path fill="currentColor" d="M14,10H3V12H14V10M14,6H3V8H14V6M3,16H10V14H3V16M21.5,11.5L23,13L16,20L11.5,15.5L13,14L16,17L21.5,11.5Z"/>
                        </svg>
                        Мой список
                    </button>
                    <button class="action-btn history">
                        <svg class="icon" viewBox="0 0 24 24">
                            <path fill="currentColor" d="M13.5,8H12V13L16.28,15.54L17,14.33L13.5,12.25V8M13,3A9,9 0 0,0 4,12H1L4.96,16.03L9,12H6A7,7 0 0,1 13,5A7,7 0 0,1 20,12A7,7 0 0,1 13,19C11.07,19 9.32,18.21 8.06,16.94L6.64,18.36C8.27,20 10.5,21 13,21A9,9 0 0,0 22,12A9,9 0 0,0 13,3"/>
                        </svg>
                        История
                    </button>
                </div>
            </div>
        </div>

     
        <section class="recently-watched">
            <h3>Недавно просмотрено</h3>
            <div class="carousel">

                <anime_card></anime_card>
                
          
                
         
            </div>
        </section>
    </div>
</template>

<style scoped lang="scss">


.container {
    background: #0a0a0e;
    color: white;
    font-family: 'Rubik', sans-serif;
    min-height: 100vh;
}




.hero {
    position: relative;
    height: 70vh;
    margin-top: 60px;

    .hero-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(180deg, rgba(16, 14, 23, 0) 0%, #0a0a0e 100%);
        z-index: 1;
    }

    .hero-image {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .hero-content {
        position: absolute;
        bottom: 20%;
        left: 5%;
        z-index: 2;
        max-width: 600px;

        h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            line-height: 1.1;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
        }

        p {
            font-size: 1.2rem;
            color: #cbd5e1;
            margin-bottom: 2rem;
        }
    }

    .cta-btn {
        background: #8e60f4;
        color: white;
        padding: 1rem 2rem;
        border: none;
        border-radius: 8px;
        font-size: 1.1rem;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        cursor: pointer;
        transition: all 0.3s ease;

        &:hover {
            background: #7c51e0;
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(142, 96, 244, 0.4);
        }

        .play-icon {
            width: 24px;
            height: 24px;
        }
    }
}


.profile-section {
    display: flex;
    gap: 2rem;
    padding: 3rem 5%;
    background: #0f0e15;
    margin: 2rem 0;
    border-radius: 12px;
    position: relative;

    .avatar-container {
        position: relative;
        flex-shrink: 0;

        .avatar-frame {
            position: relative;
            width: 150px;
            height: 150px;
            border-radius: 50%;
            overflow: hidden;
            border: 3px solid #8e60f4;
            box-shadow: 0 0 20px rgba(142, 96, 244, 0.3);

            .avatar {
                width: 100%;
                height: 100%;
                object-fit: cover;
            }
        }

        .online-status {
            position: absolute;
            bottom: 10px;
            right: 10px;
            width: 16px;
            height: 16px;
            background: #4ade80;
            border: 2px solid #0f0e15;
            border-radius: 50%;
        }

        .edit-btn {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
            position: absolute;
            bottom: 4px;
            left: 50%;
            transform: translateX(-50%);
            background: #8e60f4;
            border: none;
            padding: 0.5rem;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;

            span{
                font-size: 18px;
                font-weight: 500;
                color:white                
            }

            &:hover {
                background: #7c51e0;
                transform: translateX(-50%) translateY(-2px);
            }

            .edit-icon {
                width: 20px;
                height: 25px;
                color: white;
            }
        }
    }

    .profile-info {
        flex-grow: 1;

        .username {
            font-size: 2rem;
            margin-bottom: 0.5rem;
            color: #fff;
        }

        .stats {
            display: flex;
            gap: 2rem;
            margin-bottom: 1.5rem;

            .stat-item {
                text-align: center;

                .stat-value {
                    font-size: 1.5rem;
                    font-weight: 600;
                    color: #8e60f4;
                    display: block;
                }

                .stat-label {
                    color: #a0aec0;
                    font-size: 0.9rem;
                }
            }
        }

        .bio {
            color: #cbd5e1;
            line-height: 1.6;
            margin-bottom: 1.5rem;
            white-space: pre-line;
        }

        .actions {
            display: flex;
            gap: 1rem;

            .action-btn {
                background: #1a1625;
                border: 1px solid #2a2639;
                color: #8e60f4;
                padding: 0.8rem 1.5rem;
                border-radius: 8px;
                display: flex;
                align-items: center;
                gap: 0.5rem;
                cursor: pointer;
                transition: all 0.3s ease;

                &:hover {
                    background: rgba(142, 96, 244, 0.1);
                    transform: translateY(-2px);
                }

                .icon {
                    width: 20px;
                    height: 20px;
                }
            }
        }
    }
}


.recently-watched {
    padding: 0 5% 3rem;

    h3 {
        font-size: 1.5rem;
        margin-bottom: 1.5rem;
        color: #fff;
    }

    .carousel {
        display: flex;
        gap: 1.5rem;
        overflow-x: auto;
        padding-bottom: 1rem;
    }

   
}


@media (max-width: 768px) {
    .nav {
        flex-wrap: wrap;
        gap: 1rem;
        padding: 1rem;

        .nav-section {
            order: 1;
            width: 100%;
            justify-content: space-between;
        }

        .search-box {
            order: 3;
            width: 100%;
        }

        .auth-btns {
            order: 2;
        }
    }

    .hero-content {
        h1 {
            font-size: 2rem !important;
        }

        p {
            font-size: 1rem !important;
        }
    }

    .profile-section {
        flex-direction: column;
        align-items: center;
        text-align: center;

        .stats {
            justify-content: center;
        }

        .actions {
            flex-direction: column;
        }
    }
}
</style>