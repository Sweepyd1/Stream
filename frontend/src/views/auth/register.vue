<script setup lang="ts">
import {ref} from "vue";
import {registerUser} from "@/api/auth"
import {NewUser} from "@/models/auth"


const email = ref<string | undefined>(undefined);
const password = ref<string | undefined>(undefined);
const username = ref<string | undefined>(undefined);

async function clickRegister() {
    const userLogin = new NewUser(email.value || '', password.value || '', username.value || '' );
    try {
        const response = await registerUser(userLogin);
        console.log("User register in successfully:", response);
    } catch (error) {
        console.error("Error logging in:", error);
    }
}
</script>

<template>
    <div class="container">
        <div class="auth-card">
            <div class="header">
              <h2>Авторизация</h2>
              <p>Please sign in to continue</p>
            </div>
    
            <div class="form">
                <div class="input-group">
                    <svg class="icon" viewBox="0 0 24 24">
                        <path fill="currentColor" d="M12,4A4,4 0 0,1 16,8A4,4 0 0,1 12,12A4,4 0 0,1 8,8A4,4 0 0,1 12,4M12,14C16.42,14 20,15.79 20,18V20H4V18C4,15.79 7.58,14 12,14Z"/>
                    </svg>
                    <input 
                        type="email" 
                        placeholder="Email Address"
                        class="input-field"
                        v-model="email"
                    >
                </div>
    
                <div class="input-group">
                    <svg class="icon" viewBox="0 0 24 24">
                        <path fill="currentColor" d="M12,17A2,2 0 0,0 14,15C14,13.89 13.1,13 12,13A2,2 0 0,0 10,15A2,2 0 0,0 12,17M18,8A2,2 0 0,1 20,10V20A2,2 0 0,1 18,22H6A2,2 0 0,1 4,20V10C4,8.89 4.9,8 6,8H7V6A5,5 0 0,1 12,1A5,5 0 0,1 17,6V8H18M12,3A3,3 0 0,0 9,6V8H15V6A3,3 0 0,0 12,3Z"/>
                    </svg>
                    <input 
                        type="password" 
                        placeholder="Password"
                        class="input-field"
                        v-model="password"
                    >
                </div>

                <div class="input-group">
                    <svg class="icon" viewBox="0 0 24 24">
                        <path fill="currentColor" d="M12,17A2,2 0 0,0 14,15C14,13.89 13.1,13 12,13A2,2 0 0,0 10,15A2,2 0 0,0 12,17M18,8A2,2 0 0,1 20,10V20A2,2 0 0,1 18,22H6A2,2 0 0,1 4,20V10C4,8.89 4.9,8 6,8H7V6A5,5 0 0,1 12,1A5,5 0 0,1 17,6V8H18M12,3A3,3 0 0,0 9,6V8H15V6A3,3 0 0,0 12,3Z"/>
                    </svg>
                    <input 
                        type="text" 
                        placeholder="Username"
                        class="input-field"
                        v-model="username"
                    >
                </div>
    
                <button @click="clickRegister" class="auth-btn">
                    <span>Sign In</span>
                    <svg class="arrow-icon" viewBox="0 0 24 24">
                        <path fill="currentColor" d="M4,11V13H16L10.5,18.5L11.92,19.92L19.84,12L11.92,4.08L10.5,5.5L16,11H4Z"/>
                    </svg>
                </button>
            </div>
        </div>
    </div>
    </template>
    
<style scoped lang="scss">
    .container {
        display: flex;
        min-height: 100vh;
      
        align-items: center;
        justify-content: center;
        padding: 2rem;
    }
    
    .auth-card {
     
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2.5rem;
        width: 100%;
        max-width: 400px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        transform: translateY(0);
        transition: transform 0.3s ease;
    
        &:hover {
            transform: translateY(-5px);
        }
    }
    
    .header {
        text-align: center;
        margin-bottom: 2rem;
    
        h2 {
            color: #2d3748;
            font-size: 1.8rem;
            margin-bottom: 0.5rem;
            font-weight: 700;
        }
    
        p {
            color: #718096;
            font-size: 0.9rem;
        }
    }
    
    .input-group {
        position: relative;
        margin-bottom: 1.5rem;
    
        .icon {
            position: absolute;
            left: 1rem;
            top: 50%;
            transform: translateY(-50%);
            width: 20px;
            height: 20px;
            color: #a0aec0;
            z-index: 2;
            transition: color 0.3s ease;
           
        }
    }
    
    .input-field {
        width: 100%;
        padding: 0.9rem 1rem 0.9rem 2.8rem;
        border: 1px solid #8e60f4;
        border-radius: 10px;
        font-size: 0.95rem;
        color: #2d3748;
        transition: all 0.3s ease;
        background-color: #121212;
      
    
        &:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    
            ~ .icon {
                color: #667eea;
            }
        }
    
        &::placeholder {
            color: #a0aec0;
        }
    }
    
    .auth-btn {
        width: 100%;
        padding: 1rem;
        background:#8e60f4;
        color: white;
        border: none;
        border-radius: 10px;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        transition: all 0.3s ease;
        margin-top: 1rem;
    
        &:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
        }
    
        .arrow-icon {
            width: 18px;
            height: 18px;
            color: white;
        }
    }
    
    @media (max-width: 480px) {
        .auth-card {
            padding: 1.5rem;
        }
    }
    </style>