import type { Anime } from "@/models/mainPage";
import axios from "axios";

export async function getDataOnMainPage(): Promise<Anime[] | null> {
    try {
        const response = await axios.get("http://localhost:8000/api/stream/get_serial_for_main_page");
        
        
        if (Array.isArray(response.data)) {
            console.log(response.data as Anime[])
            return response.data as Anime[];
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
