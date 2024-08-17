import { writable } from "svelte/store";


export const ProjectStore = writable([
    {
        id: 0,
        name: "John Doe",
        description: "Hello, how are you?",
        
        created_at: "2022-01-01",
        client: "John Doe",
        logo_img: 'media/project_logos/dummy_imgs_8cEPBPE.png',
        end_date: "2022-01-01"
    }
]);

