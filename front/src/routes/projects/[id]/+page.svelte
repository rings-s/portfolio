<script>
    import { ProjectStore } from './../../../ProjectStore';
    import { onMount } from 'svelte';
    export let data;

    let project;
    let id;

    onMount(async function() {
        try {
            id = data.id;  // Ensure id is set for use in the component
            project = $ProjectStore.find(p => p.id === id);
            
            if (!project) {  // Fetch project if not found in store
                const endpoint = `http://localhost:8000/api/projects/${id}/`;
                const response = await fetch(endpoint);
                if (response.ok) {
                    project = await response.json();
                } else {
                    throw new Error('Failed to fetch project from backend');
                }
            }
        } catch (error) {
            console.error('Error in project fetching:', error.message);
            project = null;  // Set project to null in case of any errors
        }
    });
</script>

<div class="max-w-7xl mx-auto p-6">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        {#if project}
            <div>
                <img class="w-full h-72 object-cover rounded-t-lg md:rounded-lg" src={project.logo.startsWith('http') ? project.logo : `http://localhost:8000${project.logo}`} alt={project.name}/>
            </div>
            <div class="shadow-lg rounded-lg overflow-hidden">
                <div class="p-5">
                    <h1 class="text-2xl font-bold text-gray-900">{project.name}</h1>
                    <div class="mt-4">
                        <p class="text-sm text-gray-600">Start: {project.created_at}</p>
                        <p class="text-sm text-gray-600">Client: {project.client}</p>
                        <p class="text-sm text-gray-600">End: {project.end_date}</p>
                        <p class="text-sm text-gray-600">{project.description}</p>
                    </div>
                </div>
            </div>
        {:else}
            <p class="text-lg text-red-500">No project found</p>
        {/if}
    </div>
</div>
