import { writable } from "svelte/store";


export const ProjectStore = writable([
    {
        id: 0,
        name: "John Doe",
        description: "Hello, how are you?",
        // file
        created_at: "2022-01-01",
        client: "John Doe",
        // logo_img
        end_date: "2022-01-01"
    }
]);