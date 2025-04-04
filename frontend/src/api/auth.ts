import axios from "axios";
import type { UserLogin, NewUser } from "@/models/auth";

export async function loginUser(userLogin:UserLogin){
    try {
        const response = await axios.post(
            "http://localhost:8000/api/users/auth/login", 
            userLogin, 
            {
              headers: {
                "Content-Type": "application/json",
                
              }
            }
          );
        
        
        if (response.status == 200) {
            return response.data;
        } else {
            console.error("Unexpected data format:", response.data);
            return null; 
        }
    } catch (error) {
       
        if (axios.isAxiosError(error)) {
            console.error("Error message:", error.message);
            console.error("Error response:", error.response?.data);
        } else {
            console.error("Unexpected error:", error);
        }
        return null; 
    }
}



export async function registerUser(newUser:NewUser){
    try {
        const response = await axios.post("http://localhost:8000/api/users/auth/register", {"newUser":newUser });
        
        if (response.status == 200) {
            return response.data;
        } else {
            console.error("Unexpected data format:", response.data);
            return null; 
        }
    } catch (error) {
       
        if (axios.isAxiosError(error)) {
            console.error("Error message:", error.message);
            console.error("Error response:", error.response?.data);
        } else {
            console.error("Unexpected error:", error);
        }
        return null; 
    }
}
