import { writable } from "svelte/store";


export const TestimonialStore = writable([
    {
        id: 0, 
        title: "John Doe",
        description: "CEO",
        // image
        created_at: "2022-01-01"
        }
]);