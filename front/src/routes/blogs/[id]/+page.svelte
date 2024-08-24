<script>
	import { BlogStore } from '../../../BlogStore.js';
    import { onMount } from 'svelte';

    export let data;
    let blog;
    let id;

    onMount(async function() {
        try {
            id = data.id;  // Ensure id is set for use in the component
            blog = $BlogStore.find(b => b.id === id);
            
            if (!blog) {  // Fetch blog if not found in store
                const endpoint = `http://localhost:8000/api/blogs/${id}/`;
                const response = await fetch(endpoint);
                if (response.ok) {
                    blog = await response.json();
                } else {
                    throw new Error('Failed to fetch blog from backend');
                }
            }
        } catch (error) {
            console.error('Error in blog fetching:', error.message);
            blog = null;  // Set blog to null in case of any errors
        }
    });
</script>

	<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-12">
		<div class="max-w-3xl mx-auto p-4 shadow rounded-lg ">
			{#if blog}
				<div class="my-4 p-5 border-b last:border-b-0">
					<h1 class="text-2xl font-bold text-gray-900">{blog.title}</h1>
					<p class="text-sm text-gray-600">{blog.created_at}</p>
					<p>{blog.description}</p>
				</div>
				<a href="/blogs/{blog.id}" class="text-gray-600">details</a>

			{:else}
				<p>No blog was found with ID {id}...</p>
			{/if}
		</div>


	</div>

