import { writable } from "svelte/store";


export const ProjectStore = writable([
    {
        id: 0,
        name: "John Doe",
        description: "Hello, how are you?",
        
        created_at: "2022-01-01",
        client: "John Doe",
        logo_img: 'https://www.rollingstone.com/wp-content/uploads/2022/09/Big-Lebowski-2.jpg?resize=1800,1800&w=1800',
        end_date: "2022-01-01"
    }
]);

