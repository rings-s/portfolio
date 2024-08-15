<script>
    import { ProjectStore } from './../../ProjectStore.js';
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
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {#each $ProjectStore as project}
            <div class="bg-white shadow-lg rounded-lg overflow-hidden">
                
                <div class="p-5">
                    <h1 class="text-2xl font-bold text-gray-900">{project.name}</h1>
                    <p class="text-gray-700">{project.description}</p>
                    <div class="mt-4">
                        <p class="text-sm text-gray-600">Start: {project.created_at}</p>
                        <p class="text-sm text-gray-600">Client: {project.client}</p>
                        <p class="text-sm text-gray-600">End: {project.end_date}</p>
                    </div>
                </div>
            </div>
        {/each}
    </div>

    <button type="button" class="px-6 py-2 mt-6 bg-blue-500 hover:bg-blue-600 text-white font-semibold rounded-md transition-colors" 
    >
        Add a Project
    </button>
</div>
