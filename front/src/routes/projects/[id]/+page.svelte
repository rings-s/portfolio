<script>
    import { ProjectStore } from '../../../ProjectStore.js';
    import { onMount } from 'svelte';


    onMount(async function () {
        if ($ProjectStore.length) {
            const endpoint = 'http://127.0.0.1:8000/api/projects/'
            const response = await fetch(endpoint)
            const data = await response.json()

            // console.log(data)

            ProjectStore.set(data)

        }
       
    })
    
</script>



<div class="max-w-7xl mx-auto p-6">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        {#each $ProjectStore as project}

            <div>
                <img class="w-full h-72 object-cover rounded-t-lg md:rounded-lg" src="{project.logo_img}" alt="{project.name}">

            </div>
            <div class=" shadow-lg rounded-lg overflow-hidden">
               
               
                <div class="p-5">
                    <h1 class="text-2xl font-bold text-gray-100">{project.name}</h1>
                    <div class="mt-4">
                        <p class="text-sm text-gray-200">Start: {project.created_at}</p>
                        <p class="text-sm text-gray-200">Client: {project.client}</p>
                        <p class="text-sm text-gray-200">End: {project.end_date}</p>
                        <p>{project.description}</p>
                    </div>
                   
                </div>
            </div>
           
        {/each}
    </div>

    
</div>
