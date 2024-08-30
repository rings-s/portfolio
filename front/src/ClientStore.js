import { writable } from "svelte/store";



export const ClientStore = writable([
    {
        id: 0, 
        user: "John Doe",
        phone_number: "555-555-5555",
        // profile_image
        email: 'ringo@yahoo.com',
        created_at: "2022-01-01"
    }
]);
