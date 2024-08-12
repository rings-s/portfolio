import { writable } from "svelte/store";


export const BlogStore = writable([
    {
        id: 0, 
        title: "John Doe",
        description: "CEO",
        // image
        created_at: "2022-01-01"
        }
]);