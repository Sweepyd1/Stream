<script setup lang="ts">
import FilterIcon from '@/svg/filter.vue';
import { ref } from 'vue';
import { RouterLink } from 'vue-router';
import { useRoute, useRouter } from 'vue-router'
import Filter from './filter.vue';

import resultSearch from './search.vue';


const router = useRouter()
const route = useRoute()

const isFilterClicked = ref(false);
const isSearching = ref(false);

async function goToLogin() {
    await router.push("/login") 
}

async function goToRegister() {
    await router.push("/register") 
}
</script>

<template>
 <nav class="nav">
            <div class="nav-section">
                <router-link to="/" class="logo">
                    <svg class="icon" viewBox="0 0 24 24">
                        <path fill="currentColor" d="M18.09 10.5V9H20V4H15.5V5.91H18.09V10.5M21 17.5V12H22.5V17.5C22.5 18.88 21.38 20 20 20H4C2.62 20 1.5 18.88 1.5 17.5V6.5C1.5 5.12 2.62 4 4 4H8.5V5.5H4C3.45 5.5 3 5.95 3 6.5V17.5C3 18.05 3.45 18.5 4 18.5H20C20.55 18.5 21 18.05 21 17.5M11.05 15.18L5.42 9.55L6.54 8.43L11.05 12.94L16.23 7.77L17.35 8.88L11.05 15.18Z"/>
                    </svg>
                    <span>Stream</span>
                </router-link>
                
                <div class="nav-buttons">
                    <button class="nav-btn">
                        <svg class="icon" viewBox="0 0 24 24">
                            <path fill="currentColor" d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M7,9.5C7,8.7 7.7,8 8.5,8C9.3,8 10,8.7 10,9.5C10,10.3 9.3,11 8.5,11C7.7,11 7,10.3 7,9.5M12,17.23C10.25,17.23 8.71,16.5 7.81,15.42L9.23,14C9.68,14.72 10.75,15.23 12,15.23C13.25,15.23 14.32,14.72 14.77,14L16.19,15.42C15.29,16.5 13.75,17.23 12,17.23M16.5,11C15.7,11 15,10.3 15,9.5C15,8.7 15.7,8 16.5,8C17.3,8 18,8.7 18,9.5C18,10.3 17.3,11 16.5,11Z"/>
                        </svg>
                        Аниме
                    </button>
                    <button class="nav-btn">
                        <svg class="icon" viewBox="0 0 24 24">
                            <path fill="currentColor" d="M20 6H4V4H20V6M21 12V14H20V20H18V14H14V20H4V14H3V12H4V2H11V12H13V2H20V12H21M6 14V18H16V14H6Z"/>
                        </svg>
                        Сериалы
                    </button>
                    <button class="nav-btn">
                        <svg class="icon" viewBox="0 0 24 24">
                            <path fill="currentColor" d="M20 6H4V4H20V6M21 12V14H20V20H18V14H14V20H4V14H3V12H4V2H11V12H13V2H20V12H21M6 14V18H16V14H6Z"/>
                        </svg>
                        Обсуждения
                    </button>
                </div>
            </div>

            <div class="search-box">
                <svg class="search-icon" viewBox="0 0 24 24">
                    <path fill="currentColor" d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z"/>
                </svg>
                <input 
                    type="text" 
                    placeholder="Поиск аниме, сериалов..."
                    class="search-input"
                    @keyup.enter="isSearching = !isSearching"
                >
            </div>

            <div class="search_result" v-if="isSearching">
                <resultSearch></resultSearch>
            </div>
            
            <div class="auth-btns">

                <FilterIcon @click="isFilterClicked = !isFilterClicked" class="filter_icon"/>
            
                <button @click="goToLogin" class="auth-btn login">
                 
                    <span>Войти</span>
                    <svg class="arrow" viewBox="0 0 24 24">
                        <path fill="currentColor" d="M4,11V13H16L10.5,18.5L11.92,19.92L19.84,12L11.92,4.08L10.5,5.5L16,11H4Z"/>
                    </svg>
                
                </button>
                <button @click="goToRegister" class="auth-btn register">
                    Регистрация
                </button>
            </div>
        </nav>

        <div class="filter" v-if="isFilterClicked">
            <Filter/>
        </div>
        


       

</template>


<style scoped lang="scss">
.nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 5%;
    background: rgba(16, 14, 23, 0.95);
    backdrop-filter: blur(10px);
    position: fixed;
    width: 100%;
    top: 0;
    z-index: 1000;
    border-bottom: 1px solid #2a2639;

    .nav-section {
        display: flex;
        align-items: center;
        gap: 2rem;
    }

    .logo {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 1.5rem;
        font-weight: 700;
        color: #fff;
        text-decoration: none;

        .icon {
            width: 32px;
            height: 32px;
            color: #8e60f4;
        }
    }

    .nav-buttons {
        display: flex;
        gap: 1rem;
    }

    .nav-btn {
        background: none;
        border: none;
        color: #a0aec0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        transition: all 0.3s ease;
        cursor: pointer;

        &:hover {
            background: rgba(142, 96, 244, 0.1);
            color: #8e60f4;
        }

        .icon {
            width: 20px;
            height: 20px;
        }
    }
}


.search-box {
    position: relative;
    width: 30%;

    .search-icon {
        position: absolute;
        left: 1rem;
        top: 50%;
        transform: translateY(-50%);
        width: 20px;
        height: 20px;
        color: #6b7280;
    }

    .search-input {
        width: 100%;
        padding: 0.8rem 1rem 0.8rem 2.5rem;
        background: #1a1625;
        border: 1px solid #2a2639;
        border-radius: 8px;
        color: white;
        font-size: 0.95rem;
        transition: all 0.3s ease;

        &:focus {
            outline: none;
            border-color: #8e60f4;
            box-shadow: 0 0 0 3px rgba(142, 96, 244, 0.2);
        }

        &::placeholder {
            color: #6b7280;
        }
    }
}

.search_result{
    position: absolute;
    left: 39%;
    top: 80%;
}

.auth-btns {
    display: flex;
    gap: 1rem;
    align-items: center;

    .filter_icon{
        cursor: pointer;
        &:hover{
            transform: translateY(-2px);
        }
    }

    .auth-btn {
        padding: 0.8rem 1.5rem;
        border-radius: 8px;
        font-weight: 500;
        transition: all 0.3s ease;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 0.5rem;

        &.login {
            background: linear-gradient(135deg, #8e60f4 0%, #6d28d9 100%);
            border: none;
            color: white;

            &:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(142, 96, 244, 0.4);
            }

            .arrow {
                width: 18px;
                height: 18px;
            }
        }

        &.register {
            background: none;
            border: 1px solid #2a2639;
            color: #8e60f4;

            &:hover {
                background: rgba(142, 96, 244, 0.1);
            }
        }
    }
}

.filter {
    position: fixed; 
    left: 50%; 
    top: 50%; 
    z-index: 100000000;
    transform: translate(-50%, -50%); 
}


</style>