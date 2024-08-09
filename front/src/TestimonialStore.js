import { writable } from "svelte/store";



export const ContactStore = writable([
    {
        id: 0, 
        client_name: "John Doe",

        client_image: "H3Ig6@example.com",

        project_name: "Hello, how are you?",
        date: "2022-01-01",
        testimonial_body: "Hello, how are you?",

    }
]);