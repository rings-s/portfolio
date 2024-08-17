<script>
	import { ContactStore } from './../../ContactStore';
	import { onMount } from 'svelte';

	onMount(async () => {
		try {
			const endpoint = 'http://127.0.0.1:8000/api/contacts/';
			const response = await fetch(endpoint);
			if (!response.ok) {
				throw new Error(`HTTP error! status: ${response.status}`);
			}
			const data = await response.json();
			console.log(data);
			ContactStore.set(data);
		} catch (error) {
			console.error('Failed to fetch blogs:', error);
		}
	});
</script>


<div class="max-w-4xl mx-auto p-4 bg-white mt-12 shadow-lg rounded-lg">
    {#each $ContactStore as contact}
        <div class="p-4 mb-4 border-b last:border-b-0 rounded">
            <h1 class="text-xl font-semibold text-gray-900">{contact.name}</h1>
            <p class="text-gray-600">{contact.email}</p>
            <p class="text-sm text-gray-500">{contact.message}</p>
        </div>
    {/each}

    
</div>
