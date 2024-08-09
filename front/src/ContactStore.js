import { writable } from "svelte/store";



export const ContactStore = writable([
    {
        id: 0, 
        name: "John Doe",
        email: "H3Ig6@example.com",
        message: "Hello, how are you?",
    }
]);